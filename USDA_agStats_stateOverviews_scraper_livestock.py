
import requests
from bs4 import BeautifulSoup

# This scrapes the livestock information from the top tables of each page.

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

with open("/Users/geoffreyhouse/GitHub/usda-map-ag-stats/USDA_agStats_stateOverviews_scraper_results_livestock.txt", "a") as outFile:
        outFile.write("state\tfarmLabel\tfarmValue\n")

for state in states:
    print(state)
    URL_full = URL_base + state
    page = requests.get(URL_full)
    soup = BeautifulSoup(page.content, "html.parser")

    
    headings = [entry1.text for entry1 in soup.find_all(class_="firstColumn")]
    values = [removeCommas(entry2.text) for entry2 in soup.find_all(class_="secondColumn")]

    print(headings)
    print(values)

    # zip the headings and values together into a list of paired tuples
    zippedEntries = zip(headings, values)

    # open file in append mode (creates if not already existing)
    with open("/Users/geoffreyhouse/GitHub/usda-map-ag-stats/USDA_agStats_stateOverviews_scraper_results_livestock.txt", "a") as outFile:
        for entry in zippedEntries:
            outFile.write(state + "\t" + entry[0] + "\t" + entry[1] + "\n")


    




      

