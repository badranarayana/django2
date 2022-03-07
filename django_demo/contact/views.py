from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from .forms import ContactModelForm, ContactForm

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
        # empty form
        form = ContactForm()

        return render(request, template_name='contact/create_contact.html',
                      context={'form': form})
    elif request.method == 'POST':
        #import pdb;pdb.set_trace()
        # n for next line
        # c continue
        # bounded form
        form = ContactForm(request.POST)

        # we should validate before saving to db
        if form.is_valid(): # it return true if all validations passed
            # cleaned data is a dict contains input data
            name = form.cleaned_data['name']
            mobile_number = form.cleaned_data['mobile_number']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            # creating model object and saving db
            contact_obj = Contact(name=name,
                                  mobile_number=mobile_number,
                                  date_of_birth=date_of_birth,
                                  email=email,
                                  location=location)
            contact_obj.save()
        else:
            return render(request, template_name='contact/create_contact.html',
                          context={'form': form})

        return redirect(to='get-contacts')


# reference for model form
def _create_contact(request):
    if request.method == 'GET':
        # empty form
        form = ContactModelForm()

        return render(request, template_name='contact/create_contact.html',
                      context={'form': form})
    elif request.method == 'POST':
        """
        (Pdb) request.POST
<QueryDict: {'csrfmiddlewaretoken': ['OYQVB64uuZco7sXREEf48Z7Uu7cXjKBCNADM3IM8zEVwSDzv5POg9CfKoWre2ytU'], 'name': ['ram'], 'mnumber': ['
889999993'], 'dob': ['2022-02-18'], 'email': ['abnra@gmail.com'], 'location': ['hyderabad']}>

        """
        # capturing user entered data on UI
        # name = request.POST['name']
        # mobile_number = request.POST['mnumber']
        # date_of_birth = request.POST['dob']
        # email = request.POST['email']
        # location = request.POST['location']
        #
        # contact_obj = Contact(name=name, mobile_number=mobile_number,
        #                       date_of_birth=date_of_birth, email=email, location=location)

        # save the data into db
        # contact_obj.save()

        # print(name, mobile_number, date_of_birth, email, location)

        # bounded form
        form = ContactModelForm(request.POST)

        # we should validate before saving to db
        if form.is_valid():  # it return true if all validations passed
            form.save()
        else:
            return render(request, template_name='contact/create_contact.html',
                          context={'form': form})

        return redirect(to='get-contacts')


def list_contacts(request):
    # we will fecth the all record from contact table and render into html document
    return HttpResponse("HDHDHDHHDHD")






