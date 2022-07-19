from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('',HomePageView.as_view(), name = 'index'),
	path('about/',AboutPageView.as_view(), name = 'about'),
	path('book/',BookPageView, name = 'book'),
	path('menu/', views.menuPageView, name = 'menu'),
	path('product_create/', ProductCreateView.as_view(), name = 'product_create'),
	


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)