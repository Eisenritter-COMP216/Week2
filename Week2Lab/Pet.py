'''
Author: George Zhou
Date: September 22, 2020

This is the Pet (Separted from test harness for organization and modularization) Class
'''
class Pet:
    # default initializers
    name = ''
    age = 0
    owner = ''
    trained: bool = 0

    # default constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_owner(self, name):
        self.owner = name

    def train(self):
        self.trained = 1

    # printing data members
    def __str__(self):
        return f'Hi I am {self.age}yrs old and my name is {self.name} ' \
               f'\nI am {"" if self.trained else "not "}house trained ' \
               f'and {"no one" if self.owner == "" else self.owner} owns me.'
