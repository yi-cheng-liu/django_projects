from django.forms import ModelForm
from gadgets.models import Gadget, Brand

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
