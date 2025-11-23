from redis import Redis


class Queue:
    def __init__(self):
        self.client = Redis(host='localhost', decode_responses=True)
        self.queue = 'queue'

    def enqueue(self, *args):
        for name in args:
            self.client.rpush(self.queue, name)

    def dequeue(self, number=1):
        self.client.lpop(self.queue, number)
    
    def peek(self, start=-1, end=-1):
        # Defaults to peeking at the last item in the queue   
        print(self.client.lrange(self.queue, start, end))

    def trim(self):
        self.client.ltrim(self.queue, 999, 0)

    def insert(self, rel_position, element, new_element):
        self.client.linsert(self.queue, rel_position, element, new_element)


queue = Queue()

# Trim the queue to avoid duplicates caused by re-running the script
queue.trim()

# Add people to the queue
queue.enqueue("Carol Shaw", "Elizabeth Carr", "Ernest Ramos", "Carlos Ramirez")
queue.peek(0, -1)

# See the last one
queue.peek()

# Remove one person
queue.dequeue()
queue.peek(0, -1)

# Insert new person in the middle of the queue
queue.insert('AFTER', 'Elizabeth Carr', 'John Doe')
queue.peek(0, -1)
