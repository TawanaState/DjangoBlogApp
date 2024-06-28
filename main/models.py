from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    def __str__(self):
        """Unicode representation of Order."""
        return self.user.username



class Page(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    image = models.TextField()
    views = models.IntegerField()
    short_name = models.CharField(max_length=50, primary_key=True)
    enabled = models.BooleanField(default=True)


class Comment(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=30)
    product_code = models.CharField(max_length=15, default="code")
    sub_title = models.CharField(max_length=100, default="sub title")
    price = models.CharField(max_length=40)
    stock = models.IntegerField()  # This is the number of the items available
    description = models.TextField()
    delivery = models.BooleanField(default=False)
    clicks = models.IntegerField(default=0)
    image = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
    def __str__(self):
        """Unicode representation of Order."""
        return self.title


class Review(models.Model):
    by = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)


class Event(models.Model):
    title = models.CharField(max_length=70)
    caption = models.CharField(max_length=100, default="...")
    event_date = models.DateField()
    description = models.TextField()
    front_image = models.TextField()

class Booking(models.Model):
    date_of_booking = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    information = models.TextField()


class Order(models.Model):
    """Model definition for Order."""
    STATUSES = (
        ('PENDING', 'Pending'),
        ('FINISHED', 'Finished'),
    )
    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUSES, default="PENDING")
    
    class Meta:
        """Meta definition for Order."""
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.product.product_code

