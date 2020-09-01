from selenium import webdriver
browser = webdriver.Firefox()
browser.get('html')
elem = browser.find_element_by_css_selector('css')
elem.click()
elems = browser.find_elements_by_css_selector('p')
len(elems)


searchelem = browser.find_elements_by_css_selector('p')
