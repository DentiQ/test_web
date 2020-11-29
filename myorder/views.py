from django.shortcuts import render, get_object_or_404, redirect
from .models import Dinner, Style, Order
from .forms import OrderForm
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse


def index(request):
    """dinner, style 목록 출력"""
    dinner_list = Dinner.objects.order_by('dinnername')
    style_list = Style.objects.order_by('stylename')
    context = {'dinner_list': dinner_list, 'style_list': style_list}
    return render(request, 'myorder/dinner_style_list.html', context)


def order_list(request):
    """order 목록 출력"""
    order_list = Order.objects.order_by('-create_date')
    context = {'order_list': order_list}
    return render(request, 'myorder/order_list.html', context)


def order_detail(request, order_id):
    """order 상세출력"""
    order = get_object_or_404(Order, pk=order_id)
    context = {'order':order}
    return render(request, 'myorder/order_detail.html', context)


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.create_date = timezone.now()
            order.save()
            return redirect('pybo:index')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'myorder/order_form.html', context)


