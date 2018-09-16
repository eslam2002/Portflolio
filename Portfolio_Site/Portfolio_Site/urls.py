
from django.contrib import admin
from django.urls import path,include
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.portfolio_home,name='home'),
    # path('email/',views.MassegeCreateView.as_view(),name='email'),

]
