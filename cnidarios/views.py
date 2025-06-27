from django.shortcuts import render
import subprocess
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"cnidarios/index.html")



def grafico_view(request):
    subprocess.run(["python3", "cnidarios/grafico_cnidario.py"])

    return render(request, "cnidarios/grafico.html")
