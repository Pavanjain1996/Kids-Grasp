from django.shortcuts import render

def index(request):
    return render(request,"KidsGrasp/Home.html")

def english(request):
    return render(request,"KidsGrasp/English.html")

def hindi(request):
    return render(request,"KidsGrasp/Hindi.html")

def maths(request):
    return render(request,"KidsGrasp/Maths.html")

def calculator(request):
    return render(request,"KidsGrasp/Calculator.html")
