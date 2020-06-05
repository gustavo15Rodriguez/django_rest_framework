from django.urls import path
from apps.snippets import views

urlpatterns = [
    path('list/', views.snippet_list),
    path('detail/<int:pk>', views.snippet_detail)
]
