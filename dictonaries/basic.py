my_dictionary = {'key': "value"}

course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

print(course['teacher'])

print(course.keys())

print(course.values())

print(sorted(course.values()))

course['home'] = "Seattle"

#delete key and value

del(course['home'])

for item in course:
    print(item)

for key, value in course.items():
    print("{"+key + " : " + value+ "}")
