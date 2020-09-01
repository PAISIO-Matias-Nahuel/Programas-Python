import imapclient #realiza la conexion a la bandeja de entrada 
import pyzmail #extrae el texto en string del mail

##conexion al servidor del proveedor
conn = imapclient.IMAPClient('imap.gmail', ssl = True)
conn.login('mail','contraseña')

##seleccionar la bandeja
conn.select_folder('carpeta', readonly = True)

##buscar los mails en la bandeja y la informacion que posee
UIDs = conn.search(['SINCE 20-Aug-2015'])
rawMessage = conn.fetch([,['BODY[]','FLAG[]'])

##extrae el mensaje del mail seleccionado
message = pyzmail.PyzMessage.factory(rawMesagge[key,[b'BODY']])
message.get_subject()
message.get_addresses('from')
message.get_adressses('to')
message.get_adresses('bbc')

message.text_part
message.html_part
message.text_part.get_payload().decode('UTF-8')
message.text_part.charset

##ejemplo de editar una bandeja
conn.lis_folders()
conn.select_folder('INBOX', readonly = False)
UIDs = conn.search(['ON 24-Aug-2015'])
UIDs
conn.delete_messages(UIDs)
