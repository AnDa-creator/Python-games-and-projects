# import time
#
# print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[1], time.timezone))
#
# if time.daylight != 0:
#     print("\t Daylight Saving time is in effect for this location")
#     print("\tThe DST timezone is "+ time.tzname[1])
#
# print("Local Time is " + time.strftime('%z'))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now)
print(datetime.datetime.utcnow())
print(datetime.tzinfo())