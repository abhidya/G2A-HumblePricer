from requests import Session
from robobrowser import RoboBrowser
import useragents
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
print("Starting Session")
c = Session()
c.verify = False
browser = RoboBrowser(session=c, user_agent=useragents.random(), parser="html.parser")
humblebundle_link = input("Paste your humblebundle link here: ")
total = 0
browser.open(humblebundle_link)
games = browser.find_all("div", {"class": """dd-image-box-caption dd-image-box-text dd-image-box-white """})
with open('G2A_Save.txt', 'a') as file:
    file.write('\n'+'\n'+ "------------------------------------" + humblebundle_link + '\n'+'\n')
    file.close()
for game in games:
    try:
        response = game.get_text()
        response = ' '.join(response.split())
        browser.open("https://www.g2a.com/en-us/search?query="+response+"&sort=price-lowest-first")
        results = browser.find("span", {"class": "Card__price-cost price"})
        results = results.get_text()
        results_money = results.split()
        results_money = results[0]
        results_money = float(results_money)
        total = results_money + total
        with open('G2A_Save.txt', 'a') as file:
            file.write(str(response + " : " + results))
            file.close()
        print(response + " : " + results+ '\n')
    except AttributeError:
        print(response + " : Doesn't exist on G2A")
print('\n'+'\n'+ "TOTAL VALUE IF SOLD  " + str(total)  )
with open('G2A_Save.txt', 'a') as file:
    file.write('\n'+'\n'+ "TOTAL VALUE IF SOLD  " + str(total) + "------------------------------------" + '\n'+'\n')
    file.close()
pres = input("Press any button to exit")
