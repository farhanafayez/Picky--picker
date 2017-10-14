from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from django.views.generic import TemplateView

import random

# Create your views here.
#
# def old_home(request):
#     html_var = 'f strings'
#     num = random.randint(0, 10000000)
#     html_ = f"""<!DOCTYPE HTML>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Hello Fellas</h1>
#     <p>here comes{ html_var }</p>
#     <p>here comes{ num }</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)

def home(request):
    num = 0
    some_list = [
        random.randint(0,10000000),
        random.randint(0,10000000),
        random.randint(0,10000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0,10000000)
    context = {'num': num,
               'some_list': some_list
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "home.html", context)

def about(request):
  
    context = {
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "about.html", context)

def contact(request):
    
    context = {
    }
    # return render(request, "base.html", {html_var:True, 'num':num})
    return render(request, "contact.html", context)


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
   
#         return render(request, "contact.html", context)

    # def put(self, request, *args, **kwargs):
    #     context = {}
   
    #     return render(request, "contact.html", context)

    # def post(self, request, *args, **kwargs):
    #     context = {}
   
    #     return render(request, "contact.html", context)

class ContactView(TemplateView):
   
    template_name = "contact.html"





















