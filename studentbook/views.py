from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session  
 
# Create your views here.
def readmore(request, id):
    if request.POST:
        #submit comment and submit the page
        message = request.POST['message']
        user_id = request.POST['user_id']
        post_id = id
        
        query = Comment(message = message )
        query.post_id_id = post_id
        query.user_id_id = user_id
        
        query.save()
        
        # Fetch the Blog data based on the passed `id`
    data = Blog.objects.get(id=id)
    comment = Comment.objects.all().filter(post_id=id)
    # Pass the data to the template
    return render(request, 'studentbook/login/readmore.html', {'data': data,'comments':comment})


def create_post(request):
    if request.method == 'POST':
        good_name = request.POST.get('goodname')
        description = request.POST.get('description')
        title = request.POST.get('title')
        image = request.FILES.get('image')  # Use request.FILES for file uploads
        user_id = request.session.get('user_id')
        
        if not user_id:
            messages.error(request, 'User not logged in.')
            return redirect('index')
        
        if not good_name or not description or not title or not image:
            messages.error(request, 'All fields are required.')
            return render(request, 'studentbook/login/create_post.html')
        
        obj = Blog(
            user_id_id=user_id,  # Foreign key reference
            good_name=good_name,
            description=description,
            title=title,
            image=image
        )
        obj.save()
        messages.success(request, 'Post added successfully!')
        return redirect('home')
    
    return render(request, 'studentbook/login/create_post.html')
    
def logout(request):
    #destroy session
    del request.session['is_logged']
    return redirect('index')
    
def home(request):
    if request.session.get('is_logged'):  # Use .get() instead of has_key['key']
        fetch_data = Blog.objects.all()
        
        return render(request, 'studentbook/login/home.html', {'data':fetch_data})
    return redirect('index')

def user_profile(request):
    if request.session.get('is_logged'):
        user_email = request.session.get('email')
        try:
            # Fetch the user details from the database
            user = User.objects.get(email=user_email)
            return HttpResponse("jjjj")
        except User.DoesNotExist:
            return HttpResponse("User not found.")
        
        # Pass user details to the template
        return render(request, 'studentbook/login/user_profile.html', {'user': user})
    
    return redirect('index')  # If not logged in, redirect to login page
    
def index(request):
    if request.POST:
        email = request.POST['email'].lower()
        password = request.POST['password']
        
        # authentication = User()
        
        #SELECT * from user where email = q@gmai.com and password = password 
        count = User.objects.filter(email = email, password = password).count()
        if count > 0:
            request.session['is_logged'] = True
            return redirect('home')
            # return HttpResponse("You are authenticated succesfully")
        else:
            messages.error(request, 'Invalid email or password')
            
            
            return redirect("index")  
        
    return render(request,'studentbook/login/login.html')
def signup(request):
    return render(request, 'studentbook/login/signup.html')

def register_user(request):
    if request.POST:
         username_ = request.POST['username']
         email_ = request.POST['email']
         password_ = request.POST['password']
         
         obj = User(username=username_, email= email_, password=password_)
         obj.save()         
         messages.success(request, 'You are register successfully')
         return redirect('index')
         
         
         
         return HttpResponse(username_ + ' ' + email_ + ' ' + password_)
    return HttpResponse("not working")
