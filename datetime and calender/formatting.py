from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes

    #### Date Formatting ####
    now = datetime.now()

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("Year Formats: %y, %Y"))
    print(now.strftime("Weekday Formats: %a, %A"))
    print(now.strftime("Month Formats: %b, %B"))
    print(now.strftime("Day Format: %d"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale's date and time: %c"))
    print(now.strftime("Locale's date: %x"))
    print(now.strftime("Locale's time: %X"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("12 Hour Formatting: %I : %M : %S %p"))
    print(now.strftime("24 Hour Formatting: %H : %M : %S"))


if __name__ == "__main__":
    main()
