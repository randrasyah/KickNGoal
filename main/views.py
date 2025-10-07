import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406403955',
        'name': request.user.username,
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price' : product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'stock' : product.stock,
            'brand' : product.brand,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price' : product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'stock' : product.stock,
            'brand' : product.brand,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    stock = request.POST.get("stock")
    brand = strip_tags(request.POST.get("brand"))
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        stock=stock,
        brand=brand,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        # Update product fields
        product.name = strip_tags(request.POST.get("name"))
        product.description = strip_tags(request.POST.get("description"))
        product.price = request.POST.get("price")
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.stock = request.POST.get("stock")
        product.brand = strip_tags(request.POST.get("brand"))
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()
        
        return HttpResponse(b"UPDATED", status=200)
    except Product.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)
    except Exception as e:
        return HttpResponse(b"ERROR", status=400)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        product.delete()
        return HttpResponse(b"DELETED", status=200)
    except Product.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)
    except Exception as e:
        return HttpResponse(b"ERROR", status=400)

@csrf_exempt
@require_POST
def login_user_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not username or not password:
        return JsonResponse({
            'success': False,
            'message': 'Username and password are required'
        }, status=400)
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return JsonResponse({
            'success': True,
            'message': 'Login successful',
            'redirect_url': reverse('main:show_main')
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Invalid username or password'
        }, status=401)

@csrf_exempt  
@require_POST
def register_user_ajax(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1') 
    password2 = request.POST.get('password2')
    
    if not username or not password1 or not password2:
        return JsonResponse({
            'success': False,
            'message': 'All fields are required'
        }, status=400)
    
    if password1 != password2:
        return JsonResponse({
            'success': False, 
            'message': 'Passwords do not match'
        }, status=400)
    
    if len(password1) < 8:
        return JsonResponse({
            'success': False,
            'message': 'Password must be at least 8 characters long'
        }, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'success': False,
            'message': 'Username already exists'
        }, status=400)
    
    try:
        user = User.objects.create_user(username=username, password=password1)
        return JsonResponse({
            'success': True,
            'message': 'Account created successfully! Please log in.',
            'redirect_url': reverse('main:login')
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Failed to create account. Please try again.'
        }, status=500)

@csrf_exempt
@require_POST
def logout_user_ajax(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({
            'success': True,
            'message': 'You have been logged out successfully',
            'redirect_url': reverse('main:login')
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'User not authenticated'
        }, status=400)