def isPhoneNumber(text):
    if len(text) != 12:
        return False # no numero de telefono
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no codigo de area
    if text[3] != '-':
        return False # guion faltante
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False #no primeros 3 digitos
    if text[7] != '-':
        return False #segun guion faltante
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False # 4 digitos faltantes
    return True

message = 'llamame a 415-555-1011 mañana o 415-55-9999 en mi oficina'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('numero de telefono encontrado: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('no se pudo encontrar ningun numero de telefono')
    
    
      
        
