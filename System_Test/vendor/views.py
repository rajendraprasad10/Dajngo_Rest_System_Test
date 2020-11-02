from django.shortcuts import render
from .forms import VendorMdelForm
from .models import VendorMdel
from rest_framework import viewsets
from .serializers import VendorSerializer
from .models import VendorMdel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer



# ---------------------- Create index  views here. --------------------------------------------

def index(request):
    if request.method == 'POST':
        form =  VendorMdelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VendorMdelForm()

    context = {'form' : form}
    return render(request, 'index.html', context)


#  ------------------------ Vendor & Bidder API -----------------------------------------------------------
class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = VendorMdel.objects.all()



# -------------Get Register data-----------------------------------------------------------------

def register(request):
    userdata = VendorMdel.objects.all()
    context = {'user': userdata}
    return render(request, 'register.html', context)


# -------------------------Create user LoginAPI for same VendorAPI------------------------------------------

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['email'] = account.email
            data['first_name'] = account.first_name
        else:
            data = serializer.errors
        return Response(data)


# ------------------- contact page -------------------------------------------------------------------------

def contact(request):
    return render(request, 'contact.html')