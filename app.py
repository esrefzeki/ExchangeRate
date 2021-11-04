import xml.etree.ElementTree as ET
from urllib.request import urlopen
import requests


url = "https://www.tcmb.gov.tr/kurlar/today.xml"
resp = requests.get(url=url)
# print(resp.text)

tree = ET.parse(urlopen(url))
root = tree.getroot()

liste = [root.findall("Currency")]

for i in liste[0]:
    currencyCode = i.get('Kod')
    banknoteBuying = i.find("BanknoteBuying").text
    banknoteSelling = i.find("BanknoteSelling").text

    if currencyCode =="USD":
        result = float(banknoteSelling) - float(banknoteBuying)
        print("USD ", banknoteSelling)
        print("USD ", banknoteSelling)
        print("Banka alış satış arasındaki kur farkı ->", "%.5s" % str(result))

    if currencyCode =="EUR":
        result = float(banknoteSelling) - float(banknoteBuying)
        print("EUR ", banknoteSelling)
        print("EUR ", banknoteSelling)
        print("Banka alış satış arasındaki kur farkı ->", "%.5s" % str(result))


