import django.shortcuts
from django.views.generic import ListView, DetailView
from .models import Posts


# Create your views

class HomePageView(ListView):
    model = Posts
    template_name = "home.html"
    context_object_name = "all_post_list"


class DetailPageView(DetailView):
    model = Posts
    template_name = "detail.html"
    context_object_name = "single_post"
