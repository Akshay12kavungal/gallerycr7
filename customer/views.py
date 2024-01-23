from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from django.views.generic import View
from .forms import uploadimageForm

from .models import uploadimage


# Create your views here.
from django.http import HttpResponse
# ------------home page-------------
def home(request):
    return render(request,"home.html")



# -----------signup page--------------------
def signup(request):
    if request.method == 'POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Profile.objects.filter(Name=Name):
           messages.error(request,"Username already exist")
           return redirect('signup')
        elif  Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('signup')

        elif Password!=Confirm_Password:
            messages.error(request,"password didn't match")


        signup_objt=Profile(Name=Name,Email=Email,Password=Password,Confirm_Password=Confirm_Password)
        signup_objt.save()
        return render(request,'home.html')
                                
    elif request.method=='GET':
        return render(request,'signup.html')

    else:
         
        return HttpResponse("an expectation occured")

        
    return render(request,"signup.html")



 #-----------login page--------------------   

def login(request):
    if request.method=='POST':
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        profile=Profile.objects.filter(Password=Password)
        if not profile.exists():
            return redirect('signup')

        return redirect('home')
       

    return render(request,'login.html')

#-----------page--------------------





class CustomerListing(View):
    template_name = 'registrationlist.html'

    def get(self,request):
        cust_obj = Profile.objects.all()
        context = {
        'registrationlist':cust_obj
        }
        return render(request,self.template_name,context)



def upload_image(request):
    if request.method == 'POST':
        form = uploadimageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadimage_list')  # Replace 'success_url' with your actual success URL
    else:
        form = uploadimageForm()
        img_obj = uploadimage.objects.all()

    return render(request, 'upload_image.html', {'img_obj':img_obj,'form': form})









# delete profile



def delete_Profile(request,Id, *args, **kwargs):
    profile_obj = Profile.objects.get(Id=Id)
    profile_obj.delete()
    return redirect('registrationlist')