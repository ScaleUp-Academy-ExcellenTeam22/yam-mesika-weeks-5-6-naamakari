from calendar import calendar
from calendar import monthrange
import random
import datetime


def check_date_format_and_correctness(my_date: str) -> bool:
    """
    Checks if the format of the date is in this form:YYYY-MM-DD.
    :param my_date: The date to check.
    :return: Is the given date in the correct format and also makes sense.
    """
    try:
        datetime.datetime.strptime(my_date, '%Y-%m-%d')
        return True
    except ValueError as value_error:
        raise ValueError(value_error)


def find_day(new_date: str) -> int:
    """
    Find the day in the week of the date.
    :param new_date: The date to check which day it is the week.
    :return: The number of the day, monday is 0 and sunday is 6.
    """
    # Create the date to the form that the function strptime gets.
    return datetime.datetime.strptime(new_date[:4] + ' ' + new_date[5:7] + ' ' + new_date[8:], '%Y %m %d').weekday()


def raffle_dates_according_inputs_dates(date_parts1: list, date_parts2: list) -> str:
    """
    The function raffle values to the new date between the two dates it received.
    :param date_parts1: List of the components of the first date.
    :param date_parts2: List of the components of the second date.
    :return: String of the new date.
    """
    new_year = random.randint(int(date_parts1[0]), int(date_parts2[0]))
    # The same like the first year.
    if new_year == int(date_parts1[0]):
        new_month = str(random.randint(int(date_parts1[1]), 12)).zfill(2)
        if new_month == date_parts1[1]:
            new_day = str(random.randint(int(date_parts1[2]), monthrange(int(new_year), int(new_month))[1])).zfill(2)
        else:
            new_day = str(random.randint(1, monthrange(int(new_year), int(new_month))[1])).zfill(2)
    # The same like the second year.
    elif new_year == int(date_parts2[0]):
        new_month = str(random.randint(1, int(date_parts2[1]))).zfill(2)
        if new_month == date_parts2[1]:
            new_day = str(random.randint(1, int(date_parts2[2]))).zfill(2)
        else:
            new_day = str(random.randint(1, monthrange(int(new_year), int(new_month))[1])).zfill(2)
    # Between the years.
    else:
        new_month = str(random.randint(1, 12)).zfill(2)
        new_day = str(random.randint(1, monthrange(int(new_year), int(new_month))[1])).zfill(2)
    return str(new_year) + '-' + str(new_month) + '-' + new_day


def main():
    date1 = input("Please enter 2 dates in the form YYYY-MM-DD:\n")
    date2 = input()
    try:
        if check_date_format_and_correctness(date1) and check_date_format_and_correctness(date2):
            # Separate the dates to parts- year, month and day.
            date_parts1 = date1.split('-')
            date_parts2 = date2.split('-')
            new_date = raffle_dates_according_inputs_dates(date_parts1, date_parts2)
            print("The new date between the dates is:", new_date)
            # Monday is 0 and sunday is 6.
            if find_day(new_date) == 0:
                print("I do not have vinaigrette!")
    except ValueError as value_error:
        print(value_error)


if __name__ == '__main__':
    main()

