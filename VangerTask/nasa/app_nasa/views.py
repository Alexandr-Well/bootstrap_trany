from django.shortcuts import render
from django.views.generic import FormView, TemplateView


class MainView(TemplateView):
    template_name = "main_page.html"
