from django.shortcuts import render
from IPLteam.forms import teamForm
from IPLteam.models import team

# Create your views here.
def home_view(request):
    return render(request, 'IPLteam/home.html')

def addTeam_view(request):
    form = teamForm()
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            form.save()
            print('Team data inserted into database successfully!!!!')
    return render(request, 'IPLteam/add.html', context = {'form':form})

def displayTeam_view(request):
    team_list = team.objects.all()
    return render(request, 'IPLteam/display.html',{'team_list':team_list})
