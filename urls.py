from django.urls import path
from .views import PostDetailView, PostCreateView, convert

app_name = "txt2htm"

urlpatterns = [
    # path('', homeView.as_view(), name='home'),
    # path('',home_view),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/',PostCreateView.as_view(), name='create'),
]