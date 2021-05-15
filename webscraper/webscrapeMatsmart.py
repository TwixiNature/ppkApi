import pathlib

from selenium import webdriver

url1 = 'https://www.matsmart.se/proteinprodukter'
xpathPrice = "//div[@class='product-item-price']//span[@class='product-price-title']"
xpathName = "//div[@class='product-grid-item-container product-grid-item-label-header']//span[@class='label']"
xpathMultiPrice = "//div[@class='product-item-price']//span[@class='product-item-multi-price-label']"

xpathShort = "//div[@class='product-item-price']//div[@property='offers']"


class matsmartItem:
    def __init__(self, name, price, mult=1):
        self.name = name
        self.price = price
        self.mult = mult


def __CHROMEDRIVER_PATH():
    """Calculates the path to Chromedriver.exe. Chromedriver.exe is expected
    to be found as file in the same folder as this file.

    Returns:
        [type]: [description]
    """
    filepath = pathlib.Path(__file__).parent.absolute()
    CHROMEDRIVER_PATH = str(filepath) + '/chromedriver.exe'
    return CHROMEDRIVER_PATH


def __initWebDriver():
    """Returns a configured webdriver

    Returns:
        [type]: [description]
    """
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


def getProducts():
    """Returns a list containing all protein-products on matsmart site.


    Returns:
        [matsmartItem]: List of matsmartItem.
    """
    driver1 = __initWebDriver()
    driver1.get(url1)

    elementsPrice = driver1.find_elements_by_xpath(xpathPrice)
    elementsName = driver1.find_elements_by_xpath(xpathName)
    elementsMulti = driver1.find_elements_by_xpath(xpathMultiPrice)

    reversedMulti = reversed(elementsMulti)
    multiIndexes = getIndexesOfMultiDeal()
    multiValues = getValuesOfMultiDeal()
    multiValues.reverse()

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


def getNumberOfMultiDeals():
    driver1 = __initWebDriver()
    driver1.get(url1)
    elementsPrice = driver1.find_elements_by_xpath(xpathMultiPrice)

    print(len(elementsPrice))
    driver1.close()


def getIndexesOfMultiDeal():
    """Returns a list containing the indexes of the multideals

    Returns:
        [list]: [description]
    """
    driver1 = __initWebDriver()
    driver1.get(url1)
    elements = driver1.find_elements_by_xpath(xpathShort)

    listOfIndexes = []

    for index, element in enumerate(elements):
        if("product-item-multi-price-wrapper" in element.get_attribute("class")):
            listOfIndexes.append(index)
    driver1.close()
    return listOfIndexes


def getValuesOfMultiDeal():
    """Returns a list containing the number of items
    needed for price to be accurate in a multideal

    Returns:
        List: List of int's
    """
    driver1 = __initWebDriver()
    driver1.get(url1)
    elementsMulti = driver1.find_elements_by_xpath(xpathMultiPrice)
    valueList = []
    for i in elementsMulti:
        valueList.append(int(i.text[0]))

    driver1.close()
    return valueList
