import re

message = 'llamame 415-555-1011 mañana o a mi oficina 415-555-9999'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)
