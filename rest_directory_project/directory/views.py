from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(APIView):

    def get(self, request):
        if request.method == 'GET':
            users = [
                {
                    'name': 'victor',
                    'telephone': '1122',
                    'project': 'beeva'
                },
                {
                    'name': 'nany',
                    'telephone': '2211',
                    'project': 'beeva'
                },
                {
                    'name': 'javi',
                    'telephone': '3311',
                    'project': 'beeva'
                }
            ]

            return Response(status=status.HTTP_200_OK, data=users)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
