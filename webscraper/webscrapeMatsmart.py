import requests
import pprint as pp
import csv

import pathlib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

url1 = 'https://www.matsmart.se/proteinprodukter'
xpathPrice = "//div[@class='product-item-price']//span[@class='product-price-title']"
xpathName = "//div[@class='product-grid-item-container product-grid-item-label-header']//span[@class='label']"
xpathMultiPrice = "//div[@class='product-item-price']//span[@class='product-item-multi-price-label']"

xpathShort = "//div[@class='product-item-price']//div[@property='offers']"


# getProducts() RETURNS A LIST OF matsmartItem WHICH ARE ALL PROTEINS

class matsmartItem:
    def __init__(self, name, price, mult=1):
        self.name = name
        self.price = price
        self.mult = mult


def __CHROMEDRIVER_PATH():
    filepath = pathlib.Path(__file__).parent.absolute()
    CHROMEDRIVER_PATH = str(filepath) + '/chromedriver.exe'
    return CHROMEDRIVER_PATH


def __initWebDriver():
    driver = webdriver.Chrome(
        executable_path=__CHROMEDRIVER_PATH())
    return driver


def numberOfItems():
    driver = __initWebDriver()
    driver.get(url1)
    elements = driver.find_elements_by_xpath(xpathPrice)
    numberOfItems = len(elements)
    driver.close
    return numberOfItems


def allPrices():

    # Want to get:
    # * Name of product
    # * Price of product
    # * Eventual "3 för"

    pass


def getProducts():
    driver1 = __initWebDriver()
    driver1.get(url1)
    elementsPrice = driver1.find_elements_by_xpath(xpathPrice)
    elementsName = driver1.find_elements_by_xpath(xpathName)

    elementsMulti = driver1.find_elements_by_xpath(xpathMultiPrice)
    reversedMulti = reversed(elementsMulti)

    multiIndexes = getIndexesOfMultiDeal()
    multiValues = getMultiPriceCool()

    numberOfItems = 0

    if(len(elementsName) == len(elementsPrice)):
        numberOfItems = len(elementsName)
    else:
        return ValueError

    listOfItems = []

    for i in range(numberOfItems):
        itemName = elementsName[i].text
        itemPrice = int(elementsPrice[i].text)
        if(i in multiIndexes):
            item = matsmartItem(itemName, itemPrice, multiValues.pop())
        else:
            item = matsmartItem(itemName, itemPrice)
        listOfItems.append(item)

        print(item.name + '\n' + str(item.price) + '\n' + str(item.mult))

    driver1.close()

    return listOfItems


def getNumberOfMultis():
    # getProducts()

    driver1 = __initWebDriver()
    driver1.get(url1)
    elementsPrice = driver1.find_elements_by_xpath(xpathMultiPrice)

    print(len(elementsPrice))
    driver1.close()

    # Get multis into list
    # Reverse list
    # Count number of children for item
    # If count is 3 instead of 2, pop from list and put into the thing


# getProducts()
def getIndexesOfMultiDeal():
    driver1 = __initWebDriver()
    driver1.get(url1)
    elements = driver1.find_elements_by_xpath(xpathShort)

    listOfIndexes = []

    for index, element in enumerate(elements):
        if("product-item-multi-price-wrapper" in element.get_attribute("class")):
            listOfIndexes.append(index)
    driver1.close()
    return listOfIndexes


def getMultiPriceCool():
    driver1 = __initWebDriver()
    driver1.get(url1)
    elementsMulti = driver1.find_elements_by_xpath(xpathMultiPrice)
    reversedList = []
    for i in elementsMulti:
        reversedList.append(int(i.text[0]))

    driver1.close()
    reversedList.reverse()
    return reversedList
