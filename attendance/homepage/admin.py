from django.contrib import admin
from homepage.models import Faculty,Restaurant,Food,RestaurantFood

# Register your models here.
admin.site.register(Restaurant)
class PriceInline(admin.TabularInline):
    model = RestaurantFood
    extra = 0

class FoodAdmin(admin.ModelAdmin):
    inlines = [PriceInline]


admin.site.register(Faculty)
class PriceInline(admin.TabularInline):
    model = RestaurantFood
    extra = 0

class FoodAdmin(admin.ModelAdmin):
    inlines = [PriceInline]


admin.site.register(RestaurantFood)
class PriceInline(admin.TabularInline):
    model = RestaurantFood
    extra = 0

class FoodAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

    
admin.site.register(Food, FoodAdmin)
class PriceInline(admin.TabularInline):
    model = RestaurantFood
    extra = 0

class FoodAdmin(admin.ModelAdmin):
    inlines = [PriceInline]

