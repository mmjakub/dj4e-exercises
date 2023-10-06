from django.urls import path

from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.AutoListView.as_view(), name='auto_list'),
    path('auto/create', views.AutoCreateView.as_view(), name='auto_create'),
    path('auto/update/<int:pk>', views.AutoUpdateView.as_view(), name='auto_update'),
    path('auto/delete/<int:pk>', views.AutoDeleteView.as_view(), name='auto_delete'),
    path('make/', views.MakeListView.as_view(), name='make_list'),
    path('make/create', views.MakeCreateView.as_view(), name='make_create'),
    path('make/update/<int:pk>', views.MakeUpdateView.as_view(), name='make_update'),
    path('make/delete/<int:pk>', views.MakeDeleteView.as_view(), name='make_delete'),
]
