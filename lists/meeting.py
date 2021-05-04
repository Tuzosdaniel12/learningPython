attendee = ["Ken", "Alena", "Dan"]

print("They are", len(attendee), "attendees currently")

#adding to the end of the list
attendee.append("Junior")
attendee.append("Nathen")

print("They are", len(attendee), "attendees currently")


another_attendee = ["Adriana", "Juan"]

#two arrays together
# attendee.extend(another_attendee )
# print("They are", len(attendee), "attendees currently")


#if you don't want to create ne array then added them and store the result
new_array = attendee + another_attendee 

to_line = ", ".join(attendee)
cc_line = ", ".join(another_attendee)

split_list_back = to_line.split(", ")