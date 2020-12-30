from django.contrib import admin

# Register your models here.
from .models import products, users, brands, main_banner, maincategories, subcategories, reviews, scatch_result

admin.site.register(products)
admin.site.register(users)
admin.site.register(brands)
admin.site.register(main_banner)
admin.site.register(maincategories)
admin.site.register(subcategories)
admin.site.register(reviews)
admin.site.register(scatch_result)

