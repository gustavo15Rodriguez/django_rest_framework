from django.urls import path
from apps.snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', views.UserList.as_view()),
    path('detail/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
