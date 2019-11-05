from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
from .models import Prod, Service, Work, Price
from .forms import ProdForm, ServicesForm, PortfolioForm, SendForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, EmailMessage


def main_page(request):
    return render(request, 'core/main.html')


def about(request):
    return render(request, 'core/about.html')


def portfolio_list(request):
    works = Work.objects.all()[::-1]
    return render(request, 'core/portfolio.html', context={'works': works})


def portfolio_detail(request, slug):
    work = Work.objects.get(slug__iexact=slug)
    return render(request, 'core/portfolio_detail.html', context={'work': work})


class PortfolioCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PortfolioForm()
        return render(request, 'core/portfolio_create.html', context={'form': form})

    def post(self,request):
        bound_form = PortfolioForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_prod = bound_form.save()
            return redirect(new_prod)
        return render(request, 'core/portfolio_create.html', context={'form': bound_form})

    raise_exception = True


def products_list(request):
    prods = Prod.objects.all()[::-1]
    return render(request, 'core/products.html', context={'prods': prods})


def product_detail(request,slug):
    product = Prod.objects.get(slug__iexact=slug)
    return render(request, 'core/product_detail.html', context={'product': product})


class ProdCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ProdForm()
        return render(request, 'core/product_create.html', context={'form': form})

    def post(self,request):
        bound_form = ProdForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_prod = bound_form.save()
            return redirect(new_prod)
        return render(request, 'core/product_create.html', context={'form': bound_form})

    raise_exception = True


class ProdUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        prod = Prod.objects.get(slug__iexact=slug)
        bound_form = ProdForm(instance=prod)
        return render(request, 'core/product_update_form.html', context={'form': bound_form, 'prod': prod})

    def post(self, request, slug):
        prod = Prod.objects.get(slug__iexact=slug)
        bound_form = ProdForm(request.POST, request.FILES, instance=prod)

        if bound_form.is_valid():
            new_prod = bound_form.save()
            return redirect(new_prod)
        return render(request, 'core/product_update_form.html', context={'form': bound_form, 'prod': prod})

    raise_exception = True


class ServiceCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ServicesForm()
        return render(request, 'core/service_create.html', context={'form': form})

    def post(self,request):
        bound_form = ServicesForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_service = bound_form.save()
            return redirect(new_service)
        return render(request, 'core/service_create.html', context={'form': bound_form})

    raise_exception = True


class ServiceUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        service = Service.objects.get(slug__iexact=slug)
        bound_form = ServicesForm(instance=service)
        return render(request, 'core/service_update_form.html', context={'form': bound_form, 'service': service})

    def post(self, request, slug):
        service = Service.objects.get(slug__iexact=slug)
        bound_form = ServicesForm(request.POST, request.FILES, instance=service)

        if bound_form.is_valid():
            new_serv = bound_form.save()
            return redirect(new_serv)
        return render(request, 'core/service_update_form.html', context={'form': bound_form, 'service': service})

    raise_exception = True


def services_list(request):
    services = Service.objects.all()[::-1]
    return render(request, 'core/services.html', context={'services': services})


def service_detail(request, slug):
    service = Service.objects.get(slug__iexact=slug)
    fill10 = service.fill10
    fill10 = fill10.split(' ')
    is10 = 1
    if fill10[0] == '':
        is10 = 0
    fill50 = service.fill50
    fill50 = fill50.split(' ')
    is50 = 1
    if fill50[0] == '':
        is50 = 0
    fill100 = service.fill100
    fill100 = fill100.split(' ')
    is100 = 1
    if fill100[0] == '':
        is100 = 0
    quantity = service.quantity
    quantity = quantity.split(' ')
    return render(request, 'core/service_detail.html', context={'service': service, 'quantity': quantity,

                                                                'fill10': fill10, 'fill50': fill50, 'fill100': fill100,
                                                                'is10': is10, 'is50': is50,
                                                                'is100': is100})


def send_online(request):
    sent = False
    if request.method=='POST':
        form = SendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            info = cd['info']
            url = cd['url']
            subject = name
            message = '''{0} 
            Ссылка на документы - {1}'''.format(info, url)
            email = EmailMessage(
                subject,
                message,
                'SizovVlad02@yandex.ru',
                ['SizovVlad02@yandex.ru']
            )
            email.send()
            sent = True
    else:
        form = SendForm()
    return render(request, 'core/send.html', context={'form': form, 'sent': sent})




















