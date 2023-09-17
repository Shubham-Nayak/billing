from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from myapp.models import Mysetting
from myapp.models import ProductListing

from .models import Order
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from reportlab.pdfgen    import canvas
from reportlab.lib.utils import ImageReader
from datetime            import datetime



def index(request):
    settings=Mysetting.objects.get()
    orders=Order.objects.order_by('-purchase_date')
   

    paginator= Paginator(orders,10)
    page= request.GET.get('page')
    paged_listings= paginator.get_page(page)
    contex={
        "listings":paged_listings,
        "settings":settings,
        "values":request.POST
    }

    if request.method == 'POST':
                HSN_Code= request.POST['HSN_Code']
                name= request.POST['name']
                email= request.POST['email']
                phone= request.POST['phone']
                discounted_price= request.POST['discounted_price']
                gram= request.POST['gram']
                user_id= request.POST['user_id']
                purchase_mode= request.POST['purchase_mode']
                saller= request.POST['saller']

                Has_HSN=ProductListing.objects.filter(HSN_Code=HSN_Code).exists()
                if Has_HSN:
                    data =Order(HSN_Code=HSN_Code,name=name,phone=phone,email=email,discounted_price=discounted_price,user_id=user_id,gram=gram,purchase_mode=purchase_mode,saller=saller)
                    data.save()
                    messages.success(request, 'Bill genrated !')
                    return render(request,'orders/orderlisting.html',contex)
                else:
                    messages.error(request, 'Please enter valid HSN Code')
                    return render(request,'orders/orderlisting.html',contex)    




    return render(request,'orders/orderlisting.html',contex)


def create_order(request):
    settings=Mysetting.objects.get()
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    name= request.POST['name']

    response['Content-Disposition'] = 'attachment; filename="'+name+'"' 

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')

    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response)

    # Write content on the PDF 
    p.drawString(100, 500, "Hello " + get_param + " (Dynamic PDF) - " + ts ) 

    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response



                