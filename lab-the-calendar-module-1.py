# Create a class called MyCalendar that extends the Calendar class;
# create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
# in your implementation, use the monthdays2calendar method of the Calendar class.

import calendar
class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, day_weekday in week:
                    if day_weekday == weekday and day != 0:
                        count += 1
        return count


print(MyCalendar().count_weekday_in_year(2020, 1))
print(MyCalendar().count_weekday_in_year(2000, 6))
