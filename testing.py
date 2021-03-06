from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def dictionarycreator():

    entries = {}
    lists = []
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Category:Epidemiology")
    assert "Epidemiology" in driver.title

    css_elements = driver.find_elements_by_css_selector("#mw-pages a[href*='/wiki/']")

    for elem in css_elements:
        entries[elem.text] = elem.get_attribute("href")
        if (elem.text) == "learn more":
            continue
        lists.append(elem.text)

    elem = driver.find_element_by_link_text("next page").click()

    css_elements = driver.find_elements_by_css_selector("#mw-pages a[href*='/wiki/']")

    for elem in css_elements:
        entries[elem.text] = elem.get_attribute("href")
        if (elem.text) == "learn more":
            continue
        lists.append(elem.text)

    assert "No results found." not in driver.page_source
    driver.close()

    return lists

if __name__ == "__main__":
    t = []
    t = dictionarycreator()
    print (t)
