import calendar
print(calendar.month(2026, 11))
print(calendar.calendar(2026))
calendar.prcal(2027)
# calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2026, 12)
print(calendar.weekday(2026, 12, 25))
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print(calendar.isleap(2020))
print(calendar.leapdays(1966, 2026))

# calendar.Calendar – provides methods to prepare calendar data for formatting;
# print(calendar.Calendar().getfirstweekday())
# print(calendar.Calendar().itermonthdates(2026, 11))
# print(calendar.Calendar().itermonthdays(2026, 11))
# print(calendar.Calendar().monthdatescalendar(2026, 11))
# print(calendar.Calendar().monthdayscalendar(2026, 11))
# print(calendar.Calendar().yeardatescalendar(2026, 1))
# print(calendar.Calendar().yeardays2calendar(2026, 1))
# print(calendar.Calendar().yeardayscalendar(2026, 1))
# print(calendar.Calendar().monthdays2calendar(2026, 11))
# print(calendar.Calendar().yeardays2calendar(2026, 1))
# print(calendar.Calendar().itermonthdays2(2026, 11))
# print(calendar.Calendar().itermonthdays3(2026, 11))
# print(calendar.Calendar().itermonthdays4(2026, 11))
# print(calendar.Calendar().iterweekdays())

# calendar.TextCalendar – is used to create regular text calendars;
calendar.setfirstweekday(calendar.MONDAY)
print(calendar.TextCalendar().formatmonth(2026, 11))
print(calendar.TextCalendar().formatyear(2026,0, 1, 1, 3))

print(calendar.TextCalendar().formatmonth(2026, 11))

print(calendar.month(2026, 11))

print("\n#============================")

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print("\n#============================")

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

print("\n#============================")

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

print("\n#============================")

for data in c.monthdays2calendar(2020, 12):
    print(data)

print("\n#============================")



# calendar.HTMLCalendar – is used to create HTML calendars;
print(calendar.HTMLCalendar().formatmonth(2026, 11))


