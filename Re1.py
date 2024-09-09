
import re

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# Find people with first and last name only
regex = r'^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)

#Search for word charactr starting with C
Type1= 'C\w*'
for name in names:
    match = re.search(Type1, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
        print(match.span())
