from django.shortcuts import render
from ecommerceapp.models import Contact,Product
from django.contrib import messages
from math import ceil
# Create your views here.
def index(request):
    allProds= []
    catprods=Product.objects.values('catigory','id')
    print(catprods)
    cats={item['catigory'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(catigory=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}

    return render(request,"index.html",params)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        pnumber = request.POST['pnumber']
        myquery = Contact(name=name, email=email, desc=desc, phoneno=pnumber) #from modules files attributes rae taken
        myquery.save()
        messages.info(request,"We will contact you soon!")
        
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def blog(request): 
    return render(request,"blog.html")
    