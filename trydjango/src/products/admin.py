from django.contrib import admin
from .models import Product # THis is a relative import since it is in the same diretory
# Register your models here.

admin.site.register(Product)