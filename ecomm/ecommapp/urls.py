from django.urls import path
from ecommapp import views  #application me create kia url 
from ecommapp.views import SimpleView
urlpatterns = [
    path('home',views.home),
    path('home2',views.home2),
    path('home3',views.home3),
    path('catfilter/<cv>',views.catfilter),
    path('registration',views.registration),
    path('cart',views.cart),
    path('login',views.login_user),
    path('logout',views.user_logout),
    path('po',views.place_order),
    path('pd',views.product_detail),
    path('about',views.about),           #empty ' ' in url nothing after /
    path('contact',views.contact),
    path('add/<a>/<b>',views.addition),
    path('myView',SimpleView.as_view()),#class based ka url .for call: classname.as_views()
]