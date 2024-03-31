from django import forms

from catalog.models import Product, Version


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово - "{word}"')

            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('version_indicator',)

