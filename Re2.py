


import re


names = ['Brian Daugette',
'Veronica Supersonica',
'Tony Gasparovic',
'Patrick Germann',
'm!sha']


# Test for first name and last name

regex = '^\w+\s+\w+$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)

