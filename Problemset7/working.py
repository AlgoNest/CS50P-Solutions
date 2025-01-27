import re

def main():
    print(convert(input("Hours: ")))
#                               Here the first hours (([0-9][0-2]* with 0 or more repeation):*with colon 0 or more repeation
#                                now the minute time ([0-5][0-9])*) ([A-P]M) now we accepting from to [A to P] with M and so the other side
def convert(s):
         timematch = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
         if timematch:
               time = timematch.groups()
            # here the format will occur if enter 9:00 AM to 5:00 PM
            #    ('9:00', '9', '00', 'AM', '5:00', '5', '00', 'PM')
            #       0      1     2     3     4      5     6    7
               if int(time[1]) > 12 or int(time[5]) > 12:
                     raise ValueError
               else:
                     first_time = new_format_of_time(time[1], time[2], time[3])
                     second_time = new_format_of_time(time[5], time[6], time[7])
                     return  first_time + " to " + second_time
         else:
               raise ValueError
        #  we can make another function for formating the 24 hours of time
        # it looks to more things at place
        # but we can divide the section's like in the store's
def new_format_of_time(hour, minute, am_pm):
    if am_pm == "PM":
            if int(hour) == 12:
                  new_hour = 12
            else:
                  new_hour = int(hour) + 12
    else:
            if int(hour) == 12:
                  new_hour = 0
            else:
                  new_hour = int(hour)
    if minute == None:
       new_minute = ":00"
       new_time = f"{new_hour:02}" + new_minute
    else:
      new_time = f"{new_hour:02}" + ":" + minute

    return new_time



if __name__ == "__main__":
    main()
