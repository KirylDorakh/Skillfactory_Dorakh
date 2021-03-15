from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.core.mail import EmailMultiAlternatives # импортируем класс для создание объекта письма с html
from .models import Appointment
from django.core.mail import mail_admins

from django.template.loader import render_to_string # импортируем функцию, которая срендерит наш html в текст
from .models import Appointment

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # получем наш html
        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )
        # отправляем письмо
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            body=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='kirill.dorokh@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            to=['kirill.dorokh@gmail.com']  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()

        mail_admins(
            subject=f'{appointment.client_name} {appointment.date.strftime("%d %m %Y")}',
            message=appointment.message,
        )

        return redirect('make_appointment')
