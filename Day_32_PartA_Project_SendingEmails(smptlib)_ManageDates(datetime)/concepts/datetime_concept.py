import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
today = dt.datetime.today()
day_of_the_week = now.weekday()  # 0 is monday

date_of_birth = dt.datetime(year=2000,month=9,day=19)
print(day_of_the_week)
