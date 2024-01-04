from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.utils.html import escape

from solo.forms import BasicForm

class SoloView(LoginRequiredMixin, View):
    template_name = 'solo/index.html'
    success_url = reverse_lazy('solo:index')

    def get(self, request):
        result = request.session.get('solo_result', False)
        if result: del request.session['solo_result']
        form = BasicForm()
        context = {"form": form, "result": result}
        return render(request, self.template_name, context)
    
    def post(self, request):
        field1 = request.POST.get("field1", "")
        field2 = request.POST.get("field2", "")
        result = " ".join([field1.strip(), field2.strip()]).upper()
        request.session['solo_result'] = escape(result)
        return redirect(request.path)
