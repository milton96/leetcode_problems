class RecentCounter:
    def __init__(self):
        self.req = [None]
        

    def ping(self, t: int) -> int:
        self.req.append(t)

    def p(self) -> None:
        print(self.req)

if __name__ == "__main__":
    obj = RecentCounter()
    obj.ping(1)
    obj.p()