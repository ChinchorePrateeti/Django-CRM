from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    #grabbing all the records using .all
    records = Record.objects.all()
    # check to see if login is done
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authneticate
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in..")
            return redirect('home')
        else:
            messages.success(request, "You have an error in log in..")
            return redirect('home')
    else:
        return render (request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out...")
    return redirect('home')
    
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate here
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password = password)
            login(request, user)
            messages.success(request, "Yu have registered successfully...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You need to login first..")
        return redirect('home')

def customer_record_delete(request, pk):
    if request.user.is_authenticated:
        customer_record_delete = Record.objects.get(id=pk)
        customer_record_delete.delete()
        messages.success(request, "Your selected ID's record details deleted successfully...")
        return redirect("home")
    else:
        messages.success(request, "You need to login to delete the record!!!")
        return redirect('home')

def customer_record_add(request):
    form = AddRecordForm(request.POST or None)

    # meaning logged in
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfuly")
                return redirect('home')
        return render(request, 'record_add.html', {'form':form})
    else:
        messages.success(request, "You need to login first......")
        return redirect('home')

def record_update(request, pk):
    if request.user.is_authenticated:
        record_update = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance= record_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record is updated successfully.")
            return redirect('home')
        return render(request, 'record_update.html', {'form':form})

    else:
        messages.success(request, "You need to login first!!")
        return redirect('home')
