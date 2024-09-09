


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

#TEST if string starts with https or http

Links = ['https://www.geeksforgeeks.org/python-regex-cheat-sheet/#basic',
         'https://www.vdot.virginia.gov/',
         'htts://github.com/Sankarsh100/Regex/pulls',
         ]

regex1 = 'https?'
for link in Links:
    if re.match(regex1,link):
        print(link)


