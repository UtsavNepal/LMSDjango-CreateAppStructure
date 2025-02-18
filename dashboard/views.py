from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import OverdueBorrowerSerializer
from .repositories import DashboardRepository
from .services import DashboardService


class DashboardView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """Inject Repository into Service"""
        dashboard_repo = DashboardRepository()
        dashboard_service = DashboardService(dashboard_repo)

        dashboard_data = dashboard_service.get_dashboard_data()
        return Response(dashboard_data)


class GetOverdueBorrowersView(APIView):
   
    permission_classes = [AllowAny]

    def get(self, request):
        dashboard_repo = DashboardRepository()
        service = DashboardService(dashboard_repo)

        overdue_borrowers = service.get_overdue_borrowers()
        serializer = OverdueBorrowerSerializer(overdue_borrowers, many=True)
        return Response(serializer.data)


class MailOverdueBorrowersView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request):
        dashboard_repo = DashboardRepository()
        service = DashboardService(dashboard_repo)

        service.email_get_overdue_borrowers()
        return Response({"message": "Emails sent to overdue borrowers"})
