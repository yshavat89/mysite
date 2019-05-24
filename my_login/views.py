from django.views import generic
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth import logout
from django.contrib.auth.models import Permission, User


def logout_view(request):
    logout(request)
    return redirect('polls:index')


class LoginFormView(View):
    form_class = UserForm
    template_name = 'my_login/Signin.html'

    def get(self, request):

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('polls:question_add')
        else:
            return redirect('my_login:login')


class UsersView(generic.ListView):

    template_name = 'my_login/users.html'
        
    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.all()
