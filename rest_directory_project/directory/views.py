from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from directory import USERS, KEYS

class UserViewSet(APIView):

    def get(self, request):
        if request.method == 'GET':
            return Response(status=status.HTTP_200_OK, data=USERS)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetUserViewSet(APIView):
    def get(self, request, name):
        if request.method == 'GET':
            try:
                index = next(i for (i, d) in enumerate(USERS) if d['name'] == name)
                return Response(status=status.HTTP_200_OK, data=USERS[index])
            except StopIteration as e:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
