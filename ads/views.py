import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def root(request):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for i in ads:
            response.append({'id': i.pk,
                             'name': i.name,
                             'author': i.author,
                             'price': i.price})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        res = Ad.objects.create(**data)
        return JsonResponse({
            'id': res.pk,
            'name': res.name,
            'author': res.author,
            'price': res.price,
            'description': res.description,
            'address': res.address,
            'is_published': res.is_published
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for i in categories:
            response.append({'id': i.pk, 'name': i.name})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        res = Category.objects.create(**data)
        return JsonResponse({
            'id': res.pk,
            'name': res.name
        }, safe=False)


class CatDetailView(DetailView):
    model = Category
    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name}, safe=False)


class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published}, safe=False)
