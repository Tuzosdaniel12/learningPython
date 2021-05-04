obj1 = [1, 2, 3, 4, 5]
obj2 = [6, 7, 8, 9, 10]

obj1 = obj1 + obj2

print(obj1)

#concat
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums3 = nums1 + nums2 # [1, 2, 3, 4, 5, 6]

#count
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.count(4.0) # 2

#in
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

3.2 in student_gpas # True

#index
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.index(4.0) # 1

#len
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

len(my_pets) # 4

#max
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

max(student_gpas) # 4.0

#min
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

min(student_gpas) # 1.5

#multiply
nums1 = [1, 2, 3]

nums1 * 2 # [1, 2, 3, 1, 2, 3]


#not in 
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

'Jellybean' not in my_pets # True

#slice
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas[1:3] # [4.0, 3.2]

#Mutable Sequence Only Operations
#Append
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

my_pets.append('Vera') # ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

#del
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

del my_pets[0:2] # ['Ernie', 'Squash', 'Vera']

#insert
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

fruits.insert(2, 'kiwi') # ['apple', 'banana', 'kiwi', 'orange', 'pear', 'strawberry']

#pop
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

apple = fruits.pop(0) # ['banana', 'orange', 'pear', 'strawberry'], apple = 'apple'

#remove
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.remove(4.0) # [2.5, 3.2, 2.9, 3.7, 1.5, 4.0]

#reverse
my_pets = ['Ernie', 'Squash', 'Vera']

my_pets.reverse() # ['Vera', 'Squash', 'Ernie']