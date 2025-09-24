def inline_heading(
    test: str,
    chars: int = 120,
    char: str = "-",
    offset: int = 5,
    separator: str = " ",
    should_print: bool = True
) -> str:
    """
    Create a separator line with text inside.

    Args:
        test (str): The text to insert.
        chars (int): Total length of the line.
        char (str): Character to use for the separator.
        offset (int): Number of chars before the text.
        separator (str): String used before and after the text.
        should_print (bool): If True, prints the formatted line to stdout.

    Returns:
        str: A formatted separator line.
    """
    # Length of fixed part: left offset + separators + text
    fixed_len = offset + len(separator) + len(test) + len(separator)
    available_space = chars - fixed_len
    if available_space < 0:
        return "> " + test

    # Build line
    string = f"{char * offset}{separator}{test}{separator}{char * available_space}"
    if should_print:
        print(string)
    return string


def blank_line():
    """print a line of 120 dashes."""
    print("-" * 120)


if __name__ == '__main__':
    # Example usage:
    print(inline_heading("example text"))
    print(inline_heading("example text", separator=" "))
