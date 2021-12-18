from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.welcomeView,name='smartTrain'),
    # path('accounts/',include('accounts.urls')),
    path('shunt_factor/',include('shunt_factor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('driver/' , include('driver.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
