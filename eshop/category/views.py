from django.shortcuts import render
from django.http import HttpResponse
from .models import Laptop , Category
from django.views.generic import DetailView
# Create your views here.


all_categories = Category.objects.all()
category = None
def test(request):
    laptop_instance = Laptop()
    all_laptop = laptop_instance.get_all()
    # laptop_instance.delete_all()
    ctx = {}
    ctx['category_name'] = 'all'
    ctx['all_laptop'] = all_laptop
    print(all_laptop)
    return render(request , 'category/index.html' , ctx)


def laptops_view(request):
    ctx = {}
    all_laptops = Laptop.objects.all()
    all_categories = Category.objects.all()


    ctx['all_laptops'] = all_laptops
    ctx['category_name'] = 'laptops'
    ctx['all_categories'] = all_categories

    print(all_categories)
    for elem in all_categories:
        print(elem)
    # print(all_laptops)
    return render(request , 'category/laptops.html' , ctx)



class LaptopDetailView(DetailView):
    queryset = Laptop.objects.all()
    template_name = 'category/laptop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LaptopDetailView, self).get_context_data(**kwargs)
        context['category_name'] = 'laptops'
        context['all_categories'] = all_categories
        return context

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.save()
        return obj

MODEL_CHOICE  = {
    'laptops' : Laptop,
}


def search(request):
    ctx = {}
    category  = Category.objects.get(name= request.GET.get('category')).name
    if request.GET.get('to') == '' or request.GET.get('from') == '':
        all_search = MODEL_CHOICE[category].objects.all()
    else:
        all_search = MODEL_CHOICE[category].objects.all().filter(price__lt=request.GET.get('to') , price__gt=request.GET.get('from'))
    ctx['req_category'] =  request.GET.get('category')
    ctx['req_price_to'] = request.GET.get('to')
    ctx['req_price_from'] = request.GET.get('from')
    ctx['all_search'] = all_search
    ctx['all_categories'] = all_categories
    ctx['category_name'] = category
    return render(request , 'category/search.html' , ctx)