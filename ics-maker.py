# A Python script for creating ICS (iCal) files
# An author:
#  _          _       ____            _ _        
# | |   _   _| | __  / ___|___   __ _(_) |_ ___  
# | |  | | | | |/ / | |   / _ \ / _` | | __/ _ \ 
# | |__| |_| |   <  | |__| (_) | (_| | | || (_) |
# |_____\__,_|_|\_\  \____\___/ \__, |_|\__\___/ 
#                               |___/            

import os
import pathlib
from datetime import datetime

# https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory
working_dir = os.path.dirname(os.path.realpath(__file__))

# https://stackoverflow.com/questions/22947427/getting-home-directory-with-pathlib
home_dir = pathlib.Path.home()

organizer_set = False

def convert_time(time_string):
    try:
        dt = datetime.strptime(time_string, "%d-%m-%Y %H:%M")
        cal_dt = dt.strftime("%Y%m%dT%H%M%SZ")
        return cal_dt

    except:
        print("Invalid time/date input format, interrupting")
        exit(1)

if "organizer.conf" not in str(os.listdir(path=working_dir)):
    inp = input("An organizer info is not set, do you want to set it up now? [Y/n] ")

    if inp.lower() in ["y", "yes", "n", "no", ""]:

        if "y" in inp.lower() or inp == "":
            name = input("Insert your full name: ")
            email = input("Insert your e-mail address: ")
            organizer = name + "\n" + email
            
            with open(f"{working_dir}/organizer.conf", "w") as file:
                file.write(organizer)

            organizer_set = True


    else:
        print("Interrupted")
        exit(1)

else:
    organizer_set = True

    with open(f"{working_dir}/organizer.conf", "r") as file:
        organizer = file.readlines()
        name = organizer[0].strip()
        email = organizer[1].strip()



items = {
    "a name":"",
    "a beginning (dd-mm-YYYY HH:MM)":"",
    "an end (dd-mm-YYYY HH:MM)":"",
    "a location (optional)":"",
    "a description (optional)":""
    }

for item in items:
    if "optional" not in item:
        num_iterrations = 0
        
        while items[item] == "":
            
            if num_iterrations > 0:
                print("Error: invalid input")
            
            value = input(f"Insert {item} of an event: ")
            items[item] = value
            num_iterrations += 1

            if "dd-mm" in item:
                items[item] = convert_time(items[item])
    else:
        value = input(f"Insert {item} of an event: ")
        items[item] = value


ics = f"""
BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
DTSTAMP:{datetime.now().strftime("%Y%m%dT%H%M%SZ")}
DTSTART:{items["a beginning (dd-mm-YYYY HH:MM)"]}
DTEND:{items["an end (dd-mm-YYYY HH:MM)"]}
SUMMARY:{items["a name"]}
LOCATION:{items["a location (optional)"]}
DESCRIPTION:{items["a description (optional)"]}
END:VEVENT
END:VCALENDAR
"""

if organizer_set:
    ics_splitted = ics.splitlines()
    ics_splitted.insert(5, f"ORGANIZER;CN={name}:MAILTO:{email}")
    ics = "\n".join(ics_splitted)

with open(f"{home_dir}/event.ics", "w") as file:
    file.write(ics)
    print(f"File saved to {home_dir}/event.ics")