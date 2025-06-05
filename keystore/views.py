from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Keystore


class KvstoreListView(ListView):
    model = Keystore
    template_name = "kvstore_list.html"


class CaptureClientIPMixin:
    def form_valid(self, form):
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")

        form.instance.client_ip = ip

        return super().form_valid(form)


class KvstoreCreateView(CaptureClientIPMixin, CreateView):
    model = Keystore
    template_name = "kvstore_form.html"
    fields = ["key", "value"]
    success_url = reverse_lazy("kvstore_list")


class KvstoreUpdateView(CaptureClientIPMixin, UpdateView):
    model = Keystore
    fields = ["key", "value"]
    template_name = "kvstore_form.html"
    success_url = reverse_lazy("kvstore_list")


class KvstoreDeleteView(DeleteView):
    model = Keystore
    template_name = "kvstore_confirm_delete.html"
    success_url = reverse_lazy("kvstore_list")
