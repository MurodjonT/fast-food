from django.shortcuts import render
from  django.views.generic import TemplateView, ListView, CreateView
from .models import Products, Comment, Order, OrderItem
from django.core.paginator import Paginator
import requests
from django.urls import reverse_lazy


class HomePageView(TemplateView):
	template_name = 'index.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'


class ProductCreateView(CreateView):
	model =	Products
	template_name = 'product_create.html'
	fields = '__all__'
	success_url = reverse_lazy('index')

# class BookPageView(TemplateView):
# 	template_name ='book.html'

# class MenuPageView(ListView):
# 	model = Products
# 	template_name = 'menu.html'
# 	context_object_name = 'mahsulotlar'

def menuPageView(request):
	if request.user.is_authenticated:
		customer = request.user
		print(request.user)
		order, created = Order.objects.get_or_create(customer = customer, complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items # savatdagi mahsulotlar soni
	else:
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']

	obj = Products.objects.all()
	page_n = request.GET.get('page', 1)
	p = Paginator(obj, 2)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {
    'page': page,
    'cartItems': cartItems
	}
	return render(request, 'menu.html', context)



def telegram_bot_sendtext(bot_message):
  bot_token ='5130152396:AAGiHy6qCBX9Yc8cxEyhsbn1Twzk_pdWL5E'
  bot_chatID ='1129151347'
  send_text ='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode =Markdown&text=' + bot_message 
  response =requests.get(send_text)
  return response.json()




def BookPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone',None)
		email = request.POST.get('email', None)
		message = request.POST.get('message', None)
		user = Comment.objects.create(
			userName = name,
			phone = phone,
			email = email,
			message = message
			)
		user.save()
		telegram_bot_sendtext(f"Ismi: {name} \nTelfon_raqami: {phone}\nTavsiyalari : {message}")


	return render(request = request, template_name = 'book.html')

