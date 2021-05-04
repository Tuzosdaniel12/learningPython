nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)

student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]

sliced_gpas = student_gpas[2:6]

print(sliced_gpas)


#length
student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]

length = len(student_gpas)
#max value of number, letter contain greater value then number
max_gpa = max(student_gpas)

#min value of sequence number contain lower value then alphabet
min_gpa = min(student_gpas)