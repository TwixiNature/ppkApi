#from . import itemToData as i2d
from webscraper import webscrapeGymgrossisten as wsg
from webscraper import webscrapeMatsmart as wsm
import json


class proteinProduct:
    def __init__(self, name, desc='', proteinPercentage=0, proteinPerItem=0, price=0, ppk=0, itemsInBatch=0, site=''):
        self.name = name
        self.description = desc
        self.priceTotal = priceTotal
        self.proteinPercentage = proteinPercentage
        self.proteinPerItem = proteinPerItem
        self.itemsInBatch = itemsInBatch
        self.proteinTotal = self.ItemsInBatch * self.proteinPerItem
        self.ppk = self.proteinTotal / self.priceTotal
        self.site = site

        # ppk = proteinTotal / priceTotal
        # ProteinTotal = ItemsInBatch * proteinPerItem

        # * Name, Description(desc, proteininnehåll, jämför med gainomax bar), price, protein per krona


def ppk():
    pass


def wsgToJson():
    jsona = json.dumps([vars(item) for item in wsg.getProducts()], indent=4)
    f = open("data/gymgrossisten.json", "w")
    f.write(jsona)
    f.close()


def wsmToJson():
    jsona = json.dumps([vars(item) for item in wsm.getProducts()], indent=4)
    f = open("data/matsmart.json", "w")
    f.write(jsona)
    f.close()


def bigFunc():
    pass
    # WHAT WE WANT:
    # * pull json (A)
    # * pull scrape (B)
    # * Turn all in A which is in B "active". All in A which is not in B "inactive"
    # * All in B which are not in A, write to file with basic values

    # WHAT INFORMATION DO WE WANT IN BIG FILE:
    # * Name, Description(desc, proteininnehåll, jämför med gainomax bar), price, protein per krona
