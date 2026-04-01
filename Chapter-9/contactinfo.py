import pyperclip
import re

phone_re = re.compile(r'''
    ^(\+91[\-\s]?|0)?  # Optional country code (+91) or leading 0
    [6-9]              # First digit of mobile number (6, 7, 8, or 9)
    \d{9}$             # Remaining 9 digits (total 10 digits)
''', re.VERBOSE)

email_re = re.compile(r'''
    ^[a-zA-Z0-9._%+-]+  # Local part (before @)
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # Domain name
    \.                   # .
    [a-zA-Z]{2,}$        # Min 2 chars
''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_number = '-'.join([group[1],group[3],group[5]])
    if groups[6] != '':
        phone_number += ' x' + group[6]
    matches.append(phone_number)
    for groups in email_re.findall(text):
        matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')