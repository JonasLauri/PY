#! /usr/bin/env/python3
import re, pyperclip

# Regex for phone numbers
phoneRegex = re.compile(r'''
# 000-000-0000, 000-0000, (000) 000-0000, 000-000-HELP[0000], 000-0000 ext 12345, ext. 12345, x12345,
(
((\d\d\d)|(\(\d\d\d\)))?    # first code (optional)
(\s|-)    # separator
\d\d\d    # 3-digits
-    # separator
(\d\d\d\d)|(\w+\[\d+\])    # last digits
(((ext(\.)?\s)|x)    # words extensions
(\d{2,5}))?    # digits extensions
)
''', re.VERBOSE)

# Regex for emails
emailRegex = re.compile('''
[a-zA-Z0-9_.+]+    # name part
@    # @
[a-zA-Z0-9_.+]+    # domain name
''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()
    
# Extract email and phone from text 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
