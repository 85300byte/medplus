from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('about/', views.about_view, name='about'),
    path('products/', views.product, name='product'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('search/', views.search_products, name='search_products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('remove-cart-item/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders_view, name='orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('create-razorpay-order/', views.create_razorpay_order, name='create_razorpay_order'),
    path('process-cod-order/', views.process_cod_order, name='process_cod_order'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation_view, name='order_confirmation'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('update-profile-image/', views.update_profile_image, name='update_profile_image'),
    path('add-address/', views.add_address, name='add_address'),
    path('update-address/<int:address_id>/', views.update_address, name='update_address'),
    path('delete-address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('shop/<int:product_id>/', views.shop_view, name='shop_detail'),
    path('address/add/', views.add_address, name='add_address'),
    path('address/<int:address_id>/', views.get_address, name='get_address'),
    path('address/<int:address_id>/update/', views.update_address, name='update_address'),
    path('address/<int:address_id>/delete/', views.delete_address, name='delete_address'),
    path('address/<int:address_id>/set-default/', views.set_default_address, name='set_default_address'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('contact/', views.contact_view, name='contact'),
    path('check-auth/', views.check_auth, name='check_auth'),
    path('checkout/buy-now/', views.buy_now_checkout, name='buy_now_checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
