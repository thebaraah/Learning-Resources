#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PID_FILE=".pid"

if [ ! -f "$PID_FILE" ]; then
  echo "Not running (no PID file)"
  exit 0
fi

PID=$(cat "$PID_FILE")

if ! kill -0 "$PID" 2>/dev/null; then
  echo "Not running (PID $PID no longer exists), cleaning up PID file"
  rm "$PID_FILE"
  exit 0
fi

echo "Sending SIGTERM to PID $PID..."
kill "$PID"

for i in $(seq 1 10); do
  if ! kill -0 "$PID" 2>/dev/null; then
    echo "Stopped gracefully"
    rm -f "$PID_FILE"
    exit 0
  fi
  sleep 1
done

echo "Process didn't stop, sending SIGKILL..."
kill -9 "$PID" 2>/dev/null || true
rm -f "$PID_FILE"
echo "Killed"
