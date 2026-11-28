from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
import time

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

timestamp = time.time()
print("Timestamp:", timestamp)

d2 = date.fromisoformat('2019-11-04')
print(d2)

d3 = date(1991, 2, 5)
print(d3)

d3 = d3.replace(year=1992, month=1, day=16)
print(d3)

d4 = date(2019, 11, 4)
print(d4.weekday())


t = datetime(2019, 11, 4, 14, 53, 20, 1).time()

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(1)


timestamp2 = 1572879180
print(time.ctime(timestamp2))

print(time.ctime())


# time.struct_time:
#     tm_year   # specifies the year
#     tm_mon    # specifies the month (value from 1 to 12)
#     tm_mday   # specifies the day of the month (value from 1 to 31)
#     tm_hour   # specifies the hour (value from 0 to 23)
#     tm_min    # specifies the minute (value from 0 to 59)
#     tm_sec    # specifies the second (value from 0 to 61 )
#     tm_wday   # specifies the weekday (value from 0 to 6)
#     tm_yday   # specifies the year day (value from 1 to 366)
#     tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # specifies the timezone name (value in an abbreviated form)
#     tm_gmtoff # specifies the offset east of UTC (value in seconds)

timestamp3 = 1572879180
print(time.gmtime(timestamp3))
print(time.localtime(timestamp3))
print(time.strftime("%H:%M:%S", time.gmtime(timestamp3)))


timestamp4 = 1572879180
st = time.gmtime(timestamp4)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


dt3 = datetime(2020, 11, 4, 14, 53)
print(dt3.strftime("%y/%B/%d %H:%M:%S"))

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())


print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())


dt2 = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt2.timestamp())

d3 = date(2020, 1, 4)
print(d3.strftime('%Y/%m/%d'))


timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))


print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)


delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

