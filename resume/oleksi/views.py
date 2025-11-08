from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    if request.method == "POST":
        context = request.POST.get('comment')
        Comment.objects.create(comment_text=context)  # <-- ОТУТ ТИ ДОДАЄШ В БАЗУ
        comments = Comment.objects.all().order_by('-created_at')
        return render(request, 'oleksi/home.html', {'comments': comments})  # щоб при F5 не дублювало

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'oleksi/home.html', {'comments': comments})

def project1(request):

    return render(request, 'oleksi/project1.html')
def project2(request):
    return render(request, 'oleksi/project2.html')
def project3(request):
    return render(request, 'oleksi/project3.html')
def future(request):
    return render(request, 'oleksi/future.html')