#-*- coding: utf-8 -*-
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'