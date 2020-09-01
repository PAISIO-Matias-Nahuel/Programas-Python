#! python3

import re, pyperclip

#crear un regex para numeros
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345. ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?      #area code (optional)
(\s|-)                      #first separator
\d\d\d                      #first 3 digits
-                           #separator
\d\d\d\d                    #last 4 digits
(((ext(\.)?\s)|x)           #extension (optional)
 (\d{2,5}))?                #extension word-part(optional)
)
''', re.VERBOSE)

#TODO: crear un regex para mails
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+         #name part
@                       #@ symbol
[a-zA-Z0-9_.+]+         #domain part

''', re.VERBOSE)
#TODO: obtener el texto del clipboard
text = pyperclip.paste()
#TODO: extraer los numeros
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumber =[]
for phoneNumber in extractedPhone:
    allPhoneNumber.append(phoneNumber[0])

#TODO: copiar los numeros y mail al clipboard
results = '\n'.join(allPhoneNumber) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
