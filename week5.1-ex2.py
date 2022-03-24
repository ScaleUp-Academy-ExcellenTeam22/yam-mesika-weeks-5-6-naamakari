from calendar import calendar
import random
import datetime

dictionary_of_months = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30,
                        '10': 31, '11': 30, '12': 31}


def checks_year(year):
    """The function checks if the year is 'meuberet', means February have 29 days and not 28 """
    if int(year) % 4 != 0:  # not divide by 4
        return False
    if int(year) % 100 == 0 and int(year) % 400 != 0:  # dividing by 100 and not by 400
        return False
    return True


def check_structure(my_date):
    """Checks if the structure of the date is in this form:YYYY-MM-DD """
    lst = my_date.split('-')
    if len(lst[0]) != 4:
        return False
    if len(lst[1]) != 2:
        return False
    if len(lst[2]) != 2:
        return False
    return True


def find_day(new_date):
    """Find the day in the week of the date"""
    # create the date to the form that the function strptime gets
    fix_date = new_date[:4]+' '+new_date[5:7]+' '+new_date[8:]
    day_in_week = datetime.datetime.strptime(fix_date, '%Y %m %d').weekday()
    return day_in_week


def main():
    date1 = input("Please enter 2 dates in the form YYYY-MM-DD:\n")
    date2 = input()
    if check_structure(date1) and check_structure(date2):
        date_parts1 = date1.split('-')  # separate the dates to parts- year, month and day
        date_parts2 = date2.split('-')
        new_year = random.randint(int(date_parts1[0]), int(date_parts2[0]))
        if new_year == int(date_parts1[0]):  # the same like the first year
            new_month = str(random.randint(int(date_parts1[1]), 12)).zfill(2)
            if new_month == '02':
                if checks_year(new_year):
                    range_for_days = 29
                else:
                    range_for_days = dictionary_of_months[new_month]
            else:
                range_for_days = dictionary_of_months[new_month]
            if new_month == date_parts1[1]:
                new_day = str(random.randint(int(date_parts1[2]), range_for_days)).zfill(2)
            else:
                new_day = str(random.randint(1, range_for_days)).zfill(2)
        elif new_year == int(date_parts2[0]):  # the same like the second year
            new_month = str(random.randint(1, int(date_parts2[1]))).zfill(2)
            if new_month == date_parts2[1]:
                new_day = str(random.randint(1, int(date_parts2[2]))).zfill(2)
            else:
                range_for_days = dictionary_of_months[new_month]
                new_day = str(random.randint(1, range_for_days)).zfill(2)
        else:  # between the years
            new_month = str(random.randint(1, 12)).zfill(2)
            range_for_days = dictionary_of_months[new_month]
            new_day = str(random.randint(1, range_for_days)).zfill(2)
        new_date = str(new_year)+'-'+str(new_month)+'-'+new_day
        print("The new date between the dates is:", new_date)
        if find_day(new_date) == 0:  # monday is 0 and sunday is 6
            print("I do not have vinaigrette!")


if __name__ == '__main__':
    main()

