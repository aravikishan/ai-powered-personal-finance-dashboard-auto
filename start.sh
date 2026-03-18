#!/bin/bash
set -e
echo "Starting AI-Powered Personal Finance Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9040 --workers 1
