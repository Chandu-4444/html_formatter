from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.is_ajax():
        data = request.POST.get('text', None)

        if data:
            response=  {
                'msg': data
            }
            return JsonResponse(response)
        else:
            response = {
                'msg': ""
            }
            return JsonResponse(response)

