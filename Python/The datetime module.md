![](https://edube.org/uploads/media/default/0001/02/9d991359070d226d0ae497f442ee1b4511b2a435.png)
# The `datetime` module 
## date class

Is an object that describing the date, and it has several Read-only attributes such as day, month, year, weekend... (use `replace` method to replace/change the attributes).

```python
from datetime import date
today = date(2019, 11, 4)
print(today.year)  # 2019
print(today.day)   # 4
print(today.month) # 11

# 0 is Monday and 6 is Sunday
print(today.weekday)

today = today.replace(year=2003, month=1, day=15)
```
### Note

The `replace` method returns a changed _date_ object, so you must remember to assign it to a variable.
### today method

The instance Objects  of `date`  class represent a date consisting of the year, month, and day.  get the current local date using the `today` method.

```python
today = date.today()
```

### fromisoformat method

Takes a date in the YYYY-MM-DD format

![](https://edube.org/uploads/media/default/0001/02/datetime.01.04.png)

```python
d = date.fromisoformat('2019-11-04')
```


## The `time` class

`time` class allows you to present time.

```python
# time(hour=0, minute=0, second=0, microsecond=0)
t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
```

## The `datetime` class

Those are the some and the return datetime object with all attribute that we have already seen like day, house second year...

```python
datetime.datetime.now()
datetime.datetime.today()
```

# The `time` module

## `time` method

In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the **Unix epoch**, because this is when the counting of time began on Unix systems.

```python
from datetime import date
import time

# Many seconds passed since 1970
timestamp = time.time()

print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
```

You can reverse the process (getting timestamp from an existing date) using this method:

```python
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
```

## The `sleep` method

```python
time.sleep(5) # Stop the interpretation for 5s
```

## `datetime` to formatting string

`strftime` allows us to return the date and time in the format we specify, by adding a second argument consist of [directives](https://strftime.org/) that control the string formatting.

```python
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
```

## Formatting string to `datetime`

The `strptime` method requires you to specify the format in which you saved the date and time, and it return an `datetime` object.

```python
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
```

## Date and time operations

The `timedelta` is an object that could be created by the class constructor, which are: `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, and `weeks`. Each of them is optional and defaults to 0.

The `timedelta` is very useful in context of doing arithmetic operation between `datetime` objects, here is a few examples:

```python
from datetime import timedelta, date, datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
```