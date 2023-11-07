from django.http import JsonResponse


def default(request):
    return JsonResponse({'Funcionou': 1})
