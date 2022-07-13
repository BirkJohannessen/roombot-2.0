import mysql.connector as mysql
import pip._vendor.requests as requests
import datetime
import time
import base64
from bs4 import BeautifulSoup as soup


def login(urlLogin, session, bruker, passord):

    urlSSO = "https://cloud.timeedit.net/hvl/web/timeedit/ssoResponse"
    payload = {
        'has_js': '0',
        'inside_iframe': '0',
        'feidename':  bruker,
        'password': passord
    }

    responseTE = session.post(urlLogin, data=payload)
    if "Du må logge deg på via Feide for å få tilgang til TimeEdit - HVL" in responseTE.text:
        print("pålogging mislykkes")
    #<input type="hidden" name="SAMLResponse" value="PHN
    SAMLResponse=""
    try:
        SAMLResponse = soup(responseTE.text, 'html.parser').find('input', {'name': 'SAMLResponse'}).get('value')
    except Exception as e:
        print("Got unhandled exception %s" % str(e))
    payloadSSOResponse = {
        'SAMLResponse': SAMLResponse,
        'RelayState': ''
    }

    responseTE = session.post(urlSSO, data=payloadSSOResponse)
    if not " <title>TimeEdit Høgskulen på Vestlandet</title>" in responseTE.text:
        print(responseTE.text)
    else:
        print("Cookie satt til timeedit!")

def Book(date, tidStart, tidSlutt, romID, bruker, passord):
    urlLoginMedFeide = "https://cloud.timeedit.net/hvl/web/timeedit/sso/feide?back=https%3A%2F%2Fcloud.timeedit.net%2Fhvl%2Fweb%2Fstudbergen%2F"
    urlBook = "https://cloud.timeedit.net/hvl/web/studbergen/ri1Q9.html"
    payloadBook = {
        'kind': 'reserve',
        'nocache': '4',
        'l': 'nb_NO',
        'o': romID + '.22',
        'aos': '',
        'dates': date,
        'starttime': tidStart,
        'endtime': tidSlutt,
        'url': 'https://cloud.timeedit.net/hvl/web/studbergen/ri1Q9.html#00' + romID,
        'fe3': ''
    }

    session = requests.Session()
    responseFEIDE = session.get(urlLoginMedFeide)
    login(responseFEIDE.url, session, bruker, passord)
    response = session.post(urlBook, data=payloadBook)
    if len(response.text)<500:
        print(response.text)
    else:
        print("uforventet feil i reservasjon .. ")



def makeDate():
    today = datetime.date.today()
    omTreDager = today + datetime.timedelta(days=3)
    return omTreDager.strftime("%Y%m%d")


def printDatabase():
    db = mysql.connect(
        host = "localhost",
        user = "<skjult>",
        passwd = "<skjult>",
        database= "<skjult>"
    )
    cursor = db.cursor()
    query = "SELECT * FROM aktivBooking"
    cursor.execute(query)
    records = cursor.fetchall()
    print("started roombot at-", datetime.datetime.now())
    time.sleep(1)
    for record in records:
        print("######exec for "+record[4]+record[5]+record[1]+record[2]+record[3])
        print("time-", datetime.datetime.now())
        Book(makeDate(), record[4], record[5], record[1], record[2], base64.b64decode(record[3]))
        if "enkel" == record[6]:
            print("deleting entry from DB ...")
            cursor.execute("DELETE FROM aktivBooking WHERE id="+str(record[0]))
            db.commit()
    cursor.close()
    db.close()
    print("finished roombot at-", datetime.datetime.now())


if __name__ == "__main__":
    printDatabase()