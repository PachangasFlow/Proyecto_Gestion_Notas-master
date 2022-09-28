from email.message import EmailMessage
import smtplib


def enviar_email(email_destino,codigo):
    remitente ="franciscoossa@uninorte.edu.co"
    destinatario = email_destino
    mensaje= "Correo de activación"

    email=EmailMessage()
    email['From']= remitente
    email['To']= destinatario 
    email['Subject']='Coonfirmación de Correo'
    email.set_content("Bienvenido, Para Confirmar si Cuenta Ingrese el Siguiente Codigo. \ncodigo de verificación: <h2>"+codigo+"</h2>\n Recuerde ingresar este codigo para poder valisar si cuenta" )
    #email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "1015428448Ossa")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()