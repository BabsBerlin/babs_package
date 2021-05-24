from datetime import datetime

def try_me():
    return "Barbara says hello!"

def days_left():
    today = datetime.now()
    the_end = datetime(year=2021, month=6, day=11)
    return(f'There are only {(the_end - today).days} days left until the last day of this amazing bootcamp!')