import time
from interactions import (
    Extension,
    listen,
    Member,
    GuildVoice,
    Guild,
    ChannelType,
    GuildChannel,
    Task,
    IntervalTrigger
)
from interactions.api.events import (
    VoiceUserJoin,
    VoiceUserMove,
    VoiceUserLeave,
    ExtensionLoad,
    Ready,
    Startup
)
from config import (
    GENERATOR_CHANNEL_ID,
    MAX_CHANNELS_PER_CATEGORY,
    CATEGORIES,
    IGNORED_CHANNELS,
    GUILD_ID,
    CREATION_COOLDOWN
)
from utils import inline_heading, blank_line

inline_heading("Settings: general")
print("Env MAX_CHANNELS_PER_CATEGORY:", MAX_CHANNELS_PER_CATEGORY)
print("Env CREATION_COOLDOWN:", CREATION_COOLDOWN)

inline_heading("Settings: guild")
print("Env GUILD_ID:", GUILD_ID)
print("Env GENERATOR_CHANNEL_ID:", GENERATOR_CHANNEL_ID)
print("Env IGNORED_CHANNELS:", IGNORED_CHANNELS)
print("Env CATEGORIES:", CATEGORIES)


class TempVoice(Extension):
    @listen(ExtensionLoad)
    async def on_extension_load(self, event: ExtensionLoad):
        print(f"Extension {event.extension.name} loaded")

    @listen(Ready)
    async def on_ready(self, event: Ready):
        guild = self.bot.get_guild(GUILD_ID)
        if not guild:
            print(
                f"[ERROR] Guild with ID {GUILD_ID} not found! The bot needs to be installed in that guild.")
            return
        await self.force_fetch_category_data(guild)

    @listen(Startup)
    async def on_startup(self, event: Startup):
        self.cleanup_cooldowns.start()
        print("started cleanup task")

    @Task.create(IntervalTrigger(minutes=1))
    async def cleanup_cooldowns(self):
        '''
        Periodically clean up old entries in the user_last_channel_creation dict
        to prevent it from growing indefinitely.
        '''
        # print("storage:", self.user_last_channel_creation)
        user_ids = list(self.user_last_channel_creation.keys())
        for user_id in user_ids:
            current_time = int(time.time())
            last_creation_time = self.user_last_channel_creation[user_id]
            if current_time - last_creation_time > CREATION_COOLDOWN:
                del self.user_last_channel_creation[user_id]
                # print(f"Cleaned up cooldown entry for user {user_id}")

    def __init__(self, bot):
        self.bot = bot
        self.category_channels: dict[int, list[int]] = {}

        self.user_last_channel_creation: dict[int, int] = {}
        '''user_id -> unix timestamp'''

    # Translate events into join and leave

    @listen(VoiceUserJoin)
    async def on_voice_user_join(self, event: VoiceUserJoin):
        await self.handle_voice_join(event.author, event.channel)

    @listen(VoiceUserMove)
    async def on_voice_user_move(self, event: VoiceUserMove):
        await self.handle_voice_leave(event.author, event.previous_channel)
        await self.handle_voice_join(event.author, event.new_channel)

    @listen(VoiceUserLeave)
    async def on_voice_user_leave(self, event: VoiceUserLeave):
        await self.handle_voice_leave(event.author, event.channel)

    # Custom event handlers
    async def handle_voice_join(self, member: Member, channel: GuildVoice):

        # skip if wrong guild
        if channel.guild.id != GUILD_ID:
            return

        # skip if not joining the generator channel
        if channel.id != GENERATOR_CHANNEL_ID:
            return

        # find the best category to create the channel in
        best_category = await self.get_best_category(member.guild)
        if best_category is None:
            print("[NOT GOOD] No available categories to create a new channel in")
            return

        # enforce user cooldown to prevent rapid join/leave exploits
        if not await self.can_create_channel(member):
            return

        # create the temporary channel and move the user
        _ = await self.create_temp_channel_and_move(member, best_category)

    async def handle_voice_leave(self, member: Member, channel: GuildVoice):

        # skip if wrong guild
        if channel.guild.id != GUILD_ID:
            return

        # skip if channel is not a temp channel
        if not await self.is_temp_channel(channel):
            return

        # check if the channel is now empty
        if not await self.channel_is_empty(channel):
            return

        # delete the channel
        await self.delete_temp_channel(channel)

    # Util Functions
    async def create_temp_channel_and_move(
        self,
        member: Member,
        category_id: int
    ) -> GuildVoice:
        '''
        - create a temporary voice channel
        - move the member to that channel
        - return the created channel
        '''
        new_channel = await member.guild.create_voice_channel(
            name=f"{member.user.username}'s VC",
            category=category_id,
            reason=f"User {member.username} ({member.id}) joined the generator channel"
        )
        await self.add_channel_to_category(category_id, new_channel.id)
        await member.move(new_channel.id)
        return new_channel

    async def delete_temp_channel(self, channel: GuildVoice) -> None:
        # safety check
        if not channel.type == ChannelType.GUILD_VOICE:
            return

        await channel.delete(
            reason='Last user left temporary voice channel'
        )
        await self.remove_channel_from_category(channel.category.id, channel.id)

    async def force_fetch_category_data(self, guild: Guild):
        self.category_channels = {}
        channels = await guild.fetch_channels()
        channels.sort(key=lambda c: c.position)
        inline_heading("Fetched category data")
        for category in channels:

            # skip non-category channels. GuildCategory inherits from GuildChannel
            if category.type != ChannelType.GUILD_CATEGORY:
                continue

            # skip categories not in the specified list
            if category.id not in CATEGORIES:
                continue

            # add category if not already present
            print(f'Found category: {category.id}, "{category.name}"')
            self.category_channels.setdefault(category.id, [])

            for vc in category.channels:

                # add channel to the category
                self.category_channels[vc.category.id].append(
                    vc.id)

        all_channels = [ch for chs in self.category_channels.values()
                        for ch in chs]
        print('Found', len(all_channels),
              'channel(s) in the provided categories.')

    async def channel_is_empty(self, channel: GuildVoice) -> bool:
        user_amount = len(channel.voice_members)
        return user_amount == 1

    async def get_best_category(self, guild: Guild) -> int | None:
        '''
        Use the first category with available slots.
        '''
        for category_id, channel_ids in self.category_channels.items():
            voice_channel_amount = len(channel_ids)
            if voice_channel_amount < MAX_CHANNELS_PER_CATEGORY:
                return category_id

        return None

    async def is_temp_channel(self, channel: GuildVoice) -> bool:
        '''
        A temp channel is any voice channel in the specified categories that:
        - is in the specified guild
        - is in one of the specified categories
        - is not the generator channel.
        - is not in the ignored channels list
        '''
        if channel.guild.id != GUILD_ID:
            return False

        if channel.parent_id not in CATEGORIES:
            return False

        if channel.id == GENERATOR_CHANNEL_ID:
            return False

        if channel.id in IGNORED_CHANNELS:
            return False

        return True

    async def add_channel_to_category(self, category_id: int, channel_id: int):
        self.category_channels[category_id].append(channel_id)

    async def remove_channel_from_category(self, category_id: int, channel_id: int) -> bool:
        if category_id not in self.category_channels:
            return False
        if channel_id in self.category_channels[category_id]:
            self.category_channels[category_id].remove(channel_id)
            return True
        return False

    async def can_create_channel(self, member: Member) -> bool:
        '''
        Check if the user is allowed to create a new channel based on cooldown.
        '''

        current_time = int(time.time())
        last_creation_time = self.user_last_channel_creation.get(member.id, 0)

        if current_time - last_creation_time < CREATION_COOLDOWN:
            return False

        self.user_last_channel_creation[member.id] = current_time
        return True
