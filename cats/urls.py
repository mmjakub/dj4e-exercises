from django.urls import path

from cats import views as v

app_name = 'cats'
urlpatterns = [
    path('', v.CatListView.as_view(),  name='index'),
]
