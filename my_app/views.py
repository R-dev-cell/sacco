from django.shortcuts import render

def index_view(request):
        return render(request, 'index.html')

def saving_view(request):
        return render(request, 'saving.html')

def member_view(request):
        return render(request, 'member.html')
