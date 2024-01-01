from django.shortcuts import render
from django.core.mail import send_mail
from blog.models import Post


def home(request):
    latest_posts = Post.objects.order_by('-post_date', '-post_time')[:3]

    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'website/home.html', context)


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        email_body = (f"Ім'я: {message_name}\nEmail: {message_email}\n"
                      f"Номер телефону: {message_phone}\nКоментар: {message}\n")

        send_mail(
            'Паціент ' + message_name,
            email_body,
            message_email,
            ['andreykosmenuk13@gmail.com'],
        )

        return render(request, 'website/contact.html',
                      {'message_name': message_name})
    else:
        return render(request, 'website/contact.html', {})


def methods(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_text = request.POST['your-text']

        appointment_body = (f"Ім'я: {your_name}\nEmail: {your_email}\n"
                            f"Номер телефону: {your_phone}\nКоментар: {your_text}\n")

        send_mail(
            'Паціент ' + your_name,
            appointment_body,
            your_email,
            ['andreykosmenuk13@gmail.com'],
        )

        return render(request, 'website/success_appointment.html',
                      {'your_name': your_name,
                       'your_phone': your_phone,
                       "your_email": your_email,
                       "your_text": your_text})
    else:
        return render(request, 'website/methods.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_text = request.POST['your-text']

        appointment_body = (f"Ім'я: {your_name}\nEmail: {your_email}\n"
                            f"Номер телефону: {your_phone}\nКоментар: {your_text}\n")

        send_mail(
            'Паціент ' + your_name,
            appointment_body,
            your_email,
            ['andreykosmenuk13@gmail.com'],
        )

        return render(request, 'website/success_appointment.html',
                      {'your_name': your_name,
                       'your_phone': your_phone,
                       "your_email": your_email,
                       "your_text": your_text})
    else:
        return render(request, 'website/appointment.html', {})


def success_appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_text = request.POST['your-text']

        appointment_body = (f"Ім'я: {your_name}\nEmail: {your_email}\n"
                            f"Номер телефону: {your_phone}\nКоментар: {your_text}\n")

        send_mail(
            'Паціент ' + your_name,
            appointment_body,
            your_email,
            ['victorkosmenuk@gmail.com'],
        )

        return render(request, 'website/success_appointment.html',
                      {'your_name': your_name,
                       'your_phone': your_phone,
                       "your_email": your_email,
                       "your_text": your_text})
    else:
        return render(request, 'website/home.html', {})


def diagnose_methods(request):
    return render(request, 'website/diagnose_methods.html', {})


def healing_methods(request):
    return render(request, 'website/healing_methods.html', {})


def quick_methods(request):
    return render(request, 'website/quick_methods.html', {})


def aesthetic_gynecology(request):
    return render(request,
                  'website/quick methods templ/aesthetic gynecology_temp.html',
                  {})


def hysteroscopy(request):
    return render(request,
                  'website/quick methods templ/hysteroscopy_temp.html', {})


def laparatomy(request):
    return render(request, 'website/quick methods templ/laparatomy_temp.html',
                  {})


def laparoscopy(request):
    return render(request, 'website/quick methods templ/laparoscopy_temp.html',
                  {})


def radio_wave_treatment(request):
    return render(request,
                  'website/quick methods templ/radio wave treatment_temp.html',
                  {})


def vaginoplastiki(request):
    return render(request,
                  'website/quick methods templ/rezultaty-vaginoplastiki-shematichno_temp.html',
                  {})


def urinary_incontinence(request):
    return render(request,
                  'website/quick methods templ/urinary incontinence_temp.html',
                  {})


def vulvectomy(request):
    return render(request, 'website/quick methods templ/vulvectomy_temp.html',
                  {})


def colposcopy(request):
    return render(request,
                  'website/diagnose methods templ/colposcopy_templ.html', {})


def office_hysteroscopy(request):
    return render(request,
                  'website/diagnose methods templ/office_hysteroscopy_templ.html',
                  {})


def HPV_treatment(request):
    return render(request,
                  'website/healing methods templ/HPV_treatment_templ.html', {})


def postanovka_MVS(request):
    return render(request,
                  'website/healing methods templ/postanovka_MVS_templ.html',
                  {})


def treatment_infections(request):
    return render(request,
                  'website/healing methods templ/treatment_infections_templ.html',
                  {})
