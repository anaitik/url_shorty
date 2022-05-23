from django.contrib import admin
from django.urls import path
from authentication.views import loginPage, signup, logout, passwordChange
from URLHandler.views import dashboard, generate, home, deleteurl
from home_shorty.views import short_generate,home_shortener
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('loginPage/', loginPage, name="loginPage"),
    path('logout/', logout, name="logout"),
    path('passwordChange/', passwordChange, name="passwordChange"),
    path('dashboard/', dashboard, name="dashboard"),
    path('url_shorten/',home_shortener,name="home_shortener"),
    path('generate/', generate, name="generate"),
    path('shorten/',short_generate,name="shorten"),
    path('deleteurl/', deleteurl, name="deleteurl"),
    path('<str:query>/', home, name="home"),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('api/',include('api.urls')),
]
