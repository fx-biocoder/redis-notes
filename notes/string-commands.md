### Does Redis store numbers?

No, Redis only stores strings instead of numbers.

### What commands can I use to handle numbers stored in strings?

The commands `INCR` and `DECR` allow you to increment or decrement a value stored at a key by one. The syntax is:

```bash
# Increments by 1 and returns the new value
$ INCR [key]

# Decrements by 1 and returns the new value
$ DECR [key]
```

You can also increment or decrement by a given value using the `INCRBY` or `DECRBY` commands, using the following syntax:

```bash
# Increment by 5
$ INCRBY [key] 5

# Decrement by 5
$ DECRBY [key] 5
```

### Why not use `GET`/`SET` to increment numbers

`GET` and `SET` are slower than `INCR` and `DECR`. Therefore, due to performance issues it's best to use the latter commands.

### How can I know the length of a string?

You can use the `STRLEN` command. The syntax is:

`STRLEN [key]`

### How can I append a string to another that is inside a key?

You can use the `APPEND` command. The syntax is:

`APPEND [key] [string to append]`

### How can I get a portion of a string inside a key?

You can use the `GETRANGE` command, which uses a zero-based index. The syntax is:

`GETRANGE [key] [start index] [end index]`
