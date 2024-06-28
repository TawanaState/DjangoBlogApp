from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.mylogin, name='login'),
    path('products/', views.shopview, name='shop'),
    path('products/<int:product_id>/', views.productview, name='product'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.eventview, name='event'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:page_name>/', views.pageview, name='page'),
]
