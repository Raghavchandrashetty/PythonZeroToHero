import datetime

print(f"Current date time : {datetime.datetime.now()}")

print(f"Current date time : {datetime.datetime.today()}")
print(f"Current date time : {datetime.date.today()}")
# print(f"Current date time : {datetime.time.hour()}")
# print(f"Current date time : {datetime.time.minute}")
# print(f"Current date time : {datetime.time.microsecond}")


print(datetime.date(2024, 12, 25))
print(datetime.time(21, 26, 00))
print(datetime.datetime(2024, 12, 25, 21, 26, 00))
date_string = "2023-07-08"
# print(f"Current date time : {datetime.datetime.day()}")
date_object = datetime.date(2023, 7, 8)
date_string = date_object.strftime("%Y-%m-%d")
print("Date String:", date_string)


datetime_object = datetime.datetime(2023,7,8,15,30,35)
datetime_string = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
print(f"datetime_string : {datetime_string}")
print(f"datetime_string : ", datetime_string)

today = datetime.datetime.today()
print("today " , today)
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)
print(f"tomorrow : {tomorrow}")
print(f"yesterday : {yesterday}")

#date difference

date1 = datetime.date(2023, 7, 1)
date2 = datetime.date(2023, 7, 8)

difference = date2-date1
print("difference : ", difference)

now = datetime.datetime.now()
later = now + datetime.timedelta(hours=2, minutes=30)
earlier = now - datetime.timedelta(hours=1, minutes=15)
print("Later:", later)
print("Earlier:", earlier)

import pytz

timezone = pytz.timezone("America/New_York")
datetime_with_timezone = datetime.datetime.now(timezone)
print("Datetime with Timezone:", datetime_with_timezone)

utc = pytz.utc
newyork_tz = pytz.timezone("America/New_York")
datetime_utc = datetime.datetime.now(utc)
datetime_est = datetime.datetime.now(newyork_tz)
print(datetime_utc)
print(datetime_est)


time_string= "15:30:45"
time_object = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
print("Parsed Time : " , time_object)

time_object = datetime.time(15, 30, 45)
time_string = time_object.strftime("%H:%M:%S")
print(time_string)


date_string=datetime.date(2023, 7, 1)
datetime_str = datetime.datetime.strftime(date_string, "%m-%d-%Y")
# time_object = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
print(type(datetime_str))
print("Parsed Time : " , datetime_str)

import pytz
print(pytz.__version__)


# print(f"Current date time : {datetime.datetime.day()}")
# print(f"Current date time : {datetime.datetime.month()}")
# print(f"Current date time : {datetime.datetime.year()}")
# print(f"Current date time : {datetime.datetime.hour()}")
# print(f"Current date time : {datetime.datetime.minute()}")
# print(f"Current date time : {datetime.datetime.second()}")
# print(f"Current date time : {datetime.datetime.microsecond()}")