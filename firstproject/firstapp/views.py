from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def hello(request):
    userName=request.GET['name'] 
    # welcome.html에서 name으로 받은거를 username이라는 변수에 저장한 것.
    return render(request, "hello.html", {'userName':userName})
    #hello.html에서 userName을 받을 때는, {{userName}}이렇게 쓴다.
