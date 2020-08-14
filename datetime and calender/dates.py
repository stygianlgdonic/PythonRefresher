from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is: ", today)

    # print out the date's individual components
    print("Date Components: ", today.year, today.month, today.day)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Weekday: ", today.weekday())
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Which is: ", days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("Date & Time: ", today)

    # Get the current time
    print("Current Time: ", today.time())


if __name__ == "__main__":
    main()

