from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 25, null = True)
	phone = models.CharField(max_length = 25, null = True)
	email = models.EmailField()
	date_created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 25, null = True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATAGORY = (
		('Indoor', 'Indoor'),
		('Outdoor', 'Outdoor')
	)
	name = models.CharField(max_length = 255, null = True)
	price = models.FloatField()
	catagory = models.CharField(max_length = 255, choices = CATAGORY)
	description = models.TextField(null = True)
	date_created = models.DateTimeField(auto_now_add = True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for Delivery', 'Out for Delivery'),
		('Delivered', 'Delivered')
	)
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE, null = True)
	product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
	date_created = models.DateTimeField(auto_now_add = True)
	status = models.CharField(max_length = 255, choices = STATUS)

	def __str__(self):
		return f"{self.customer} -- {self.product}"