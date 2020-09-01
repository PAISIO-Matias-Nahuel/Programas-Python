import smtplib

##establecer la conexion con el server y el port
conn = smtplib.SMTP('smtp.gmail.com', '587')
type(conn)
conn.ehlo()
conn.starttls()

##inicio de secion
conn.login('mailejemplo@gmail.com','contraseña')

##enviar mail
conn.sendmail('maildesalida','maildeentrada','texto del mail')

##terminar conexion
conn.quit()
