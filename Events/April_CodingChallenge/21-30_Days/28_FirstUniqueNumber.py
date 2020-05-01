class FirstUnique:

    def __init__(self, nums: List[int]):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self) -> int:
        while self.d and self.c[self.d[0]] != 1:
            self.d.popleft()
        return self.d[0] if self.d else -1

    def add(self, value: int) -> None:
        self.c[value] += 1
        self.d.append(value)
