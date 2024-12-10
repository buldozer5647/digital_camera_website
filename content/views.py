# from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect

from .models import DigitalImage
from .forms import DigitalImageForm

import random

# class HomePage(CreateView):
#     form_class = DigitalImageForm
#     template_name = "home.html"
#     success_url = "homepage"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         r = lambda: random.randint(0, 255)
#         context["color"] = '#{:02X}{:02X}{:02X}'.format(r(), r(), r())

#         context["images_objects"] = DigitalImage.objects.order_by("date")

#         return context

def home_page(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = DigitalImageForm(request.POST, files=request.FILES)
            print(request.POST)
            print(request.FILES)
    
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            else:
                print("No1")
                print(form.errors)
        else:
            print("Not auth")

        return redirect("homepage")
    else:
        form = DigitalImageForm
        images_objects = DigitalImage.objects.order_by("date")
        r = lambda: random.randint(0, 255)
        color = '#{:02X}{:02X}{:02X}'.format(r(), r(), r())
    
    return render(request, "home.html", {
        "form": form,
        "images_objects": images_objects,
        "color": color,
    })

