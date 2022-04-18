#from pyexpat import model
#from unicodedata import name
#from urllib import response
from django.shortcuts import render
from django.views.generic import DetailView#, ListView
from .forms import ContactFormModelForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Post

from django.core.paginator import Paginator

# Create your views here.

def home(request):

    posts_list = Post.objects.order_by('-publish_date')

    p = Paginator(posts_list, 9)
    page = request.GET.get('page')
    posts = p.get_page(page)

    return render(request, 'home.html', {
            "object_list" : posts_list,
            "posts" : posts,
        })


''' Class based homepage view
class PostListView(ListView):
    model = Post
    template_name = 'home.html'

'''

class PostDetailView(DetailView):
    model = Post
    template_name = 'article.html'

def about(request):
    return render(request, 'about.html', {})

''' View without ModelForm

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            m = form.cleaned_data["message"]
            cc = form.cleaned_data["cc_myself"]

            recipients = ['jdlandau123@gmail.com']

            if cc:
                recipients.append(e)

            send_mail(subject = "No Subject", message=m, from_email=e, recipient_list=recipients)
            return HttpResponseRedirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form":form})
'''
def contact(request):

    if request.method == "POST":
        form = ContactFormModelForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            m = form.cleaned_data["message"]
            cc = form.cleaned_data["cc_myself"]

            recipients = ['jdlandau123@gmail.com']

            if cc:
                recipients.append(e)

            send_mail(subject = "No Subject", message=m, from_email=e, recipient_list=recipients)
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        form = ContactFormModelForm()

    return render(request, 'contact.html', {"form":form})


def thanks(request):
    return render(request,'thanks.html', {})

def search(request):
    if request.method == "POST":
        search_bar = request.POST['search-bar']

        search_results = Post.objects.filter(title__contains=search_bar)

        return render(request, 'search.html', {"search_bar" : search_bar,
        "search_results": search_results})

    else:
        return render(request, 'search.html', {})