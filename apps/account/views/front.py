from django.views.generic import TemplateView


class AuthView(TemplateView):
    template_name = 'account/auth.html'

