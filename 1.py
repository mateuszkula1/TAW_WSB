from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

# Załadowanie strony https://duckduckgo.com/ i test czy strona się załadowała 
browser.get("https://duckduckgo.com/")
print(browser.title)
assert "DuckDuckGo — Privacy, simplified." in browser.title

# Wyszukanie w oknie wyszukiwania frazy "the biggest python software house"
elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("the biggest python software house")
elem.send_keys(Keys.RETURN)

# Oczekiwanie na załadowanie listy wyników
wait = WebDriverWait(browser, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "r1-0")))

# Wejście w pierwszy link
element.click()

# Załadowanie strony i test czy zawiera string "STX Next"
wait.until(EC.title_is("Python Django and JS Development Company - STX Next"))
print(browser.title)
assert "STX Next" in browser.page_source

# Zamknięcie przeglądarki
browser.quit()
