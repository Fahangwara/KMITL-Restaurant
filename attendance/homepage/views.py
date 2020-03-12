from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from homepage.models import Faculty,Restaurant,Food,RestaurantFood

def homepage(request):

    search_txt = request.GET.get('inputSearch', '')

    restaurant_information = get_all_restaurant_information()

    faculty_all = get_all_faculty()

    if search_txt != '':
        restaurant_information = restaurant_information.filter(name__icontains = search_txt)

    context = {
        'restaurant_information': restaurant_information,
        'fac_all': faculty_all
    }

    return render(request, 'index.html', context)


def detail_page(request, restaurant_id):
    specified_restaurant_information = get_restaurant_information(restaurant_id)
    foodmenu = get_food_by_restaurant(restaurant_id)
    context = {
        'information' : specified_restaurant_information,
        'food_menu': foodmenu

    }
    return render(request, 'detail.html', context)

def get_all_restaurant_information():
    restaurant = Restaurant.objects.all()
    return restaurant

def get_restaurant_information(id):
     restaurant = Restaurant.objects.get(pk = id)
     return restaurant

def get_all_food():
    foodmenu = Food.objects.all()
    return foodmenu

def get_food(id):
    foodmenu = Food.objects.get(pk = id)
    return foodmenu

def get_all_restaurantfood():
    restaurantfood = RestaurantFood.objects.all()
    return restaurantfood

def get_restaurantfood(id):
    restaurantfood = RestaurantFood.objects.filter(restaurant_id = id)
    return restaurantfood

def get_food_by_restaurant(restaurant_id):
    restaurantfood = get_restaurantfood(restaurant_id)
    # restaurantfood = [{'price': 45, 'faadsf': 2332}, {}, {}, {}]
    foods = []
    for food_obj in restaurantfood:
        # food_obj = {'price': 45, 'faadsf':2332, 'food_id_id': 132}
        food = get_food(food_obj.food_id_id)        
        foods.append({
            'id': food_obj.food_id_id,
            'name': food.name,
            'price': food_obj.price,
        })

    return foods

def get_all_faculty():
    faculty = Faculty.objects.all()
    return faculty

def get_faculty(id):
    faculty = Faculty.objects.get(pk = id)
    return faculty

def restaurant_edit(request):
    return HttpResponse('Edit Restaurant Page.')
