import re
import sys
def main():
    full_str = input("Hours: ")
    times = find_times(full_str)  # send find_times to extract times
    start_time = convert_military(times[0])
    end_time = convert_military(times[1])
    print(f'{start_time} to {end_time}')



def find_times(full_str):
    matches = re.search(r"(\d.+) to (\d.+)", full_str)
    if matches:
        #print(matches.groups)
        first, second = matches.groups()
        #print(f'first:{first}, second:{second}')
        return first,second
    else:
        raise ValueError("Include AM or PM and use 'to' between times")



def convert_military(time):
    '''
    first check to see if time entered is in form 11:00 AM
    '''
    matches = re.search(r"(\d+):(\d+) ([AP]M)",time)
    if matches:
        #print(f'trying match with colon: {matches.groups()}')
        hours,minutes,meridian = matches.groups()
        #print(f'hours:{hours}  minutes{minutes} meridian {meridian}')
        if int(minutes) >59:            # verify that minutes is less than 60
            raise ValueError("Minutes should be 59 or less")
            sys.exit()
        elif meridian == 'PM':          # if time is PM add 12 hours to hours to convert
                                        # to military time
            hours = int(hours) + 12
        return f'{hours}:{minutes}'     # return time in military time
    '''
    next check to see if time entered in form 9 AM
    '''
    else:
        matches = re.search(r"(\d+) ([AP]M)",time)                  # searches for digit or digits
        if matches:
            #print(f'reached match without colon {matches.groups()}')
            hour,meridian = matches.groups()
            if int(hour)>12:                                                # times with hours more than 12 are not valid when uning AM/PM
                print("hour should be less than 12 when using AM PM notation")
                raise ValueError
            else:
                #print(f'{hour}, meridian: {meridian}')
                if meridian == 'PM':                                        # for example 5 PM converts to 17:00
                    hour = int(hour)+12
                    return f'{hour}:00'
                else:                                                       # for example 5 AM converts to 05:00
                    return f'{hour}:00'
        else:
            raise ValueError



if __name__ == '__main__':
    main()