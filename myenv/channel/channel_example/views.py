from django.contrib.auth import login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.urls import reverse
from django.shortcuts import render,redirect

User = get_user_model()

@login_required(login_url='/log_in/')
def user_list(request):
	users = User.objects.select_related('logged_in_user')
	for user in users:
		user.status = 'Online' if hasattr(user,'logged_in_user') else 'Offline'
	return render(request,'channel_example/user_list.html',{'users':users})

def log_in(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request,form.get_user())
			return redirect(reverse('channel_example:user_list'))
		else:
			print(form.errors)
	return render(request,'channel_example/log_in.html',{'form':form})


@login_required(login_url='/log_in/')
def log_out(request):
	logout(request)
	return redirect(reverse('channel_example:log_in'))

def sign_up(request):
	form = UserCreationForm()
	if request.method =='POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('channel_example:log_in'))
		else:
			print(form.errors)
	return render(request,'channel_example/sign_up.html',{'form':form})
