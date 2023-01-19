from django.contrib import admin
from .models import Product, Review
from django.utils import timezone


class ReviewInline(admin.TabularInline):
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock",
                    "added_days_ago", "update_date")
    list_editable = ("is_in_stock", )
    # list_display_links = ("create_date", ) #can't add items in list_editable to here
    ordering = ("name",)
    search_fields = ("name",)
    # prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    list_per_page = 25
    inlines = (ReviewInline,)
    # date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock")

    fieldsets = (
        (None, {
            "fields": (
                # to display multiple fields on the same line, wrap those fields in their own tuple
                ('name', 'slug'), "is_in_stock"
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes": ("collapse", ),
            "fields": ("description",),
            'description': "You can use this section for optionals settings"
        })
    )

    actions = ("is_in_stock",)

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")

    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"
admin.site.index_title = "Welcome to Clarusway Admin Portal"
