# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

print("The following country are available, choose on frome 9")
i = 1
mapper = {0 : "quit it"}
for x in pytz.country_names :

    print("{}: {}: {}".format(i, x, pytz.country_names[x]))
    new = {i : x}
    mapper.update(new)
    i = i+1
    if i == 10 :
        break


while True:
    serial = int(input("Enter the serial number: "))
    if serial not in [0,10]:
        country = mapper[serial]
        if country in pytz.country_names:

            if country in pytz.country_timezones:
                for zone in pytz.country_timezones(country):
                    print("The current time at {} is {} ".
                          format(pytz.country_names[country],datetime.datetime.now(tz=pytz.timezone(zone))))
                    print("The current time at {} is {} ".format(pytz.country_names["IN"],datetime.datetime.now()))
                    print("The current time at {} is {} ".format("UTC",datetime.datetime.utcnow()))

        else:
            print("Time zone not found")

    else:
        break