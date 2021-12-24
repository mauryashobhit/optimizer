from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from portfolio import views

app_name="portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    path('optimize/',views.optimize,name='optimize'),
    url(r'^google/',views.google,name='google'),
    url(r'^facebook/',views.facebook,name='facebook'),
    url(r'^cisco/',views.cisco,name="cisco"),
    url(r'^apple/',views.apple,name='apple'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('user/',views.user,name="user"),
    path('user_apple/',views.user_apple,name="user_apple"),
    path('user_google/',views.user_google,name="user_google"),
    path('user_facebook/',views.user_facebook,name="user_facebook"),
    path('user_cisco/',views.user_cisco,name="user_cisco"),
    path('calculations/',views.calculate,name="calculate"),
    path('google_forecast/',views.forecast_google,name="forecast_google"),
    path('facebook_forecast/',views.forecast_facebook,name="forecast_facebook"),
    path('apple_forecast/',views.forecast_apple,name="forecast_apple"),
    path('cisco_forecast/',views.forecast_cisco,name="forecast_cisco"),
    path('news/',views.news,name="news"),
]
