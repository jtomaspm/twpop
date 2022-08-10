from django.http import JsonResponse
import json

def api_home(request, *args, **kargs):
    try:
        data = json.loads(request.body)
        print(data)
    except:
        print("error")
    return JsonResponse(
        {
            "msg" : "Hello World"
        }
    )