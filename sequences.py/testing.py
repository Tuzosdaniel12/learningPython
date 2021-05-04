docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

print(docs.count('tuple'))

print(docs.index('tuple'))#.index() will return the index of first match, if not found then Value Error will be thrown

#list and tuples
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits # False
'eggplant' not in fruits # True

'eggplant' in vegetables # True
'eggplant' not in vegetables # False

#index
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list

#count
my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat') # 2
my_pets.count('lizard') # 0

#Range

nums = range(10)

0 in nums # True
10 in nums # False
4 in nums # True

0 not in nums # False
15 not in nums # True
10 not in nums # True


nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True