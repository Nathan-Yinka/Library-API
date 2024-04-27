from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

class EndpointList(APIView):
    """
    View to list all available endpoints in the 'library' app.
    """

    def get(self, request, format=None):
        endpoint_urls = {
            "get_books": request.build_absolute_uri(reverse("book-list-create")),
            "get_all_categories": request.build_absolute_uri(reverse('category-list-create'))
        }

        return Response(endpoint_urls)
