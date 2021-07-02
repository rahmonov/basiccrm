from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView

from agents.forms import AgentForm, AgentUpdateForm
from django.views.generic import DetailView
from agents.forms import AgentForm

from agents.models import Agent
from users.models import User


class AgentListView(LoginRequiredMixin, View):
    def get(self, request):
        search_param = request.GET.get('q')
        agent_type = request.GET.get('type')
        queryset = Agent.objects.all()

        if request.user.is_business_owner():
            queryset = Agent.objects.filter(business_owner=request.user.businessowner)

        if search_param:
            queryset = queryset.filter(Q(user__username__icontains=search_param))

        paginator = Paginator(queryset.order_by('id'), 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'agents': page_obj.object_list,
            'page_obj': page_obj,
        }

        return render(request, 'agents/list.html', context)


class AgentCreateView(LoginRequiredMixin, View):

    def get(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(initial={'business_owner': business_owner})

        context = {
            'form': form
        }

        return render(request, 'agents/create.html', context)

    def post(self, request):
        business_owner = request.user.businessowner
        form = AgentForm(data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            with transaction.atomic():
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                region = form.cleaned_data['region']

                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password)
                )

                Agent.objects.create(
                    user=user,
                    business_owner=business_owner,
                    region=region
                )

                send_mail(
                    subject='Account Created',
                    message=f'An account was created for you in BasicCRM. '
                            f'Your username is {username} and your password is {password}',
                    from_email='jrahmonov2@gmail.com',
                    recipient_list=[user.email]
                )

            return redirect(reverse('agents:list'))
        else:
            return render(request, 'agents/create.html', context)


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    model = Agent
    context_object_name = "agent"
    success_url = reverse_lazy('agents:list')
    template_name = 'agents/delete_confirm.html'
    pk_url_kwarg = "id"


class AgentUpdateView(LoginRequiredMixin, View):

    def get(self, request, id):
        agent = Agent.objects.get(pk=id)
        data = {
            'username': agent.user.username,
            'first_name': agent.user.first_name,
            'last_name': agent.user.last_name,
            'email': agent.user.email,
            'region': agent.region,
        }

        form = AgentUpdateForm(data=data)

        context = {
            'form': form
        }

        return render(request, template_name='agents/update.html', context=context)

    def post(self, request, id):
        agent = Agent.objects.get(pk=id)
        user = agent.user

        form = AgentUpdateForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            region = form.cleaned_data['region']

            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            agent.user = user
            agent.region = region
            agent.save()

            return redirect('agents:list')
        else:
            return render(request, template_name='agents/update.html', context=context)

class AgentDetailView(DetailView, LoginRequiredMixin):
    model = Agent
    template_name = 'agents/agent-detail.html'
    context_object_name = 'agent'
    pk_url_kwarg = 'id'

