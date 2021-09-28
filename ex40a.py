# this is based on code examples in the book, 
# that were not meant to be as a separate exercise to type in
# but I did it anyway, in this form

import mystuff

mythings ={
    "apples": "apple, Apple, APPLE!",
    "tangerine": "Tangerine, Tangerine"
}

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("I'M CLASSY APPLES!")

# dict style
print(mythings['apples']) 
print(mythings['tangerine'])

# module style
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)