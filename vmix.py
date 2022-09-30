import requests
import bs4
import datetime


def Main():
     
    url_vmix = "http://127.0.0.1:8088/api"
    url_code = requests.get(url_vmix)
    soup = bs4.BeautifulSoup(url_code.text, "lxml") 
    dt = datetime.datetime.now()

    """____reading vMix xml atributs____"""
    version_vmix = soup.find_all('version')
    overlay_vmix = soup.find_all("overlay")
    input_vmix = soup.find_all('input')
    pgm_vmix = soup.find_all("active")
    preview_vmix = soup.find_all('preview')
    edition_vmix = soup.find_all("edition")
    recording_vmix = soup.find_all('recording')
    audio_vmix = soup.find_all("audio")
    external_vmix = soup.find_all("external")
            

            # print(version_vmix)
            # print(overlay_vmix)
            # print(len(overlay_vmix))
            # print(len(input_vmix))
    d = {}
    for input in input_vmix:

        try:
            d[input['number']] = input['title']
        except:
            pass

        """Search input on overlay vMix"""
    for overlay_in in overlay_vmix:

        try:
            if overlay_in.get_text() != '' and overlay_in['preview'] == 'True':
                print(str(dt) + "\n"+ "Input: " + d[overlay_in.get_text()] + " on preview overlay, number " + overlay_in['number'])
        except KeyError:
            print(str(dt) + "\n" + "Input: " + d[overlay_in.get_text()] + " on pgm overlay, number " + overlay_in['number'])

            # print("\n" + "Preview input - " + d[preview_vmix[0].text])
            # print("PGM input - " + d[pgm_vmix[0].text])

       
    PGM = d[pgm_vmix[0].text]
    PREVIEW = d[preview_vmix[0].text]
    return PGM, PREVIEW



        
