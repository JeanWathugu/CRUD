from django.shortcuts import render

from django.http import HttpResponse

from Jean.models import details


def home(request):
    return render(request, 'index.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = details(name=name, school=school, email=email)
        person.save()

        print(name, school, email)

    return render(request, 'index.html')

def people(request):
    d = details.objects.all()
    return render(request, 'people.html', { "data":d})
#or you could say after d , context= {'d' : d}...this gives people acccess to the data