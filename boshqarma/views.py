from django.shortcuts import render, redirect
from .models import News, QuyiTashkilotlar
from .forms import SendForm


def index(request):
    form = SendForm()
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'index.html', context)


def news(request):
    news = News.objects.filter().order_by('-id')
    context = {'news': news}
    
    return render(request, 'news.html', context)

def hujjatlar(request):
    context = {}
    return render(request, 'hujjat.html', context)

def quyi_tashkilotlar(request):
    branches = QuyiTashkilotlar.objects.all()
    context = {'branches':branches}
    return render(request, 'quyi_tashkilotlar.html', context)

def qabul(request):

    context = {}
    return render(request, 'qabul.html', context)

