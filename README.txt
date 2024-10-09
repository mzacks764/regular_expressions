reg_expressions.py is a python script that searches for the string um  (case insensitive) in a longer string and returns a count of how many times um appears.
input: string to search
output: count of number of times 'um' appears.

working.py takes a string listing working hours and converts it to military times.
input: starting time to ending time.  Starting and ending times may be written with only hours (i.e. '9 AM') or with hours and minutes (i.e. '7:45 PM')
output: starting time to ending time in military time. (i.e. '09:00 AM to 19:45 PM')

watch.py takes a string of html code and looks for a link to www.youtube.com/xxxx where xxx represents the rest of the full youtube address.  If found it extracts this link.  It then converts the link to a youtu.be/xxxx
address.
input: html string that may contain www.youtube.com/xxx
output link to web address youtu.be/xxx or None if no youtube link is found.
