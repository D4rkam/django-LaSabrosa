from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    #Si el metodo es igual a POST, se recuperan los datos del formulario
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            #Creamos el correo
            email = EmailMessage(
                "La Sabrosa: Nuevo Mensaje de contacto", #Asunto
                "De {} {}\n\nEscribió:\n\n{}".format(name, email, content), #Mensaje
                "lasabrosa.com", #Email de Origen
                ["thomaslinares32@gmail.com"], #Email de destino
                reply_to=[email]
            )

            #Lo enviamos y redireccionamos
            try:
                email.send()
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo fallo, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'form':contact_form})

    