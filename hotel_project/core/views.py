from django.http import HttpResponse

def home(request):
    print("Website is running!!!!!!!@@@@@#####")
    return HttpResponse("Welcome to the Motel Website!!!!")
