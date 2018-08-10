from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

@login_required
def index(request):
	return render(request, 'chat/index.html', {})

