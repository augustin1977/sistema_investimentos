from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario,Tipo
from django.shortcuts import redirect 
from hashlib import sha256
from usuarios.forms import *
from Financeiro import settings
import re
import string
import random
from django.http import Http404
from funcoes_basicas import *

def home(request):
    return render(request, "home.html", {'status':0})


