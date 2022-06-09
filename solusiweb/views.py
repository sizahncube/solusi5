from django.shortcuts import render
from django.template import Template 
#from django.contrib.staticfiles import storage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def index(request):

    
    return render(request, "index.html")

def admin(request):

    return render(request, "admin.html")

def home(request):
    
    return render(request, "home.html")
    
def vice(request):
    
    return render(request, "vice.html")

def provice(request):
    
    return render(request, "provice.html")

def daf(request):
    
    return render(request, "daf.html")


def studentaff(request):
    
    return render(request, "studentaff.html")

def register(request):
    
    return render(request, "register.html")


def theol(request):
    
    return render(request, "theol.html")


def agric(request):
    
    return render(request, "agric.html")

def commerce(request):
    
    return render(request, "commerce.html")

def education(request):
    
    return render(request, "education.html")

def health(request):
    
    return render(request, "health.html")

def theology(request):
    
    return render(request, "theology.html")


def graduation(request):
    
    return render(request, "graduation.html")

def about(request):

    return render(request, "about.html")

##def contact(request):

   # return render(request, "contact.html")

def alumini(request):

    return render(request, "alumini.html")

def library(request):

    return render(request, "library.html")

def studentlib(request):

    return render(request, "studentlib.html")




def agribusiness(request):

    return render(request, "agribusiness.html")


def clothing(request):

    return render(request, "clothing.html")


def nursing(request):

    return render(request, "nursing.html")

def matnum(request):

    return render(request, "matnum.html")

def nutrition(request):

    return render(request, "nutrition.html")

def science(request):

    return render(request, "science.html")

    
def inAccounts(request):

    return render(request, "inAccounts.html")

def infosys(request):

    return render(request, "infosys.html")

def infinance(request):

    return render(request, "infinance.html")

def inmarketing(request):

    return render(request, "inmarketing.html")

def inmanagement(request):

    return render(request, "inmanagement.html")

def educat(request):

    return render(request, "educat.html")



def healt(request):

    return render(request, "healt.html")

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            #fone = form.cleaned_data['number']
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, message, from_email, ['buhlencube406@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact/')
    return render(request, "contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')
