from django.shortcuts import render
from journal.models import Note
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.

@login_required
def write(request):
    return render(request, 'journal/index.html')

@login_required
def note_list(request):
    notes = serializers.serialize("json", Note.objects.all().filter(user=request.user))
    return JsonResponse(notes, safe=False)

@login_required
def note_update(request, id):
    if request.method == "PUT":
         print(request)
         note = Note.objects.all().get(id=id)
         data = json.loads(request.body)
         note.content = data['fields']['content']
         note.save()
         return JsonResponse('ok', safe=False)

@login_required
def note_create(request):
    if request.method == "POST":

        data = json.loads(request.body)
        note = Note(content=data['fields']['content'], word_count=data['fields']['word_count'], pub_date=data['fields']['pub_date'], user=request.user)
        note.save()
        return JsonResponse({ 'result': 'OK', 'note': note.content }, status=200)
        
         