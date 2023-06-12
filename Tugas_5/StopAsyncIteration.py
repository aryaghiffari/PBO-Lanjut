try:
    class AsyncIterator():
        def __init__(self):
            self.counter = 0
        def __aiter__(self):
            print(self)
    
    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        print(self.counter)
finally:
    print("iterator telah selesai")
    