from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:thanks')
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            mail = form.cleaned_data['mail']
            message = (
                f'Здравствуйте, {name}! '
                'Вы получили это письмо, так как написали в Cats Company.\n'
                f'Ваш отзыв:\n{text}\n\n'
                'Спасибо за обратную связь! Мы обязательно учтем ваше мнение.\n'
                '© Cats Company'
            )

            send_mail(
                'Cats company',
                message,
                settings.ADMIN_EMAIL,
                [mail],
                fail_silently=False,
            )

            self.model.objects.create(**form.cleaned_data)
            return redirect('feedback:thanks')

        return render(request, self.template_name)


def redirect_thanks(request):
    template = "feedback/thanks.html"
    context = {}
    return render(request, template, context)
