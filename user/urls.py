from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout", views.checkout, name="checkout"),
    path("product/<int:id>", views.product, name="product"),
    path("search", views.search, name="search"),
    path("shop-category/<int:id>", views.shop_category, name="shop_category"),
    path("shop/<int:id>", views.shop, name="shop"),
    path("whatsapp/<int:id>", views.whatsappFun, name="whatsapp"),
    path("cart/<int:id>", views.addtocart, name="addtocart"),
    path("cart", views.viewcart, name="viewcart"),
    path("deletefromcart/<int:id>", views.deletefromcart, name="deletefromcart"),
    path("about-us", views.about_us, name="about_us"),
    path("blog-detail", views.blog_detail, name="blog_detail"),
    path("blog-grid", views.blog_grid, name="blog_grid"),
    path("blog-list", views.blog_list, name="blog_list"),
    path("coming-soon", views.coming_soon, name="coming_soon"),
    path("compare", views.compare, name="compare"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("order-success", views.order_success, name="order_success"),
    path("order-tracking", views.order_tracking, name="order_tracking"),
    path("otp", views.otp, name="otp"),
]
