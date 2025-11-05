from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'finXD.html')


def pagina2 (request):
           return render(request,'pag2.html')


def pagina1 (request):
    return render(request,'pag1.html')
    

def main (request):
    return render(request, 'iniciar.html')


