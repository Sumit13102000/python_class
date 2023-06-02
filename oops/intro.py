#a = 1
#b = a+c


class Greeting:
    name=""
    def init (self,name):
        print("constructor is emoked")
        self.name = name

    def say_hello_world(self):
        print("Hello,World")

    def say_hello(self,name):
        print(f"hello,{name}")

    def say_hello_name(self):
        print(f"hello,{self.name}")    

    def __str__(self) -> str:
        return "This is a Greet Class"
           

obj = Greeting()
print(obj.name)
obj.say_hello_name()

print(obj)
#obj.say_hello_world()
#obj.say_hello("world")