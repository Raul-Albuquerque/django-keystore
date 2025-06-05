from django.contrib import admin
from django.urls import path
from keystore.views import (
    KvstoreListView,
    KvstoreCreateView,
    KvstoreUpdateView,
    KvstoreDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", KvstoreListView.as_view(), name="kvstore_list"),
    path("create", KvstoreCreateView.as_view(), name="kvstore_create"),
    path("update/<int:pk>", KvstoreUpdateView.as_view(), name="kvstore_update"),
    path("delete/<int:pk>", KvstoreDeleteView.as_view(), name="kvstore_delete"),
]
