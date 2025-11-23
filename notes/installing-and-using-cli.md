### How to install

Follow the instructions in [Redis.io](https://redis.io) to install. For Windows, use this:

```bash
# Start Redis server
$ docker run -d --name redis -p 6379:6379 redis:<version>

# Connect with Redis CLI
$ docker exec -it redis redis-cli

# If you have redis-cli installed locally:
$ redis-cli -h 127.0.0.1 -p 6379
```

### What components does Redis have?

The Redis server (which handles command logic) and the Redis client (which interfaces with the server).

### What commands should I use?

Use `redis-server` to start the server and `redis-client` to start the client. You can run multiple clients simultaneously from different terminals.
