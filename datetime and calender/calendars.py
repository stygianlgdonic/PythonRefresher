# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
cal = c.formatmonth(2020, 1)
print(cal)

# create an HTML formatted calendar
htmlCal = calendar.HTMLCalendar(calendar.MONDAY)
cal = htmlCal.formatmonth(2020, 1)
print(cal)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2020, 1):
    print(i)


# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meatings will be on:")
for m in range(1, 13):

    cal = calendar.monthcalendar(2020, m)

    week1 = cal[0]
    week2 = cal[1]

    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
