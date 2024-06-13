# A Python script for creating ICS (e-calendar events) files

import os

if organizer.txt not in os.listdir:
    inp = input("An organizer info is not set, do you want to set it up now? [Y/n]")

    if inp.lower() in ["y", "yes", "n", "no", ""]:

        if "y" in inp.lower() or inp == "":
            name = input("Insert your full name: ")
            email = input("Insert your e-mail address: ")
            organizer = name + "\n" + email
            with open("organizer.txt", "w") as file:
                file.write(organizer.txt)


    else:
        print("Interrupted")
        exit(1)


items = {"a name":"", "a beginning (hh-mm-dd-mm-yyyy)":"", "an end (hh-mm-dd-mm-yyyy)":"", "a description (optional)":""}

for item in items:
    if "optional" not in item:
        num_iterrations = 0
        
        while items[item] == "":
            
            if num_iterrations > 0:
                print("Error: invalid value")
            
            value = input(f"Insert {item} of an event: ")
            items[item] = value
            num_iterrations += 1
    else:
        value = input(f"Insert {item} of an event: ")
        items[item] = value

ics = f"""
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
ORGANIZER;CN=John Doe:MAILTO:john.doe@example.com
DTSTART:19970714T170000Z
DTEND:19970715T040000Z
SUMMARY:Bastille Day Party
GEO:48.85299;2.36885
END:VEVENT
END:VCALENDAR
"""