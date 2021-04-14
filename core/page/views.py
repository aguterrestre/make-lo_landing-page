from django.contrib.auth.views import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.template.loader import get_template

from config import settings


class LandingPage(TemplateView):
    """ Vista para visualizar un template de Landing Page """
    template_name = 'landing_page.html'

    def send_email(self, name, email, phone, message):
        """ Metodo para enviar correo electrónico """
        data = {}
        try:
            # Genero el contexto
            context = {'name': name, 'email': email, 'phone': phone, 'message': message}
            # Defino el template a enviar por mail
            template = get_template('send_email.html')
            # Defino el contenido que será enviado por mail
            content = template.render(context)
            # Defino asunto del mail a enviar
            subject = (f'Prueba solicitada - {name}')
            # Defino el correo electrónico del usuario
            email_landing_page = 'aguterrestre@gmail.com'
            # Defino el correo a enviar
            email = EmailMultiAlternatives(
                subject,
                '',
                settings.EMAIL_HOST_USER,
                [email_landing_page]
            )
            # Agrego al mail a enviar el contenido
            email.attach_alternative(content, 'text/html')
            # Envío el mail
            email.send()
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        """ Usamos método POST para enviar mail de contacto """
        data = {}
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            self.send_email(name, email, phone, message)
        except Exception as e:
            data['error'] = 'Ha ocurrido un inconveniente al intentar enviar la solicitud.\n'+str(e)
        return JsonResponse(data, safe=False)
