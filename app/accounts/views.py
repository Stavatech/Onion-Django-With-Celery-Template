from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class AccountDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        return Response("Hello {id}".format(id=id))
