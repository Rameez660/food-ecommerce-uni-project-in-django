from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	
	path('aboutus', views.aboutus, name="aboutus"),
	path('contactus', views.contactus, name="contactus"),
	
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path("viewdetail/<str:myid>",views.viewdetail,name="viewdetail"),
]