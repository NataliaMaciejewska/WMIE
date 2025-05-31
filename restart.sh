#!/bin/bash

echo "🧹 Cleaning up..."
docker compose down --volumes --remove-orphans
docker image prune --all --force

echo "🔨 Rebuilding..."
docker compose build --no-cache

echo "🚀 Starting fresh containers..."
docker compose up --force-recreate