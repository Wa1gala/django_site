from django.contrib import admin

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class SneakersAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px;">Минимальный размер изображения {}x{}!</span>""".format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Зармер изображения превыщает 3MB')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изобрашение меньше минимального')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Загруженное изобрашение меньше минимального')
        return image


class TshirtAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px;">Минимальный размер изображения {}x{}!</span>""".format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Зармер изображения превыщает 3MB')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изобрашение меньше минимального')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Загруженное изобрашение меньше минимального')
        return image


class TshirtAdmin(admin.ModelAdmin):
    form = TshirtAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tshirt'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SneakersAdmin(admin.ModelAdmin):
    form = SneakersAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Tshirt, TshirtAdmin)
admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
