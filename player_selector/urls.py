from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('vote/', views.vote, name='vote'),
    path('new-besthomo/', views.new_besthomo_view, name='new_besthomo'),
    path('new-besthomo2/', views.new_besthomo_view2, name='new_besthomo2'),
    path('vote-success/', views.vote_success_view, name='vote_success'),
    path('fetch-votes/', views.fetch_votes, name='fetch_votes'),
]
