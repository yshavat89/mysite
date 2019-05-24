from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import Treasure
from .forms import TreasureForm
from django.contrib.auth.models import Permission, User

def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('myapp.change_blogpost')

    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.get(
        codename='change_blogpost',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('myapp.change_blogpost')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('myapp.change_blogpost')  # True




class IndexView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    # LoginRequiredMixin
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    permission_required = 'treasure.create_treasure'

    #PermissionRequiredMixin,
    # PermissionRequiredMixin handel pramissions
    #permission_required = 'polls.can_vote'
    # Or multiple of permissions:
    #permission_required = ('polls.can_open', 'polls.can_edit')

    # UserPassesTestMixin test user attributes 
    def test_func(self):
        return self.request.user.email.endswith('@gmail.com')


    # generic.ListView
    template_name = 'treasure/index.html'
    context_object_name = 'treasures_list'

    def get_queryset(self):
        """Return all treasures."""
        return Treasure.objects.all()

class DetailView(LoginRequiredMixin,generic.DetailView):
    # LoginRequiredMixin
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    # generic.DetailView
    model = Treasure
    context_object_name = 'treasure'
    template_name = 'treasure/detail.html'


class TreasureCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # PermissionRequiredMixin :
    permission_required = 'treasure.create_treasure'

    # CreateView
    model = Treasure
    fields = ['name','value', 'material', 'location', 'image']

class TreasureFormView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TreasureForm
    template_name = 'treasure/treasure_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(commit=True)
        treasures_list = Treasure.objects.all()
        return render(request, 'treasure/index.html', {'treasures_list': treasures_list})