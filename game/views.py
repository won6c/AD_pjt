from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DoomPlayRecord
from django.utils.timezone import now, timedelta
import json

def doom_embed_view(request):
    return render(request, 'game/doom.html')

# game/views.py


@csrf_exempt
def record_doom_play(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        duration = data.get("duration", 0)
        score = data.get("score", 0)

        DoomPlayRecord.objects.create(
            user=request.user,
            start_time=now() - timedelta(seconds=duration),
            end_time=now(),
            duration=duration,
            score=score
        )
        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "unauthorized"}, status=403)
