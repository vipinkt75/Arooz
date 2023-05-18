from django.contrib import messages
from django.db.models import Q, Sum
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import (
    AdminNumber,
    Category,
    MainBanner,
    OrderDetails,
    Product,
    SubBanners1,
    SubBanners2,
    SubCategory,
)


def index(request):
    mainbanner = MainBanner.objects.last()
    subbanners1 = SubBanners1.objects.last()
    subbanners2 = SubBanners2.objects.last()
    topsave = Product.objects.filter(is_top_save_today=True)
    bestseller1 = Product.objects.filter(is_best_seller=True)[::-1]
    bestseller2 = Product.objects.filter(is_best_seller=True)[::-1]
    context = {
        "mainbanner": mainbanner,
        "subbanner1": subbanners1,
        "subbanner2": subbanners2,
        "topsave": topsave,
        "bestseller1": bestseller1,
        "bestseller2": bestseller2,
    }
    return render(request, "web/index.html", context)


def product(request, id):
    products = Product.objects.get(id=id)
    sub = products.subcategory
    percentage = ((products.price - products.offer_price) / products.price) * 100
    context = {"products": products, "subcategory": sub, "percentage": percentage}
    return render(request, "web/product-slider.html", context)


def shop(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(subcategory__category=category)
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "web/shop-left-sidebar.html", context)


def shop_category(request, id):
    subcategory = SubCategory.objects.filter(id=id)
    context = {"subcategory": subcategory}
    return render(request, "web/shop-category.html", context)


def shop_product(request, id):
    product = Product.objects.filter(id=id)
    context = {"product": product}
    return render(request, "web/shop-category-slider.html", context)


def search(request):
    kw = request.GET.get("search")
    if kw:
        if Product.objects.filter(
            Q(product__icontains=kw) or Q(description__icontains=kw)
        ):
            results = Product.objects.filter(
                Q(product__icontains=kw) | Q(description__icontains=kw)
            )
            context = {"results": results, "status": 1}
            return render(request, "web/search.html", context)
        else:
            messages.error(request, "No matching products found...")
            context = {"status": 0}
            return render(request, "web/search.html", context)
    else:
        return render(request, "web/search.html")


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def addtocart(request, id):
    id = id
    product = Product.objects.get(id=id)
    price = product.price
    if product:
        if OrderDetails.objects.filter(cart_id=_cart_id(request), product=product):
            messages.warning(request, "product is already in cart")
            return redirect("/product/" + str(id))
        else:
            OrderDetails.objects.create(
                cart_id=_cart_id(request), product=product, total=price
            )
            messages.warning(request, "Product added successfully")
            return redirect("/product/" + str(id))
    else:
        messages.error(request, "product is not available")
        return redirect("/product/" + str(id))


def viewcart(request):
    sub_total = OrderDetails.objects.filter(
        cart_id=request.session.session_key
    ).aggregate(Sum("total"))
    carted_item = OrderDetails.objects.filter(cart_id=request.session.session_key)
    context = {"carted_item": carted_item, "sub_total": sub_total}
    return render(request, "web/cart.html", context)


def deletefromcart(request, id):
    product = OrderDetails.objects.get(Cart_id=request.session.session_key, id=id)
    product.delete()
    messages.warning(request, "Product removed successfully...")
    return redirect("/cart")


@csrf_exempt
def whatsappFun(request, id):
    product = Product.objects.get(id=id)
    messagestring = ""
    name = request.POST.get("name")
    cus_number = request.POST.get("number")
    sleevelength = request.POST.get("sleevelength")
    chestaround = request.POST.get("chestaround")
    waistAround = request.POST.get("waistAround")
    Length = request.POST.get("Length")
    Hip = request.POST.get("Hip")
    Waist = request.POST.get("Waist")
    Thighs = request.POST.get("Thighs")
    Hem = request.POST.get("Hem")
    date = request.POST.get("eventdate")
    sizepant = request.POST.get("sizeoption")
    sizeshirt = request.POST.get("sizeoption")

    print("product.offer_price", product.offer_price)
    if product.offer_price:
        amount = int(product.rentalsecurity) + int(product.offer_price)
    else:
        amount = int(product.rentalsecurity) + int(product.price)
    data = list()
    number_obj = AdminNumber.objects.all().last()
    number = number_obj.phone_number
    try:
        messagestring = (
            "https://wa.me/+91"
            + number
            + "?text=Table Name :"
            + "Items"
            + "%0a------Order Details------"
        )
        data1 = {
            "name": product.product,
            "price": product.price,
            "rent_security": product.rentalsecurity,
            "amount": amount,
            "offer_price": product.offer_price,
        }
        data.append(data1)
        for i in data:
            print("rr")

            messagestring += (
                "%0aProduct-Name:"
                + str(i["name"])
                + "%0aPrice:"
                + str(i["price"])
                + "%0aRent-Security :"
                + str(i["rent_security"])
                + "%0a-----------------------------"
            )
            print("rr")
            print(str(i["offer_price"]))
            if str(i["offer_price"]):
                messagestring += "%0aOffer_price:" + str(i["offer_price"])
            messagestring += "%0aAmount-To-Pay :" + str(i["amount"])
        messagestring += (
            "%0a-----------------------------%0a\
                Grand Total :"
            + str(amount)
            + "%0a-----------------------------"
        )

        messagestring += "%0aShirt-Size:" + str(sizeshirt)
        messagestring += "%0aPant-Size:" + str(sizepant)
        messagestring += "%0a-----------------------------"
        messagestring += (
            "%0aSleeve-length:"
            + str(sleevelength)
            + "%0aChest-around:"
            + str(chestaround)
            + "%0aWaist-Around:"
            + str(waistAround)
            + "%0a-----------------------------"
        )
        messagestring += (
            "%0aLength-Pant:"
            + str(Length)
            + "%0aHip:"
            + str(Hip)
            + "%0aWaist-For-Trouser:"
            + str(Waist)
            + "%0aThighs:"
            + str(Thighs)
            + "%0aHem:"
            + str(Hem)
        )
        messagestring += "%0a-----------------------------%0a"
        messagestring += "%0a-----------------------------%0a"
        messagestring += "%0aEvent-Date:" + str(date)
        messagestring += "%0aCustomer-Name:" + str(name)
        messagestring += "%0aCustomer-Number:" + str(cus_number)

    except Exception:
        pass
    data = {
        "status": "success",
        "link": messagestring,
    }
    print("1")
    return render(request, "web/whatsappblank.html", data)


def checkout(request):
    return render(request, "web/checkout.html")


def about_us(request):
    context = {}
    return render(request, "web/about-us.html", context)


def blog_detail(request):
    context = {}
    return render(request, "web/blog-detail.html", context)


def blog_grid(request):
    context = {}
    return render(request, "web/blog-grid.html", context)


def blog_list(request):
    context = {}
    return render(request, "web/blog-list.html", context)


def coming_soon(request):
    context = {}
    return render(request, "web/coming-soon.html", context)


def compare(request):
    context = {}
    return render(request, "web/compare.html", context)


def contact_us(request):
    context = {}
    return render(request, "web/contact-us.html", context)


def order_success(request):
    context = {}
    return render(request, "web/order-success.html", context)


def order_tracking(request):
    context = {}
    return render(request, "web/order-tracking.html", context)


def otp(request):
    context = {}
    return render(request, "web/otp.html", context)
