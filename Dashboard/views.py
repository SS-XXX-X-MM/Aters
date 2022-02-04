from django.shortcuts import render
from django.views.generic import View

class DashboardHomeView(View):
    template = 'dashboard/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        pass

