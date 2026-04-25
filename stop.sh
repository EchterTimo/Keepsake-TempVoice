#!/bin/bash

read -p "Enter environment (leave blank for none): " ENV

if [ -z "$ENV" ]; then
    echo "Stopping..."
    docker compose down
else
    echo "Stopping environment: $ENV..."
    docker compose -p "$ENV" down
fi
