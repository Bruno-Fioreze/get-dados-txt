from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Arquivo

# Create your views here.

def index(request):
    if (request.method == "POST"):
        array_extensao = ['txt']
        array_conteudo = []
        header = ["comprador","descricao","precounitario","quantidade","endereco","fornecedor"]
        dict = {}
        for file in request.FILES.getlist('file'):
            if(get_ext(file.name) in array_extensao ):
                filename = save_archive(file)
                f = open("media/"+filename, encoding='utf-8', errors='ignore')
                lines = f.readlines()
                lines.pop(0)

                for line in lines:
                    array_line_temp = line.split("\t")
                    array_conteudo.append({
                        "descricao":array_line_temp[0],
                        "comprador":array_line_temp[1],
                        "precounitario":converte(array_line_temp[2],"float"),
                        "quantidade":converte(array_line_temp[3],"int"),
                        "endereco":array_line_temp[4],"fornecedor":array_line_temp[5]
                    })
                for line in array_conteudo:
                    arquivo = Arquivo()
                    arquivo.descricao = str(line["descricao"])
                    arquivo.comprador = str(line["comprador"])
                    arquivo.precounitario = line["precounitario"]
                    arquivo.quantidade = line["quantidade"]
                    arquivo.endereco = str(line["endereco"])
                    arquivo.fornecedor = str(line["fornecedor"])
                    arquivo.save()

    if(request.method == "GET"):
        return render(request,"core/index.html")

def get_ext(nome):
    array = nome.split(".")
    indice = len(array) - 1
    return array[indice]

def save_archive(file):
    fs = FileSystemStorage(location='./media/')
    filename = fs.save(file.name, file)
    return filename

def converte(valor,tipo):
    if(tipo.lower() == "float"):
        if(valor != None and valor != ''):
            return float(valor)
    if (tipo.lower() == "int"):
        if (valor != None and valor != ''):
            return int(valor)


