from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class UserViewSet(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request):
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

        return Response(
            data=users
        )