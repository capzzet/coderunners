from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import ContactForm
from .models import yldam_news


# Create your views here.
def index(request):
    posts = yldam_news.objects.all()
    features = [
        {'title': 'Ваши мечты - наша работа', 'icon': 'fa fa-pencil',
         'description': 'Мы работаем над безопасными и удобными дорогами.', 'link': '#section2'},
        {'title': 'Для нас значим каждый', 'icon': 'fa fa-graduation-cap',
         'description': 'Характер нашей работы учитывает мнение каждого.', 'link': '#section3'},
        {'title': 'Оперативное оказание услуг', 'icon': 'fa fa-book',
         'description': 'Обширный штат сотрудников оперативно решит проблему.', 'link': '#section4'},
    ]
    return render(request,'yldam/index.html',{'title':'doolat','posts':posts,'features': features})

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Дополнительные действия после получения данных формы
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
def PageNotFound(request,exception):
    return HttpResponseNotFound("404")