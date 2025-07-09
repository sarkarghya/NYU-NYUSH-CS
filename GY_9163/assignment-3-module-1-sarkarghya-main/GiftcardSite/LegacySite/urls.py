from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('buy', views.buy_card_view, name="Buy Gift Card"),
    path('buy/', views.buy_card_view, name="Buy Gift Card"),
    path('buy/<int:prod_num>', views.buy_card_view, name="Buy Gift Card"),
    path('buy.html', views.buy_card_view, name="Buy Gift Card"),
    path('gift', views.gift_card_view, name="Gift a Card"),
    path('gift/', views.gift_card_view, name="Gift a Card"),
    path('gift/<int:prod_num>', views.gift_card_view, name="Gift a Card"),
    path('gift.html', views.gift_card_view, name="Gift a Card"),
    path('login', views.login_view, name="Login"),
    path('login/', views.login_view, name="Login"),
    path('login.html', views.login_view, name="Login"),
    path('register', views.register_view, name="Register"),
    path('register/', views.register_view, name="Register"),
    path('register.html', views.register_view, name="Register"),
    path('logout', views.logout_view, name="Logout"),
    path('logout/', views.logout_view, name="Logout"),
    path('logout.html', views.logout_view, name="Logout"),
    path('use', views.use_card_view, name="Use a card"),
    path('use.html', views.use_card_view, name="Use a card"),
    path('use/', views.use_card_view, name="Use a card"),
    path('metrics/', views.metrics_view, name="Prometheus Metrics"),
    path('metrics', views.metrics_view, name="Prometheus Metrics"),
    path('metrics.html', views.metrics_view, name="Prometheus Metrics"),
    
]
