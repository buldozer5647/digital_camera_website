from django.views.generic import TemplateView
import random

class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        r = lambda: random.randint(0, 255)
        context["color"] = '#{:02X}{:02X}{:02X}'.format(r(), r(), r())
        return context
