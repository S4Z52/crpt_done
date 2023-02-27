from django.contrib import admin
from django.urls import path,include
from users_auth import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('admin/', admin.site.urls),
path('accounts/', include('django.contrib.auth.urls')),
path('home/', include('users_auth.urls')),
path('', include('users_auth.urls'), name='upld'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)