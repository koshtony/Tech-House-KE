from django.shortcuts import render

# Create your views here.
def shop_view(request):
    
    return render(request,'ecommerce/shop.html')