### What is a hash map?

It is a map where each key maps to a single value.

### What are hash maps used for?

They are used for representing complex structures like objects with multiple properties.

### What is the storage capacity for hash maps?

Hash maps can store up to four billion properties within a single map.

### What commands are used for hashes?

The command `HSET` is used to set values in a hashmap, while `HGET` is used to retrieve values. The syntax is:

```bash
HSET [key] [field 1] [value 1] [field 2] [value 2] ... [field n] [value n]

HGET [key] [field]
```

### Provide an example of an use case for hash maps

User information in memory (e.g., user ID, name, avatar URL, and role). Another example is shopping carts.

### Can you read more than one key in a hash map?

Yes, by using the `HMGET` command. The syntax is:

`HMGET [key] [field a] [field b] [field c] ... [field n]`

### What naming strategy can I use for keys?

You can use this naming strategy:

`table:primary-key` (e.g., `loggedUser:123` to get the user with `ID = 123`)

### Can I increment or decrement values in a hash map?

Yes, using the `HINCRBY` command, which can also take negative numbers. The syntax is:

`HINCRBY [key] [field] [number]`

### Can I retrieve all the data in a hash map?

Yes, using the `HGETALL` command. The syntax is:

`HGETALL [key]`

### Can I know how many fields are stored in a hash map?

Yes, using the `HLEN` command. The syntax is:

`HLEN [key]`
