from django.http import HttpResponse


def index(request):
    name = request.GET.get("name", "Rekruto")
    message = request.GET.get("message", "Давай дружить!")
    return HttpResponse(f"Hello {name}! {message}!")
