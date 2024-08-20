import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def default(request):
    return Response({
                        "status": "success",
                        "message": "server is running",
                    }, status=200)

@csrf_exempt
@api_view(['POST'])
def search_course(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            query = data.get('query')
            encoded_query = requests.utils.quote(query)

            # First API call to search for courses
            search_url = "https://course-finder-using-react-node-backend.vercel.app/search-course"
            search_headers = {
                "accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",  # Ensure the content type is set correctly
            }

            # Prepare the request body
            search_body = json.dumps({"query": encoded_query})  # Make sure to include the query in the body

            # Make the POST request
            search_response = requests.post(search_url, headers=search_headers, data=search_body)
            return Response(search_response.json(), status=200)
        else:
            return Response({
                "status": "error",
                "message": "Invalid request method.",
            }, status=405)
    except Exception as e:
        return Response({
            "status": "error",
            "message": "Internal Server Error",
            "details": str(e),
        }, status=500)
