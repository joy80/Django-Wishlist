from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from .models import Wishlist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration.html', {'form': form})


class WishlistView(ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'
    ordering = ['-by']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WishlistView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class WishlistDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Wishlist

    def test_func(self):
        wishlist = self.get_object()
        if self.request.user == wishlist.author:
            return True
        return False


class WishlistCreateView(LoginRequiredMixin, CreateView):
	model = Wishlist
	fields = ['wish', 'by']
	success_url = '/wishlist'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class WishlistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wishlist
    success_url = '/wishlist'

    def test_func(self):
        wishlist = self.get_object()
        if self.request.user == wishlist.author:
            return True
        return False