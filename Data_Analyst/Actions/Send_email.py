import os
import glob
import smtplib
import ssl
from email.message import EmailMessage

email_emisor ="fredfactory25@gmail.com"
email_receptor = "fredfactory25@gmail.com"
clave = "FrEDFactory.2025"

# Paso 1: Buscar todos los archivos que empiezan con 'reporte_' y terminan en .docx
archivos = glob.glob("reporte_*.docx")

# Paso 2: Si hay archivos, obtener el más reciente
if archivos:
    ultimo_archivo = max(archivos, key=os.path.getmtime)
    print(f"Último archivo detectado: {ultimo_archivo}")
    
    # Paso 3: Preparar correo
    asunto = "Último Reporte Automático de FrED"
    cuerpo = "Hola, te envío el último reporte generado automáticamente por el sistema."

    mensaje = EmailMessage()
    mensaje["From"] = email_emisor
    mensaje["To"] = email_receptor
    mensaje["Subject"] = asunto
    mensaje.set_content(cuerpo)

    # Paso 4: Adjuntar el archivo más reciente
    with open(ultimo_archivo, "rb") as f:
        contenido = f.read()
        mensaje.add_attachment(contenido, maintype="application", subtype="octet-stream", filename=os.path.basename(ultimo_archivo))

    # Paso 5: Enviar el correo
    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(email_emisor, clave)
        servidor.send_message(mensaje)

    print("📤 Correo enviado exitosamente con el archivo:", ultimo_archivo)

else:
    print("⚠️ No se encontró ningún archivo 'reporte_*.docx' para enviar.")