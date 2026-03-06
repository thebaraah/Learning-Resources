#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PID_FILE=".pid"

if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    echo "Already running (PID $PID)"
    exit 0
  fi
  echo "Removing stale PID file (PID $PID no longer exists)"
  rm "$PID_FILE"
fi

nohup node server.js >> /dev/null 2>&1 &
echo $! > "$PID_FILE"
echo "Started (PID $!)"
