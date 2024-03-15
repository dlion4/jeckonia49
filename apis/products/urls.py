from django.urls import path, include

urlpatterns = [
    path("drf/", include("apis.products.restapi.urls")),
    path("ninja/", include("apis.products.ninja.urls")),
]
