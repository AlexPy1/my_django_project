from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото', )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время созданиия')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    global_url = models.CharField(max_length=255, verbose_name='global_url', default='url')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']





# class CustomUser(AbstractBaseUser):
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('user', kwargs={'user_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         ordering = ['username']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


# class CustomUser(AbstractBaseUser):
#     username_validator = ASCIIUsernameValidator()
#
#     username = models.CharField(max_length=150, unique=True,
#                                 help_text=("Требуется не более 150 символов. Только буквы и цифры ASCII."),
#                                 validators=[username_validator],
#                                 error_messages={"unique": ("Пользователь с таким именем существует"), })
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='user_url')
#     first_name = models.CharField("Фамилия", max_length=150, blank=True)
#     last_name = models.CharField("Имя", max_length=150, blank=True)
#     age = models.PositiveIntegerField(blank=True, null=True)
#     email = models.EmailField(verbose_name='Email')
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('users', kwargs={'user_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         ordering = ['name']
