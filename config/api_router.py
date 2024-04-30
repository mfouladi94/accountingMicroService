from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from django.urls import include
from django.urls import path
from accountingmicroservice.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [

    path("wallets/", include("accountingmicroservice.wallet.urls")),
    path("transactions/", include("accountingmicroservice.ptransactions.urls")),

]
