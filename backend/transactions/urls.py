from django.urls import path
from .views import TransactionDetail, TransactionList, dashboard_summary, simulate_transaction

urlpatterns = [path("transactions", TransactionList.as_view()), path("transactions/<int:pk>", TransactionDetail.as_view()), path("transactions/simulate", simulate_transaction), path("dashboard/summary", dashboard_summary)]
