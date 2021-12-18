
import requests
from bs4 import BeautifulSoup

# This scrapes the crop information from the bottom tables on each page.

listHolder = []
states = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", \
        "CONNECTICUT", "DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", \
        "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", \
        "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", \
        "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", \
        "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", \
        "RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", \
        "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
#states = ["NEW MEXICO", "MAINE"]
URL_base = "https://www.nass.usda.gov/Quick_Stats/Ag_Overview/stateOverview.php?state="

def removeCommas(input):
        if input == "":
            return("0")
        else:
            return(input.replace(",",""))


for state in states:
    print(state)
    URL_full = URL_base + state
    page = requests.get(URL_full)
    soup = BeautifulSoup(page.content, "html.parser")

    
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

with open("/Users/geoffreyhouse/GitHub/usda-map-ag-stats/USDA_agStats_stateOverviews_scraper_results_full.txt", "w") as outFile:
    outFile.write("State\tCommodity\tplantedAllPurposeAcres\tharvestedAcres\tcropYield\tproduction\tpricePerUnit\tproductionValueDollars\n")
    for rowDict in listHolder:
        lineHolder = ""
        for key in rowDict:
            #print(key)
            lineHolder += rowDict[key].strip() + "\t"
        lineHolder += "\n"
        
        outFile.write(lineHolder)




      

