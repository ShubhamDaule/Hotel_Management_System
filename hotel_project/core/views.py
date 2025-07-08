from django.http import HttpResponse

def home(request):
    print("Website is running!!!!!!!@@@@@##########@@@@@@@@##0000###")
    return HttpResponse("Welcome to the Motel Website!!!!")
