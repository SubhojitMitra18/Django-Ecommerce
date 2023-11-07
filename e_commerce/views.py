from django.shortcuts import render,redirect,HttpResponse
from app.models import Category,Product,Contact_us,Order
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from e_commerce.forms import UserCreateForm,MyLogForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

import razorpay
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="login")
def cart_add(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="login")
def item_increment(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")
@login_required(login_url="login")
def item_decrement(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="login")
def cart_clear(request):
    cart=Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="login")
def cart_detail(request):
    return render(request,'cart/cart_detail.html')

    

def Master(request):
    return render(request,'master.html')

def Index(request):
    category=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product=Product.objects.all()
    context={
        'category':category,
        'product': product,
    }
    return render(request,'index.html',context)

def signup(request):
    if request.POST:
        form=UserCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your registration is successfull')
            except Exception as e:
                messages.error(request, 'Your registration is not successfull')
    else:
        form=UserCreateForm()
    return render(request, 'registration/signup.html', {'form':form})
    
    '''
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            new_user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect('index')
    else:
        form=UserCreateForm()
    
    context={
        'form':form,
    }
    
    return render(request,'registration/signup.html',context)'''
def login_view(request):
    if request.POST:
        frm=MyLogForm(request=request, data=request.POST)
        if frm.is_valid():
            uname=frm.cleaned_data['username']
            upass=frm.cleaned_data['password']
            user=authenticate(request,username=uname, password=upass)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        frm=MyLogForm()
    return render(request, 'registration/login.html',{'frm':frm})


def userLogout(request):
    logout(request)
    return redirect('/login')

def contact_page(request):
    if request.method=="POST":
        contact=Contact_us(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        contact.save()
    return render(request,'contact_us.html')

'''
def Checkout(request):
    if request.method=='POST':
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        pincode=request.POST.get('pincode')
        uid=request.session.get('_auth_user_id')
        cart=request.session.get('cart')
        user=User.objects.get(id=uid)
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        
        for i in cart:
            a=int(cart[i]['price'])
            b=cart[i]['quantity']
            total=a*b
            order=Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                phone=phone,
                pincode=pincode,
                total=total
            )
            order.save()
        payment = client.order.create({
        'amount': total * 100,
        'currency': 'INR',
        'payment_capture': 1,  # Auto-capture payments
    })
        order1 = Order(user = request.user, razorpay_order_id = payment['id'])
        
        order1.save()
        request.session['cart']={}
        return redirect("index")
        
    return HttpResponse('This is Checkout Page')

'''


def Checkout(request):
    if request.method.POST:
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        uid = request.session.get('_auth_user_id')
        cart = request.session.get('cart')
        user = User.objects.get(id=uid)

        # Initialize the Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        # Calculate the total amount from the cart
        total_amount = 0
        for item in cart.values():
            total_amount += int(item['price']) * item['quantity']
        # Create a Razorpay order
        payment = client.order.create({
            'amount': int(total_amount) * 100,  # Amount should be in paise
            'currency': 'INR',
            'payment_capture': 1,  # Auto-capture payments
        })

        # Save the Razorpay order ID to the database
        order = Order(user=user, razorpay_order_id=payment['id'])
        order.save()

        # Now, you can clear the user's cart
        request.session['cart'] = {}

        # Redirect to the payment page, which can use Razorpay JavaScript to complete the payment
        context = {
            'phone':phone,
            'address': address,
            'payment': payment,
        }
        print(context)
        return render(request, 'checkout.html', context)
    

    return HttpResponse('This is Checkout Page')



def Your_Order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)
    order = Order.objects.filter(user=user)
    context={
        "order":order,
    }
    return render(request,'order.html',context)

