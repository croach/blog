Title: Everything You Need to Know About Python Timezones
Slug: python-timezones
Date: 2016-12-31 15:09
Tags: python
Author: Christopher Roach
Status: draft
Summary: Everything one needs to know about using timezones in Python

### Why Are Timezones Such a Pain in Python?

There are two main reasons why timezones are painful in Python. The
first is simply that timezones are just a pain to deal with in general.
The differences between the abstract concept of a date versus the
pinpoint exactitude of a timestamp can be frustrating to deal with at
best and can be the cause some very rousing debates in your team's
architecture discussions. The default strategy to just make everything a
UTC based timestamp sounds nice at first blush, but take, for example,
an employee's start date. If we make this data type a UTC based
timestamp in our database, what happens when we convert it into that
employee's timezone? Without careful consideration, that employee may be
reporting to work on Tuesday the 18th rather than Monday the 17th like
you originally intended. Perhaps, in this situation, what you really
wanted is something much more general, say a simple date instead of a
full fledged timezone aware date and time. From this example, it's easy
to see just how important forethought and planning are in getting your
timezone strategy just right.

The second reason that timezones can be an annoyance is much more
specific to Python. While <span
style="font-size: 10.0pt;line-height: 13.0pt;">Python comes with a
library for supporting dates and times called
[datetime](http://docs.python.org/2/library/datetime.html), its
creators, in all their infinite wisdom, have essentially decided to punt
on the topic of timezones. The datetime library does, however, provide a
way for the user to hook their own implementation of a timezone object
into the library. To this end, the tzinfo abstract class is provided.
Luckily for us we don't have to worry about creating our own
implementation though, since the creators of the
[pytz](http://pytz.sourceforge.net/) library have already taken care of
that task for us. Given that pytz is the de facto standard in the Python
world for dealing with timezones, the rest of this document will assume
that you've already installed it in your local environment.</span>

### Python datetime Do's and Dont's

Don't use naive datetime objects - If you think you need a naive datetime
object, perhaps you actually want a date object instead.

Don't use localized datetime objects - Try to do everything in UTC if
you can. If you can't, consider again whether you need a different data
type such as a date.

Don't do arithmetic on localized datetime objects - Try only to do
arithmetic on UTC datetime objects, it's much cleaner since there is no
such thing as daylight savings time.

Do use
[normalize](http://pytz.sourceforge.net/#localized-times-and-date-arithmetic)
after performing arithmetic on localized datetime objects - If you
absolutely must do arithmetic on localized datetime objects, make sure
you call the normalize method on the result. This should take care of
any daylight savings time issues that come up.

Don't do comparisons on localized datetime objects - Again, try,
whenever possible, [to do everything in UTC
time](http://pytz.sourceforge.net/#problems-with-localtime) since it's
safer than localized times and, if you must do the comparison on
localized times, consider again if you're using the correct data type
for the job.

Do use
dt.[astimezone](http://docs.python.org/2/library/datetime.html#datetime.datetime.astimezone)(pytz.utc)
before comparing datetime objects - Turn timezone aware datetime objects
into UTC time before doing any work with them. The nice thing to is
that, if the datetime object is already in UTC time, this call is
essentially free since the astimezone function just returns the original
object, so feel free to do this blindly to any datetime objects you
have.

Do be careful when using dt.replace(tzinfo=timezone) - Unlike the
timezone.localize method, replace [tries to do some thinking for
you](http://stackoverflow.com/questions/1379740/pytz-localize-vs-datetime-replace)
with respect to daylight savings time. It's safer just to work with UTC
times or convert datetime objects using astimezone instead of trying to
do so by hand.

Don't use datetime(…, tzinfo=timezone) to create a timezone aware
datetime object - Don't pass timezone object into the datetime
constructor, it's
[broken](http://pytz.sourceforge.net/#localized-times-and-date-arithmetic).
Instead, create the datetime object and call timezone.localize on it.

Do use timezone.localize(datetime(…)) to add a tzinfo object to a
datetime object - Use the localize method to add a tzinfo object to a
datetime object.

Don't use timezone.localize for localizing datetime objects - The
localize method probably doesn't do what you think it does. It simply
replaces the tzinfo object on the datetime object and nothing more. If
you want to convert a datetime object from one timezone to another, use
the astimezone method.

Do use dt.astimezone to localize datetime objects - This is the correct
method to call to convert a datetime object from one timezone to
another.

Don't use datetime.utcnow() - This will always return a naive datetime
object.

Do use datetime.now(pytz.utc) - This is the preferred way to get the
current UTC date and time since it will return a timezone aware datetime
object.

### Display Times in a Local Time Zone in MySQL

If you've ever wanted to see the times in a table in the local time
zone, rather than calculating everything in your head, you're in luck.
MySQL provides a function that will allow you to do just that, but you
may have to do a little work first to get it to work.

So, let's take a look at a simple query that uses the
[CONVERT\_TZ](http://dev.mysql.com/doc/refman/5.1/en/date-and-time-functions.html#function_convert-tz)
function that MySQL provides. The example query below shows the start
and end times of every interview in the database in HireIn's default
local time zone (i.e., 'US/Pacific' or 'California time').

Simple `CONVERT_TZ` example:

```sql
SELECT CONVERT_TZ(i.start_time, 'UTC', 'US/Pacific'),
       CONVERT_TZ(i.end_time, 'UTC', 'US/Pacific')
FROM interviews i;
```

The `CONVERT_TZ` function is very simple, it just takes the DATETIME
object you want to convert, the time zone to convert it from (in our
case, this should always be 'UTC'), and the time zone to convert it to.

Now, if you run this query and get back a bunch of NULL's, you have a
little setup to do first before you can do the conversion. 

The problem that you're running into, is MySQL has a table that keeps track of
what each of the time zones are and how to calculate the difference in times,
but that table is currently empty. In fact, we can confirm that this is the
case by taking a peak at the number of records in this table. If you'd like to
do that, just execute the line below at the command line.

Check if `time_zone` is populated

```sh
% echo 'select count(*) from time_zone' | mysql -uroot -p mysql
```

If you get back a zero when you execute the line above, the table is
empty and needs to be populated for the `CONVERT_TZ` function to work
properly.

To populate the table, just execute the line below at the command line.

Populate the `time_zone` table

```sh
% mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql
```

Once you've executed the line above, the table should be properly
populated and you can verify this by once again running the command that
checks the number of records in the `time_zone` table. If the number
comes back greater than zero this time, the table is populated and the
`CONVERT_TZ` function should now work. Go ahead and run the original
SELECT statement from the beginning of this section and you should now
be seeing all start and end times in the local time zone rather than the
NULL's that you were seeing before.

Before we leave this section, I'd like to point out that you don't have
to use time zones to get the `CONVERT_TZ` function to work. Instead, you
could just use offset times. So, for example, if we wanted to show the
interview times in 'US/Pacific' time, we could just use the following
SELECT statement with offsets instead of time zones.

`CONVERT_TZ` with offsets instead of time zones

```sql
SELECT CONVERT_TZ(i.start_time, '+00:00', '-08:00'),
       CONVERT_TZ(i.end_time, '+00:00', '-08:00')
FROM interviews i;
```

This statement actually works without populating the time\_zone table,
so it'll work in a pinch if you don't want to take the time to run the
population command, but keep in mind that you are specifying an exact
offset, so this won't work across DST boundaries. For example, in the
statement above, we specify an offset of 8 hours, so as long as we are
looking at start and end times that occurred during standard time,
everything will be correct, but if we wanted to look at some times
during daylight savings time, what's returned will be off by one hour.
Considering how easy it is to populate the `time_zone` table, the only
reason I can see not to do it is if you don't have permissions to do
(or, maybe you just forgot the root password).

Ok, so maybe that was 10 minutes...

### Helpful Links

-   [datetime — Basic date and time
    types](http://docs.python.org/2/library/datetime.html)
-   [pytz — World Timezone Definitions for
    Python](http://pytz.sourceforge.net/)
-   [Localized times and date
    arithmetic](http://pytz.sourceforge.net/#localized-times-and-date-arithmetic)
-   [Problems with localized
    time](http://pytz.sourceforge.net/#problems-with-localtime)
-   [MySQL CONVERT\_TZ
    function](http://dev.mysql.com/doc/refman/5.1/en/date-and-time-functions.html#function_convert-tz)

