from django.conf.urls import url

from user import views

urlpatterns={
    url("get_vcode/",views.get_vcode),
    url("login/",views.login)
}