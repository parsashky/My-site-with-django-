from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from website.forms import contactform , NameForm , newsletterform
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket did not submited')
    form = contactform()
    return render(request,'website/contact.html',{'form':form})
def newsletter_view(request):
    if request.method == 'POST':
        form = newsletterform(request.POST)
        if form.is_valid():
                form.save()
                HttpResponseRedirect('/')
    else :
        HttpResponseRedirect('/')
def test_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
        else:
            return HttpResponse("not valied")
    form = contactform()
    return render(request,'website/test.html',{"form":form})