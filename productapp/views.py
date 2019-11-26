from django.shortcuts import render
# Create your views here.
from productapp.models import product

def search(request):
    x = request.GET['pcat']
    y = request.GET['pname']
    recs = product.objects.filter(pcat=x,pname=y)
    return render(request,'products.html', {'records':recs})
def search1(request):
    x = request.GET['pcat']
    y = request.GET['pname']
    recs = product.objects.filter(pcat=x, pname=y)
    return render(request,'product1.html', {'records':recs})