from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from cartapp.models import cart
from productapp.models import stock, product

@login_required()
def cartview(request):
    return render(request, 'cart1.html', {'records': display(request)})


# @login_required
# def delete(request):
#     return render(request,'delete.html')

# @login_required
# def cancel(request):
#     return render(request,'cancel.html')
@login_required
def addcart(request):
    x = request.GET["pid"]
    qt = stock.objects.filter(prodid=int(request.GET["pid"]))
    qtt=0
    for p in qt:
        qtt=p
    qt=[q for q in range(1,qtt.totqty+1)]
    return render(request, 'addcart.html', {"pid": x, "qtt": qt})


def insertcart(request):
    x = request.GET["pid"]
    qt = request.GET["qtt"]
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    pr = product.objects.get(pid=int(x))
    stc = stock.objects.get(prodid=int(request.GET["pid"]))
    stc.totqty = int(stc.totqty) - int(qt)
    stc.save()
    a = int(str(x))
    b = int(str(qt))
    c = un
    d = float(pr.pcost)
    e = int(str(qt)) * float(pr.pcost)
    f = pr.pimage
    ct = cart(username=c, pid=a, units=b, unitprice=d, tuprice=e, image=f)
    ct.save()
    return render(request, 'insertcart.html')


#
def delete(request):
    cts = cart.objects.filter(id=int(request.GET["id"]))
    stc = stock.objects.get(prodid=int(request.GET["pid"]))
    stc.totqty = int(stc.totqty) + int(request.GET["units"])
    stc.save()
    cts.delete()
    return render(request, 'cart1.html', {'records': display(request)})


def cancel(request):
    return render(request, 'welcome.html')


def display(request):
    user = User.objects.get(id=request.session.get("_auth_user_id"))
    un = str(user.username)
    ct = cart.objects.filter(username=un)
    # tp=0.0
    # ctid=0
    # for p in ct:
    #     tp=tp+float(p.tuprice)
    #     ctid=p.id
    # dic={"k":ct}
    return ct


def modify(request):
    x = request.GET["pid"]
    qt = stock.objects.filter(prodid=x)
    qtt = 0
    for p in qt:
        # global qtt
        qtt = p
    qt = [q for q in range(1, qtt.totqty + 1)]
    oldqt = request.GET['units']
    unitprice=request.GET["unitprice"]
    tuprice = request.GET['tuprice']
    cid=request.GET["id"]
    return render(request, 'modifyqty.html', {"pid": x, "qtt": qt, "units": oldqt,"unitprice":unitprice,"cartid":cid})


def modifiedcart(request):
    cid= int(request.GET["cid"])
    nqt = int(request.GET["nqt"])
    stc = stock.objects.get(prodid=int(request.GET["pid"]))
    stc.totqty = int(stc.totqty) + int(request.GET["units"]) - nqt
    stc.save()
    up = float(request.GET["unitprice"])
    id = int(request.GET["pid"])
    ct = cart.objects.get(id=cid)
    ct.units = nqt
    ct.tuprice = up * nqt
    ct.save()
    return render(request, 'cart1.html', {'records': display(request)})
   # obj = cart.objects.filter(pid=int(x))
    # obj.units = nqt
    # up=request.GET["unitprice"]
    # obj.tuprice = up*nqt

