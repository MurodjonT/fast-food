from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
	name_card = models.CharField(max_length = 250)
	description = models.TextField()
	price = models.CharField(max_length = 250)
	image = models.ImageField(upload_to ='image/')
	
#string obyektni qaytarad
	def __str__(self):
		return self.name_card

class Comment(models.Model):
	userName = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'{self.userName}'

#1-chi bosqich


class Order(models.Model):
	customer = models.ForeignKey(User, on_delete = models.SET_NULL, blank =True, null = True)
	data_ordered = models.DateTimeField(auto_now_add = True)
	name = models.CharField(max_length = 200, null = True)
	complete = models.BooleanField(default =  False, null = True, blank = False)



	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Products, on_delete = models.SET_NULL, blank = True, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
	quantity = models.IntegerField(default = 0, null = True, blank = True)
	date_added = models.DateTimeField(auto_now_add = True)
	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	def __str__(self):
		return str(self.id)







# Create your models here.
