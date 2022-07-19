from django.urls import path
from .views import UserCreateView

urlpatterns = [
	path('signup/',UserCreateView.as_view(),name='signup'),
	]
