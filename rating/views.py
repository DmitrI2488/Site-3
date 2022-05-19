from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from Home.models import rating


def ratings(request):
    alla = Paginator(rating.objects.filter(passed = False).order_by('-id'), 8)
    stra = request.GET.get('page')
    alla = alla.get_page(stra)
    rat = Paginator(rating.objects.all().order_by('-id'), 8)
    page = request.GET.get('page')
    chanels = rat.get_page(page)
    rating_list = rating.objects.filter(passed=True).order_by('-id')
    rating_list = Paginator(rating_list, 8)
    page2 = request.GET.get('page')
    rating_list = rating_list.get_page(page2)
    return render(request, 'rating/rating.html',
                  {'chanels': chanels,
                   'chanel': alla,
                   'rating_list': rating_list
                   })


def failed(request):
    rat = Paginator(rating.objects.filter(passed = False).order_by('-id'), 8)
    page = request.GET.get('page')
    chanels = rat.get_page(page)
    return render(request, 'rating/failed.html',
                  {'rating_list': chanels})


def dyn_ratings(request, offset):
    cards = rating.objects.filter(id__gte=offset, id__lte=offset+8)
    return JsonResponse({'cards': cards})


class ratingsView(ListView):
    model = rating
    template_name = 'rating/rating.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        alla = Paginator(rating.objects.filter(passed=False).order_by('-id'), 8)
        stra = self.request.GET.get('page')
        context['chanel'] = alla.get_page(stra)
        rat = Paginator(rating.objects.all().order_by('-id'), 8)
        page = self.request.GET.get('page')
        context['chanels'] = rat.get_page(page)

        context['rating_list'] = rating.objects.filter(passed=True).order_by('-id')
        context['rating_list']= Paginator(context['rating_list'], 8)
        page2 = self.request.GET.get('page')
        try:
            context['rating_list'] = context['rating_list'].get_page(page2)
        except PageNotAnInteger:
            context['rating_list'] = context['rating_list'].get_page(1)
        except EmptyPage:
            context['rating_list'] = context['rating_list'].get_page(context['rating_list'].num_pages)

        return context
