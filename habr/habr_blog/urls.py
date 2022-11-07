from django.urls import path
from .views import *

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
    path('users/', users, name='users'),
    path('users/<int:id>/', all_post_user, name='user_post'),
    path('users/my_post', user_post, name='my_post'),

]