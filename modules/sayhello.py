class SayHello:
    def __init__(self, target="World"):
        self.target = target
    def say(self):
        print(f"Hello, {self.target}!!")
        print("Nice to meet you!")
if __name__ == '__main__':
    app = SayHello()
    app.say()
    app = SayHello("Someone")
    app.say()
