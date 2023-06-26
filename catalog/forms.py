from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    @staticmethod
    def has_forbidden_words(field_content: str) -> bool:
        return bool(len(ProductForm.forbidden_words & set(field_content.split())))

    class Meta:
        model = Product
        # fields = '__all__'
        # # fields = ('product_name', 'product_description', 'product_cost',)
        exclude = ('product_data_created', 'product_last_data_change',)

    def clean_product_name(self):
        clean_data = self.cleaned_data['product_name']
        # Если пересечение множества запрещённых слов и множества слов введённых в поле 'product_name' не пустое
        if self.has_forbidden_words(clean_data):
            raise forms.ValidationError(f'Поле "Наименование" не должно содержать '
                                        f'слов - {", ".join(ProductForm.forbidden_words)}.')

        return clean_data

    def clean_product_description(self):
        clean_data = self.cleaned_data['product_description']
        # Если пересечение множества запрещённых слов и множества слов введённых в поле 'product_name' не пустое
        if self.has_forbidden_words(clean_data):
            raise forms.ValidationError(f'Поле "Описание" не должно содержать '
                                        f'слов - {", ".join(ProductForm.forbidden_words)}.')

        return clean_data


class ProductVersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        """
        нельзя добавить более одной активной версии
        """
        is_active = self.cleaned_data['is_active']
        print(is_active)
        # product = self.cleaned_data['product']
        if self.instance.product:
            if is_active and self.instance.product.version_set.filter(is_active=True).exclude(id=self.instance.id).exists():
                raise forms.ValidationError('Нельзя добавить более одной активной версии')
        return is_active
