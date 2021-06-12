import smtplib
import json
from fetch_data import get_data
with smtplib.SMTP('smtp.gmail.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("kapileshk1230@gmail.com", "kapileshk1993@123")

    pins = ["400018","400028"]
    all_data_all = []

    for pin in pins:
        appt = get_data(pin,"06-06-2021")
        all_data_all.append(appt)

    data_parser = json.dumps(all_data_all)
    data_parser = data_parser.replace("{","")
    data_parser = data_parser.replace("}","\n\n")
    data_parser = data_parser.replace("[","")
    data_parser = data_parser.replace("]","")
    data_parser = data_parser.replace(",","\n")

    print(type(data_parser))

    """
    subject = 'COVID-TEST_EMAIL'
    body = data_parser

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail("kapileshk1230@gmail.com","dramrutaa9@gmail.com", msg)
    smtp.sendmail("kapileshk1230@gmail.com","kapileshkothavale@gmail.com", msg) """