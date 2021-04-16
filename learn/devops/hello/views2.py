from django.http import HttpResponse
from django.views.generic import View

def index(request):
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')
    elif request.method == 'PUT':
        return HttpResponse('put')
    elif request.method == 'DELETE':
        return HttpResponse('delete')

class IndexView(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    def delete(self, request):
        return HttpResponse('delete')
