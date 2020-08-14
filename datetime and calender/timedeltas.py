from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=2, minutes=12))

# print today's date
today = datetime.now()
print("Today is: ", today)

# print today's date one year from now
print("1 year later: " + str(today + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("1 year and 2 weeks later: " + str(today + timedelta(days=365, weeks=2)))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A, %d, %B, %Y")
print("one week ago, it was ", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

if afd < today:
    print("Already went by %d days ago" % ((today - afd).days))
    afd = afd.replace(year=today.year + 1)


# Now calculate the amount of time until April Fool's Day

days_left = afd - today
print("its just", days_left.days, "days away now!")
