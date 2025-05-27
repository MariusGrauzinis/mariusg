class A:
    pass

    def start(self) -> None:
        print("A started")

    def stop(self) -> None:
        print("A stopped")

    @staticmethod
    def len_string(self, string: str) -> int:
        return len(string)


my_class = A()
my_class.start()
my_class.stop()

print(my_class.len_string("Hello"))




