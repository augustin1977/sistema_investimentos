import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from usuarios.models import *
from django.shortcuts import render,redirect
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

def enviar_email(subject,body,recipients):
        html_message = MIMEText(body, 'html')
        html_message['Subject'] = subject
        html_message['From'] = settings.EMAIL_HOST_USER
        html_message['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD_APP)
            server.sendmail(settings.EMAIL_HOST_USER, recipients, html_message.as_string())   
                    

def is_user(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            usuario = request.session.get('usuario')
        except:
            usuario=False
        if usuario:
            user= Usuario.objects.get(id=usuario)
            tipouser=Tipo.objects.get(tipo="user")
            tipoadmin=Tipo.objects.get(tipo="admin")
            if user.ativo==1 and (user.tipo==tipouser or user.tipo==tipoadmin):
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        else:
            return redirect('login')  # Redireciona para uma página de login ou qualquer outra página apropriada
    return wrapper
def is_admin(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            usuario = request.session.get('usuario')
        except:
            usuario=False
        if usuario:
            user= Usuario.objects.get(id=usuario)
            tipo=Tipo.objects.get(tipo="admin")
            if user.ativo and user.tipo==tipo:
                return view_func(request, *args, **kwargs)
            else: 
                return redirect("/login?status=99")
        else:
            return redirect("/login?status=99")  # Redireciona para uma página de login ou qualquer outra página apropriada
    return wrapper
           
