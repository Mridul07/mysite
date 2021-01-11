from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from tester.models import MyUser
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
# Create your views here.
## Dont name apps as accounts <-----

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        designation = request.POST['designation']
        dob = request.POST['birthday']

        print(dob)

        if password1 == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, 'Email id Taken')
                return redirect('register')
                #return redirect('register')
            else:
                user = MyUser.objects.create_user(password=password1, email=email, date_of_birth=dob, designation=designation, first_name=first_name, last_name=last_name) ## Add over here
                #sirf create
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matched')
            return redirect('register')
        return redirect('/')


    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


def welcome(request):
    context = {"index_page" : "active"}
    return render(request, 'index.html', context)


def upload(request):
    context = {}
    #print(MyUser.email)
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] =fs.url(name)
    return render(request, 'upload.html', context)

def book_list(request):
    print(request.user.email)
    fetch_email = request.user.email
    #books = Book.objects.all()
    books = Book.objects.filter(email=fetch_email)
    return render(request,'book_list.html', {
        'books': books
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{
        'form': form
    })


## New functions for manager view and manager change status
def book_list_manager(request):

    books = Book.objects.all()
    #books = Book.objects.filter(email="cavani@gmail.com")
    return render(request,'book_list_manager.html', {
        'books': books
    })

def update_status(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.status = True
        book.save()
    return redirect('book_list_manager')