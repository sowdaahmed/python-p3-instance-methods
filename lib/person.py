
#!/usr/bin/env python3


class Person:
    def __init__(self, name="Guido", age=0):  # Provide defaults so Person() works
        self.name = name
        self.age = age

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
