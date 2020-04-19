# Formatting output
x = "Item one : {}, Item two : {}".format("ali", "alireza")
y = "Item one : {a}, Item two : {b}".format(a="ali", b="alireza")

print(x)
print(y)

# List

lst = [1, 2, 3, 4, 5, 6]
lst2 = [7, 8, 9, 10]
lst.append(lst2)  # appending the lst2 as one element in the lst
lst.extend(lst2)  # add all items in the lst2 to the lst
print(lst)

# remove an item from the list
last_item_in_list = lst.pop()
print(last_item_in_list)
print(lst)

third_item = lst.pop(2)
print(third_item)
print(lst)

# reverse list
lst.reverse()
print(lst)

numbers_list = [4.545, 56.4, 2.8, 2]
numbers_list.sort()
print(numbers_list)

# matrix
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list comprehension
first_col = [row[0] for row in mat]
print(first_col)

# dictionaries do not have order
my_stuff = {"key1": "value1", "key2": "value2"}
print(my_stuff["key1"])

my_stuff["key1"] = "new value 1"  # reassignment by key
my_stuff["key3"] = "value3"  # add a new item to the dictionary

# to know the type of an object
my_list = [1, 2, 3, 5]
print(type(my_list))


class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    # Class attributes
    species = "mammal"
    pi = 3.14

    def __init__(self, name, age, radius):
        Animal.__init__(self)  # calling this function is optional
        print("Dog created")
        self.name = name
        self.age = age
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Dog.pi

    def set_radius(self, new_r):
        self.radius = new_r

    def eat(self):
        print("Dog eating")

    def __str__(self):
        return "This is a dog name: {n}, age: {a}".format(n=self.name, a=self.age)

    def __len__(self):
        return self.age

    def __del__(self):
        print("This method will be called when the object delete")


my_dog = Dog(name="Pico", age=10, radius=10)
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_dog)
print(len(my_dog))
del my_dog

import re

patterns = ["term1", "term2"]
text = "This is text having the term1 not the other one"

for pat in patterns:
    print("Searching for: ", pat)
    if re.search(pat, text):
        print("Match!")
    else:
        print("not found")

index = re.search("term1", text)
print("index is: ", index.start())

split_term = '@'
user = "user@gmail.com"
print(re.split(split_term, user))

pattern = "sd?"  # having s with zero or one d
pattern = "sd{3}"  # having s with 3 d followed by the s
pattern = "sd{2, 3}"  # having s with 2 or 3 d followed by the s
pattern = "s[sd]"  # having s with followed by one s or one d

# a \ should be escape in normal python string, to do this
test_pat = [r'\d+']  # return sequence of digits
test_pat2 = [r'\D+']  # return sequence of Non digits
test_pat3 = [r'\s+']  # return sequence of white space
test_pat4 = [r'\S+']  # return sequence of NON white space
test_pat5 = [r'\w+']  # return sequence of words not symbols included
test_pat6 = [r'\W+']  # return sequence of NON alphanomical
test_sen = "test 124345 symbol %$%$"
print(re.findall(test_pat[0], test_sen))
print(re.findall(test_pat2[0], test_sen))
print(re.findall(test_pat3[0], test_sen))
print(re.findall(test_pat4[0], test_sen))
print(re.findall(test_pat5[0], test_sen))
print(re.findall(test_pat6[0], test_sen))
