
import requests
from bs4 import BeautifulSoup

listHolder = []
states = ["WASHINGTON", "COLORADO", "NEW MEXICO"]
states = ["NEW MEXICO", "MAINE"]
URL_base = "https://www.nass.usda.gov/Quick_Stats/Ag_Overview/stateOverview.php?state="

for state in states:
    URL_full = URL_base + state
    page = requests.get(URL_full)
    soup = BeautifulSoup(page.content, "html.parser")

    def removeCommas(input):
        if input == "":
            return("0")
        else:
            return(input.replace(",",""))

    for tableRow in soup.find_all("tr", class_="datarow"):
        commodity = tableRow.find_all('td')[0].text
        plantedAPAcres = removeCommas(tableRow.find_all('td')[1].text)
        harvestedAcres = removeCommas(tableRow.find_all('td')[2].text)
        cropYield = tableRow.find_all('td')[3].text
        production = tableRow.find_all('td')[4].text
        pricePerUnit = tableRow.find_all('td')[5].text
        productionValueDollars = tableRow.find_all('td')[6].text
        listHolder.append({"State": state,
        "Commodity": commodity,
        "plantedAllPurposeAcres": plantedAPAcres,
        "harvestedAcres": harvestedAcres,
        "cropYield": cropYield,
        "production": production,
        "pricePerUnit": pricePerUnit,
        "productionValueDollars": productionValueDollars})

#print(listHolder)

with open("/Users/geoffreyhouse/GitHub/usda-map-ag-stats/USDA_agStats_stateOverviews_scraper_results.txt", "w") as outFile:
    outFile.write("State\tCommodity\tplantedAllPurposeAcres\tharvestedAcres\tcropYield\tproduction\tpricePerUnit\tproductionValueDollars\n")
    for rowDict in listHolder:
        lineHolder = ""
        for key in rowDict:
            #print(key)
            lineHolder += rowDict[key].strip() + "\t"
        lineHolder += "\n"
        
        outFile.write(lineHolder)




      

