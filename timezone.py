from datetime import datetime
import pytz
a = 'Asia/Calcutta'
tz = pytz.timezone(a)
b = datetime.now(tz)
print(b)
#for i in pytz.all_timezones:
    #print(i)
