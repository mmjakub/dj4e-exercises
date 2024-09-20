from django.urls import path

from cats import views as v

app_name = 'cats'
urlpatterns = [
    path('', v.CatListView.as_view(),  name='index'),
    path('main/create', v.CatCreateView.as_view(), name='cat_create'),
    path('main/<int:pk>/update', v.CatUpdateView.as_view(), name='cat_update'),
    path('main/<int:pk>/delete', v.CatDeleteView.as_view(), name='cat_delete'),
    path('lookup/', v.BreedListView.as_view(), name='breed_list'),
    path('lookup/create/', v.BreedCreateView.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update', v.BreedUpdateView.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete', v.BreedDeleteView.as_view(), name='breed_delete'),
]
