from redis import Redis

r = Redis(host='localhost', port=6379, db=0, decode_responses=True)

try:
    print("Using SET command with 'name' = 'John Doe'...")
    output = r.set('name', 'John Doe')
    print(output)

    print("Using GET command to retrieve 'name'...")
    output = r.get('name')
    print(output)

    print("Redis is setup correctly!")
except Exception as e:
    print("Error: {e}")
