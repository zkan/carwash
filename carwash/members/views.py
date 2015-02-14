from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import MemberForm


class MemberAddView(TemplateView):
    form_class = MemberForm
    template = 'member_add.html'

    def get(self, request):
        form = self.form_class()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )
