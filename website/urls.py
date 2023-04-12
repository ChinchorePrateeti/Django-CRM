from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('record_delete/<int:pk>', views.customer_record_delete, name='record_delete'),
    path('record_add', views.customer_record_add, name='record_add'),
    path('record_update/<int:pk>', views.record_update, name='record_update'),

]
