import datetime

def before_NY():
    time_now = datetime.datetime.now()
    last_new_year = datetime.datetime(time_now.year, 1, 1)
    return (time_now-last_new_year).days

