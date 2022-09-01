import datetime

def new_year_time():
    time_now = datetime.datetime.now()
    new_year = datetime.datetime(time_now.year+1, 1, 1)
    return (new_year-time_now).days