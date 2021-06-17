import datetime

now = datetime.datetime.now()

today = datetime.datetime.combine(datetime.date.today(), datetime.time())


print(f"{today.year}")  # year
print(f"{today.month}")  # month
print(f"{today.day}")  # day
print(f"{today.hour}")  # hour
print(f"{today.weekday()}")  # weekday, Monday is index 0
print(f"{now.timestamp()}") #timestamp


def minutes(dtime1, dtime2):
    deltat = dtime2 - dtime1
    return round(deltat.total_seconds() / 60)

#  format date by using this function string for time
print(now.strftime("%m/%d/%y"))

# str parse time

birthday = datetime.datetime.strptime("2014-04-21", "%Y-%m-%d")

birthday_party = datetime.datetime.strptime("2014-04-21 12:00", "%Y-%m-%d %H:%M")

print(birthday)

print(birthday_party)

## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
def to_string(date):
    return date.strftime("%d %B %Y")

print(to_string(now))