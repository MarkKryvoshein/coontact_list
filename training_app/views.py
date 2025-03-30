from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactsForm
# Create your views here.
def contact_list(request):
    if request.method == "POST":
        id = request.POST.get("id")
        print(id)
        if id:
            Contact.objects.filter(id=id).delete()
            return redirect("contact_list")

    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactsForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, 'contact_form.html', {'form': form})
    else:
        form = ContactsForm()
        return render(request, 'contact_form.html', {'form': form})

def about_contact(request, contact_id):


    contact = Contact.objects.filter(id=contact_id)
    contact = list(contact)



    return render(request, 'about_contact.html', {'contact': contact[0]})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactsForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, 'contact_form.html', {'form': form})
    else:
        form = ContactsForm(instance = contact)
    return render(request, 'contact_form.html', {'form': form})

