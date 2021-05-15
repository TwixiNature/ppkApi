import pathlib

from selenium import webdriver

url = 'https://www.gymgrossisten.com/kosttillskott/bars'

xpathName = "//p[@class='product-tile-name']"
xpathPrice = "//div[@class='price']"


class gymgrossistenItem:
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
    driver.get(url)
    elements = driver.find_elements_by_xpath(xpathPrice)
    numberOfItems = len(elements)
    driver.close
    return numberOfItems


def namesOfItems():
    driver = __initWebDriver()
    driver.get(url)
    elements = driver.find_elements_by_xpath(xpathName)
    listOfAllItemNames = [item.text for item in elements]
    return listOfAllItemNames


def pricesOfItems():
    driver = __initWebDriver()
    driver.get(url)
    elements = driver.find_elements_by_xpath(xpathPrice)
    listOfPrices = []
    for element in elements:
        if(element.find_elements_by_class_name("price-adjusted") != []):
            text = element.find_elements_by_class_name(
                "price-adjusted")[0].text
            listOfPrices.append(priceTextToInt(text))
        else:
            text = element.find_element_by_class_name("price-sales").text
            listOfPrices.append(priceTextToInt(text))

    return listOfPrices


def priceTextToInt(text):
    sep = ' '
    return int(text.split(sep, 1)[0])


def getProducts():
    """Returns a list containing all protein-products on Gymgrossisten site.


    Returns:
        [matsmartItem]: List of gymgrossistenItem.
    """
    listOfNames = namesOfItems()
    listOfPrices = pricesOfItems()
    listOfGymgrossistenItems = []
    for i in range(len(listOfNames)):
        listOfGymgrossistenItems.append(
            gymgrossistenItem(listOfNames[i], listOfPrices[i]))
        print(listOfNames[i])
        print(listOfPrices[i])
        print('\n')

    return listOfGymgrossistenItems
