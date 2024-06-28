from django.contrib import admin
from .models import Client, Page, Comment, Product, Review, Event, Booking, Order
from django.contrib.auth.models import User


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    '''Admin View for Page'''
    
    list_display = ['title', 'enabled', 'publish_date']
    list_filter = ['enabled', 'publish_date']
    inlines = [
        CommentInline,
    ]
    
    search_fields = ['title','sub_title']
    ordering = ['publish_date', 'title']
    class Media:
        js = ['assets/tinymce/tinymce.min.js', 'assets/js/scripts.admin.js']




class ReviewInline(admin.TabularInline):
    '''Stacked Inline View for Review'''
    model = Review
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ['title', 'price', 'clicks', 'post_date', 'enabled']
    list_filter = ['price', 'post_date', 'clicks']
    inlines = [
        ReviewInline,
    ]
    search_fields = ['title']
    ordering = ['clicks','post_date', 'price']
    class Media:
        js = ['assets/tinymce/tinymce.min.js', 'assets/js/scripts.admin.js']




class BookingInline(admin.TabularInline):
    '''Stacked Inline View for Booking'''
    model = Booking
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    '''Admin View for Event'''

    list_display = ['title', 'event_date']
    list_filter = ['title', 'event_date']
    inlines = [
        BookingInline,
    ]
    search_fields = ['title']
    ordering = ['event_date']
    class Media:
        js = ['assets/tinymce/tinymce.min.js', 'assets/js/scripts.admin.js']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'datetime', 'status', 'quantity']
    list_filter = ['product', 'status', 'datetime', 'quantity']
    search_fields = ['product']
    ordering = ['datetime', 'product', 'quantity']
    class Media:
        js = ['assets/tinymce/tinymce.min.js', 'assets/js/scripts.admin.js']



admin.site.register(Client)
