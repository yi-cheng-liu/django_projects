from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gadgets.models import Gadget, Brand
from gadgets.forms import BrandForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Brand.objects.all().count()
        al = Gadget.objects.all()

        ctx = {'brand_count': mc, 'gadget_list': al}
        return render(request, 'gadgets/gadget_list.html', ctx)


class BrandView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Brand.objects.all()
        ctx = {'brand_list': ml}
        return render(request, 'gadgets/brand_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class BrandCreate(LoginRequiredMixin, View):
    template = 'gadgets/brand_form.html'
    success_url = reverse_lazy('gadgets:all')

    def get(self, request):
        form = BrandForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BrandForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        brand = form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BrandUpdate(LoginRequiredMixin, View):
    model = Brand
    success_url = reverse_lazy('gadgets:all')
    template = 'gadgets/brand_form.html'

    def get(self, request, pk):
        brand = get_object_or_404(self.model, pk=pk)
        form = BrandForm(instance=brand)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        brand = get_object_or_404(self.model, pk=pk)
        form = BrandForm(request.POST, instance=brand)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class BrandDelete(LoginRequiredMixin, View):
    model = Brand
    success_url = reverse_lazy('gadgets:all')
    template = 'gadgets/brand_confirm_delete.html'

    def get(self, request, pk):
        brand = get_object_or_404(self.model, pk=pk)
        form = BrandForm(instance=brand)
        ctx = {'brand': brand}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        brand = get_object_or_404(self.model, pk=pk)
        brand.delete()
        return redirect(self.success_url)


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class GadgetCreate(LoginRequiredMixin, CreateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetDelete(LoginRequiredMixin, DeleteView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createviewd
