from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/about-us', views.about_us, name='about-us'),
    path('careers', views.careers, name='careers'),
    path('stories', views.stories, name='stories'),
    path('help/return-policy', views.return_policy, name='return-policy'),
    path('help/terms-of-use', views.terms_of_use, name='terms-of-use'),
    path('help/privacy', views.privacy, name='privacy')
]