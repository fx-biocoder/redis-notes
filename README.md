# Redis notes (work in progress)

This repository contains notes for Redis and a Python script to test Redis commands.

## How to run

On Windows Powershell:

```bash
docker run -d --name my-redis-container -p 6739:6379 redis:7

python3 -m app.py
```

## Contents

- The `notes/` directory contains notes for several features from Redis.
- `app.py` contains a basic script to verify that Redis server is running correctly.
- `queue.py` implements a basic Redis queue.
