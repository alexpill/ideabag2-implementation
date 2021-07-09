#!/usr/bin/env python3

""" Extract countries vs taxes from Wikipedia scrapping, and export to JSON """

from bs4 import BeautifulSoup
import requests
import json

def extract_taxes():
    req = requests.get("https://en.wikipedia.org/wiki/Value-added_tax")
    soup = BeautifulSoup(req.text, features="html.parser")

    taxes = {}

    for table in soup.find_all("table", class_="wikitable")[:3]:
        for row in table.tbody("tr")[1:]:
            columns = row.find_all('td')
            country = columns[0].text.split("[")[0].strip() # get rid of Wikipedia refs
            vat = columns[1].text.split("[")[0].strip() # get rid of Wikipedia refs
            vat = vat.split("%")[0].split(" ")[-1] # get rid of '%' and take first percentage
            try: # convert to float or 0.0
                vat = float(vat)
            except:
                vat = "unknown or free"
            taxes[country] = vat

    return taxes

def main():
    taxes = extract_taxes()
    # [print(f"{i}\t{taxes[i]}") for i in taxes]
    with open("taxes.json", "w") as json_file:
        json.dump(taxes, json_file, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()
