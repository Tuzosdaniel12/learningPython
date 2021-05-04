# def print_teacher(name, job, topic):
#     print(name)
#     print(job)
#     print(topic)
    
# print_teacher('Ashley', 'Instructor', 'Python')


def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')
print_teacher(name='Ashley', job='Instructor', topic='Python') # = print_teacher(**teacher)


teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

print_teacher(**teacher)