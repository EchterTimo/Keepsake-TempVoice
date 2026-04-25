#!/bin/bash

read -p "Enter environment (leave blank for none): " ENV

if [ -z "$ENV" ]; then
    echo "Starting without specific environment..."
    docker compose up -d --build
else
    echo "Starting environment: $ENV..."
    docker compose -p "$ENV" up -d --build
fi
