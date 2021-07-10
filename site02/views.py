from django.shortcuts import render, HttpResponse

# Create your views here.
def appindex(request):
    #return HttpResponse("This is app index page.")
    progress = 'in progress'
    value = 1999
    context = {'status1':progress,'status2':value}
    return render(request, 'app-about.html', context)

def aboutpost(request):
    #print(request)
    if request.method == 'GET':
        temp = {}
        progress = request.GET.get('Text1')

    value = 1999
    context = {'status1':progress,'status2':value}
    return render(request, 'aboutpost.html', context)
