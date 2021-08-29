from django.http import request
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from blog_app.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.

# Contains all the blog of a particular user
class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = "blog_app/my_blogs.html"
    
# Class based views
# Function for creating a new blog
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_app/write_blog.html'
    fields = ("blog_title", "blog_content", "blog_image")

    def form_valid(self, form):
        # ID --- primary
        blog_obj = form.save(commit=False)
        blog_obj.user = self.request.user
        title = blog_obj.blog_title
        # Slug in the URL
        blog_obj.slug = title.replace(" ", "-")+"-" + str(uuid.uuid4())
        # print("Title : ", blog_obj.blog_title)
        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))

# All the blogs
class BlogList (ListView):
    context_object_name = "blogs"
    model = Blog
    template_name = "blog_app/blog_list.html"

# On login view the blog details
@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
            return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug': slug}))
    return render(request, 'blog_app/blog_details.html', context={'blog': blog})

# Class based views
# function for updating blogs
class UpdateBlogs(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = "blog_app/edit_blog.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_app:blog_details', kwargs={'slug': self.object.slug})



