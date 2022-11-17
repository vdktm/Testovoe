from django.shortcuts import render


def hello_rekruto(request):
    return render(request, 'hello/index.html')







# from django.http import HttpResponse
#
#
# def hello_rekruto(request):
#     name = request.GET.get("name", "Rekruto")
#     message = request.GET.get("message", "Давай дружить!")
#     return HttpResponse(f"Hello {name}! {message}!")
