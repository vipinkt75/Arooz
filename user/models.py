from django.db import models
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField


class AdminNumber(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)


class Category(models.Model):
    category = models.CharField(max_length=200, unique=True, null=True, blank=True)
    image = VersatileImageField(upload_to="categories/", null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("user:shop", kwargs={"id": self.id})

    def get_subcategories(self):
        return SubCategory.objects.filter(category=self)

    def get_product(self):
        return Product.objects.filter(category=self)

    def __str__(self):
        return str(self.category)


class SubCategory(models.Model):
    subcategory = models.CharField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse_lazy("user:product", kwargs={"id": self.id})

    def get_shop_url(self):
        return reverse_lazy("user:shop", kwargs={"id": self.id})

    def get_products(self):
        return Product.objects.filter(subcategory=self)

    def __str__(self):
        return str(self.subcategory)


class Product(models.Model):
    # user=models.ForeignKey(Login, on_delete=models.CASCADE, null=True,default='')
    product = models.CharField(max_length=150)
    image = VersatileImageField(upload_to="products/", null=True, blank=True)
    sub_image1 = VersatileImageField(upload_to="products/", null=True, blank=True)
    sub_image2 = VersatileImageField(upload_to="products/", null=True, blank=True)
    sub_image3 = VersatileImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.IntegerField(null=True, blank=True)
    offer_price = models.IntegerField(null=True, blank=True)
    rentalsecurity = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    is_top_save_today = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    measurements_needed = models.BooleanField(default=False)

    def get_sizesshirt(self):
        return AvailableSizesShirt.objects.filter(product=self)

    def get_sizespant(self):
        return AvailableSizesPant.objects.filter(product=self)

    def __str__(self):
        return self.product


class MainBanner(models.Model):
    bannerbig = VersatileImageField(upload_to="MainBanner/", null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )


class SubBanners1(models.Model):
    subbanner1 = VersatileImageField(upload_to="SubBanners/", null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )


class SubBanners2(models.Model):
    subbanner2 = VersatileImageField(upload_to="SubBanners/", null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )


class HeaderFlash(models.Model):
    address = models.CharField(max_length=250, null=True, blank=True)
    # offer_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address


class AvailableSizesShirt(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    size_shirt = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.size_shirt


class AvailableSizesPant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    size_pant = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.size_pant


class OrderDetails(models.Model):
    cart_id = models.CharField(max_length=200, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    sleevelength = models.CharField(max_length=150, null=True, default=0)
    chestaround = models.CharField(max_length=150, null=True, default=0)
    waistAround = models.CharField(max_length=150, null=True, default=0)
    LengthTrouser = models.CharField(max_length=150, null=True, default=0)
    hip = models.CharField(max_length=150, null=True, default=0)
    WaistForTrouser = models.CharField(max_length=150, null=True, default=0)
    thighs = models.CharField(max_length=150, null=True, default=0)
    hem = models.CharField(max_length=150, null=True, default=0)
    size = models.CharField(max_length=3, null=True, blank=True, default=0)
    date = models.DateField(null=True)
    total = models.FloatField(max_length=150, null=True, default=0)
