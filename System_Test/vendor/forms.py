from .models import VendorMdel
from django import forms

# ------------ model form for Vendor and Bidder-------------------------------------------
class VendorMdelForm(forms.ModelForm):
    class Meta:
        model  = VendorMdel
        fields = '__all__'
