from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Film


def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

@csrf_exempt
def film_api_view(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return JsonResponse({"error": "film not found"}, status=404)
    
    if request.method == 'GET':
        return JsonResponse(film.to_dict())
    elif request.method == 'POST':
        return JsonResponse(film.to_dict())
    elif request.method == 'PUT':
        return JsonResponse(film.to_dict())
    elif request.method == 'DELETE':
        film.delete()
        return JsonResponse({"message": "Film was deleted from database successfully"})
    else:
        return JsonResponse({"message": "this method is not allowed"}, status=405)

@csrf_exempt
def films_api_view(request):
    if request.method == 'GET':
        return JsonResponse({
            'films': [
                film.to_dict() for film in Film.objects.all()
            ]
        })
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)

            new_film = Film(
                title = data['title'],
                description = data['description'],
                release_date = data['release_date'],
                box_office = data['box_office']
            )

            new_film.save()

            return JsonResponse({"message": "Film was added to database successfully"})
        except Exception as e:
            return JsonResponse({"error": "Error occured while adding new film"}, status=400)
    else:
        return JsonResponse({'error': 'errrooooorrrrrr'})
