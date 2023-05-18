from django.contrib import admin
from user.models import (
    AdminNumber,
    AvailableSizesPant,
    AvailableSizesShirt,
    Category,
    HeaderFlash,
    MainBanner,
    OrderDetails,
    Product,
    SubBanners1,
    SubBanners2,
    SubCategory,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(MainBanner)
admin.site.register(SubBanners1)
admin.site.register(SubBanners2)
admin.site.register(HeaderFlash)
admin.site.register(AdminNumber)
# custome measurements
admin.site.register(AvailableSizesShirt)
admin.site.register(AvailableSizesPant)
admin.site.register(OrderDetails)
