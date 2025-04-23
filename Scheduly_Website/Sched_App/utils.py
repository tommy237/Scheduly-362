# Sched_App/utils.py

EPOCH_WEEKDAY = 4
MONTH_NAMES = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
WEEKDAY_NAMES = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year):
    return {
        "January":   31,
        "February":  29 if is_leap(year) else 28,
        "March":     31,
        "April":     30,
        "May":       31,
        "June":      30,
        "July":      31,
        "August":    31,
        "September": 30,
        "October":   31,
        "November":  30,
        "December":  31,
    }

def count_leaps(upto):
    return upto//4 - upto//100 + upto//400

def days_before_year(y):
    years = y - 1970
    leaps = count_leaps(y-1) - count_leaps(1969)
    return years*365 + leaps

def days_before_month(y,m):
    dim = days_in_month(y)
    total=0
    for name in MONTH_NAMES[:m-1]:
        total += dim[name]
    return total

def days_since_epoch(y,m,d):
    return days_before_year(y) + days_before_month(y,m) + (d-1)

def weekday(y,m,d):
    return (days_since_epoch(y,m,d) + EPOCH_WEEKDAY) % 7

def first_weekday_of_month(y,m):
    return weekday(y,m,1)
