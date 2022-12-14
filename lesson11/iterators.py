my_list = [1, 2, 3, 4]


# for i in my_list:
#     print(i)

# list_iter = iter(my_list)
# print(next(list_iter))
# print(next(list_iter))


# range implementation
class MyNumbers:

    def __init__(self, start: int = 0, end: int = 10, steps: int = 1):
        self.start = start - 1
        self.end = end
        self.steps = steps

    def __iter__(self):
        self.a = self.start
        return self

    def __next__(self):
        if self.a > self.end or self.a + self.steps > self.end:
            # to stop next() from iterating, StopIteration exception is raised:
            raise StopIteration()
        self.a += self.steps
        return self.a


for i in MyNumbers(-4, 10):
    print(i)
