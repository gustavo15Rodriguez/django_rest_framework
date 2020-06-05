from django.urls import path
from apps.snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', views.snippet_list),
    path('detail/<int:pk>', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
