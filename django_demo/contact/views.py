from django.shortcuts import render, HttpResponse, redirect
from .models import Contact

# Create your views here.

def index(request):
    # keep
    return HttpResponse("Response coming from index view")


def get_contact(request):
    # we connect to db and fetch the contact data
    # and give in response to the user
    contacts = Contact.objects.all()

    context = {'contacts': contacts}
    return render(request, template_name='contact/contacts_list.html', context=context)



def create_contact(request):
    if request.method == 'GET':
        return render(request, template_name='contact/create_contact.html')
    elif request.method == 'POST':
        """
        (Pdb) request.POST
<QueryDict: {'csrfmiddlewaretoken': ['OYQVB64uuZco7sXREEf48Z7Uu7cXjKBCNADM3IM8zEVwSDzv5POg9CfKoWre2ytU'], 'name': ['ram'], 'mnumber': ['
889999993'], 'dob': ['2022-02-18'], 'email': ['abnra@gmail.com'], 'location': ['hyderabad']}>
        
        """
        # capturing user entered data on UI
        name = request.POST['name']
        mobile_number = request.POST['mnumber']
        date_of_birth = request.POST['dob']
        email = request.POST['email']
        location = request.POST['location']

        contact_obj = Contact(name=name, mobile_number=mobile_number,
                              date_of_birth=date_of_birth, email=email, location=location)

        # save the data into db
        contact_obj.save()

        #print(name, mobile_number, date_of_birth, email, location)

        return redirect(to='get-contacts')

def list_contacts(request):
    # we will fecth the all record from contact table and render into html document
    return HttpResponse("HDHDHDHHDHD")






