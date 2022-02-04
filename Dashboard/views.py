from django.shortcuts import render


from django.shortcuts import render
from django.views import View

class DashboardHomeView(View):

    def get(self, request, *args, **kwargs):
        template = 'dashboard/dashboard_home.html'
        context = {

        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        pass

