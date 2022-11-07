from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, request, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth.models import User
from .utils import *

def users(request):
   return render(request,'habr_blog/users.html',{'users': User.objects.all()})

def user_post(request):
    if request.user.is_authenticated:
        current_user = request.user
        post = Post.objects.filter(username_id=current_user.id)
        return render(request, 'habr_blog/us_post.html', {'us_post': post})
    else:
        reverse_lazy('home')

def all_post_user(request, id):
    post = Post.objects.filter(username_id=id)
    return render(request, 'habr_blog/all_post_user.html', {'us_post': post})






class PostHome(DataMixin, ListView):
    model = Post
    template_name = 'habr_blog/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('cat')


def about(request):
    return render(request, 'habr_blog/about.html', {'menu': menu, 'title': 'О сайте'})


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'habr_blog/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'habr_blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'habr_blog/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(titel='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'habr_blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'habr_blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'habr_blog/addpage.html'
    # success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


