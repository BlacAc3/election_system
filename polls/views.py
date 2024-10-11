from django.shortcuts import render
from .models import Agentname, AnnouncedLgaResults, AnnouncedPuResults, AnnouncedWardResults, AnnouncedStateResults, Lga, Party, PollingUnit, States, Ward 

# Create your views here.
def index(request):
    polling_units = PollingUnit.objects.all() 
    return render(request, 'polls/index.html', {
        "polling_units":polling_units,

        })

def get_pu_result(request, pu_unique_id):
    pu_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pu_unique_id)
    return render(request, "polls/index.html", {
        "pu_results":pu_results,

        })

def get_lga(request):
    lga = Lga.objects.all()
    return render(request, "polls/lga_results.html", {
        "lga":lga,

        })

def get_lga_result(request):
    lga = Lga.objects.all()
    lga_id = request.POST.get('lga_id')
    polling_units = PollingUnit.objects.filter(lga_id=lga_id)
    lga_calc_results={}
    for unit in polling_units:
        announced_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit.uniqueid)
        for result in announced_result:
            key = result.party_abbreviation
            value = result.party_score
            if key in lga_calc_results:
                lga_calc_results[key] += value  # Add value to existing key
            else:
                lga_calc_results[key] = value 
    return render(request, "polls/lga_results.html", {
        "lga_results":lga_calc_results,
        "lga":lga
        })

def new_polling_unit(request):
    parties = Party.objects.all()
    wards = Ward.objects.all()
    lga = Lga.objects.all()
    return render(request, "polls/addscores.html", {
        "parties":parties,
        "wards":wards,
        "lgas":lga
        })

def create_polling_unit(request):
    if request.method == "POST":
        parties = Party.objects.all()
        polling_unit = PollingUnit.objects.create(
            polling_unit_id=request.POST.get('polling_unit_id'),
            ward_id=request.POST.get('ward_id'),
            lga_id=request.POST.get('lga_id'),
            polling_unit_name=request.POST.get('polling_unit_name'),
            # Add more fields as necessary
            entered_by_user=request.POST.get('entered_by_user'),
            date_entered=request.POST.get('date_entered'),
            user_ip_address=request.POST.get('user_ip_address'),
        )
        polling_unit.save()
        for party in parties:
            if request.POST.get(f'party_{party.partyid}'):
                result = AnnouncedPuResults.objects.create(
                    polling_unit_uniqueid =polling_unit.uniqueid,
                    party_abbreviation = party.partyname,
                    party_score = request.POST.get(f'party_{party.partyid}'),
                    entered_by_user = request.POST.get('entered_by_user'),
                    date_entered = request.POST.get('date_entered'),
                    user_ip_address = request.POST.get('user_ip_address'),
                )   
                result.save()

        return new_polling_unit(request)
