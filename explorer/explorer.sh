#!/bin/bash
cd "$(dirname "$0")"
pip install -q watchdog 2>/dev/null
echo "Explorer: http://localhost:3117"
open http://localhost:3117
python server.py
