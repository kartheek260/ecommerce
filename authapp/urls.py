from django.urls import path
from . import views
app_name='authapp'

urlpatterns = [
path('signup/', views.signup),
path('login/',views.login),
path('signup/otpvalidation',views.otpvalidation),
path('my_logout/',views.my_logout),

]
