# class myclass:
#     x = 5
#
#
# a = myclass()
# print(a.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person('SALMAN', 55)
# print(p1.name)
# print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def myfunc(self):

        print('hello my name is ' + self.name)


a = Person('SALMAN', 55)

a.myfunc()
