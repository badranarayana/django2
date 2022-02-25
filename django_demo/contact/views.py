from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # keep
    return HttpResponse("Response coming from index view")


def get_contact(request):
    # we connect to db and fetch the contact data
    # and give in response to the user
    data = {"Name": "Ravi", "age": 23}
    return HttpResponse(data)


def create_contact(request):
    if request.method == 'GET':
        return render(request, template_name='contact/create_contact.html')
    elif request.method == 'POST':
        # read data from request oject
        # store into db
        pass




