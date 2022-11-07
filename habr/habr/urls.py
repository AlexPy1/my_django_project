from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from habr import settings
from habr_blog.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('habr_blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound