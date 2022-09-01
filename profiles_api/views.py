from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APUView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over yout application logic',
            'Is mapped manueally to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
