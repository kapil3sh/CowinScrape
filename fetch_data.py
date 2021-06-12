import requests
import json

from requests.models import parse_header_links

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

def get_data(pin,date):
    req = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pin+"&date="+date,headers=headers)
    data = req.json()
    val = req.text
    if "Invalid Pincode" in val:
        return "invalid pincode"
    else :
        centers = data["centers"]
        if (len(centers)>0):
            all_data = []
            for center in centers:
                sessions = center["sessions"]
                for session in sessions:
                    all_data.append({"center_name":center["name"],
                    "center_address":center["address"],
                    "center_pincode":center["pincode"],
                    "date":session["date"],
                    "age_limit":session["min_age_limit"],
                    "available_capacity_dose1":session["available_capacity_dose1"],
                    "available_capacity_dose2":session["available_capacity_dose2"],
                    "vaccine":session["vaccine"],
                    "slots":session["slots"]})
            return(all_data)
                     

