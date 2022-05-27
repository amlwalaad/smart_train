from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.welcomeView,name='smartTrain'),
    path('profile/',views.profileview,name='profile'),
    # path('accounts/',include('accounts.urls')),
    path('empolyeeStation/',include('empolyeeStation.urls')),
    path('shunt_factor/',include('shunt_factor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('driver/' , include('driver.urls')),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
