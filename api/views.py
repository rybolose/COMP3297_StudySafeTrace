from datetime import timedelta, datetime

import requests
from django.shortcuts import render


# Create your views here.
def load_venue_data(request):
    hkuID = request.GET['HKU_ID']
    dateDiag = datetime.strptime(request.GET['Date_Of_Diagnosis'], "%Y-%m-%d")
    dateDiag = dateDiag.strftime("%Y-%m-%d")
    disinfectURL = f"https://immense-scrubland-01353.herokuapp.com/disinfectvenues/?HKU_ID={hkuID}&Date_Of_Diagnosis={dateDiag}"
    memberURL = f'https://immense-scrubland-01353.herokuapp.com/members/{hkuID}'

    member = requests.get(memberURL).json()
    disinfect_venues_json = requests.get(disinfectURL).json()

    disinfect_venues = list()

    for venue in disinfect_venues_json:
        id = venue['Venue_Code']
        disinfect_venues.append(id)

    context = {
        "subject": member["Name"],
        "date": dateDiag,
        "venues": disinfect_venues
    }
    return render(request, 'venues.html', context=context)


def load_close_contact_list(request):
    hkuID = request.GET['HKU_ID']
    dateDiag = datetime.strptime(request.GET['Date_Of_Diagnosis'], "%Y-%m-%d")
    dateDiag = dateDiag.strftime("%Y-%m-%d")
    closecontactsURL = f'https://immense-scrubland-01353.herokuapp.com/closecontacts/?HKU_ID={hkuID}&Date_Of_Diagnosis={dateDiag}'
    memberURL = f'https://immense-scrubland-01353.herokuapp.com/members/{hkuID}'
    member = requests.get(memberURL).json()
    close_contact = requests.get(closecontactsURL).json()
    close_contact_list = []

    for contact in close_contact:
        id = contact['HKU_ID']
        name = contact['Name']
        close_contact_list.append(id + ":" + name)

    context = {
        "subject": member["Name"],
        "date": dateDiag,
        "contacts": close_contact_list
    }
    return render(request, 'contacts.html', context=context)
