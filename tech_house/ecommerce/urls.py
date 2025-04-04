from django.urls import path
from . import views
from .views import shop_view,shop_details_view,shop_add_to_cart_view,shop_plus_to_cart,\
    shop_minus_to_cart_view,shop_cart_view,shop_rem_cart_view,filter_products_by_brand,\
    filter_by_sub_category,filter_by_price_range,search_products,sort_products,\
        create_product_review,edit_product_review,delete_product_review,shop_checkout_details,\
            shop_pesapal_payment_post,shop_pesapal_response_page,shop_get_pesapal_ipn_id

urlpatterns = [
    
             path('',views.shop_view,name='eco-shop'),
             path('shop-details/<int:pk>/',views.shop_details_view,name="eco-shop-details"),
             path('add-to-cart/<int:pk>/', views.shop_add_to_cart_view, name="eco-shop-add-to-cart"),
             path('plus-to-cart/<int:pk>/', views.shop_plus_to_cart, name="eco-shop-plus-to-cart"),
             path('minus-to-cart/<int:pk>/', views.shop_minus_to_cart_view, name="eco-shop-minus-to-cart"),
             path('cart/', views.shop_cart_view, name="eco-shop-cart"),
             path('remove-from-cart/<int:pk>/', views.shop_rem_cart_view, name="eco-shop-remove-cart"),
             path('filter-products-by-brand/<int:brand_id>/', views.filter_products_by_brand, name="eco-shop-filter-by-brand"),
             path('filter-products-by-sub-category/<int:sub_category_id>/', views.filter_by_sub_category, name="eco-shop-filter-by-sub-category"),
             path('filter-products-by-price-range/', views.filter_by_price_range, name="eco-shop-filter-by-price-range"),
             path('sort-products', views.sort_products, name="eco-shop-sort-products"),
             path('search-products/', views.search_products, name="eco-shop-search-products"),
             path('create-review/', create_product_review, name="eco-create-review"),
             path('edit-review/', edit_product_review, name="eco-edit-review"),
             path('delete-review/', delete_product_review, name="eco-delete-review"),
             path('checkout_details/',shop_checkout_details,name="eco-shop-checkout-details"),
             
             # PESAPAL LINKS
             path('pesapa-payment-post/',shop_pesapal_payment_post,name="eco-pesapal-payment-post"),

             path('response-page/', shop_pesapal_response_page, name="eco-pesapal-response-page"),
             path('ipn/',shop_get_pesapal_ipn_id,name="eco-pesapal-ipn-id"),	
             
]

