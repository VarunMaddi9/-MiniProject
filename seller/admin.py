from django.contrib import admin
from .models import bidding, seller

# Register your models here.
admin.site.register(seller)
admin.site.register(bidding)
