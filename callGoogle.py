from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
from random import random
from selenium.common.exceptions import NoSuchElementException


# A function to generate a random number between min, max
def generate_random_between_steps():
    min = 1
    max = 4
    return (min + (random() * (max - min)))

# A function to generate random time between letters
def generate_random_between_letters():
    min = 0.2
    max = 0.5
    return (min + (random() * (max - min)))

# An object of class webdriver (for chrome)
driver = webdriver.Chrome()

# The url address that we want to go to
url = 'https://www.google.com'

# Go to the url given above
driver.get(url)

# Wait a random time before the next step
time.sleep(generate_random_between_steps())

# Get the search entry field
searchEntry = driver.find_element_by_name('q')

# Click on the search entry to activate it
searchEntry.click()

# The string to search for
searchFor = 'PyConDE'

# Write into the search field with random time between each step
for letter in searchFor:
    searchEntry.send_keys(letter)
    time.sleep(generate_random_between_letters())

time.sleep(generate_random_between_steps())

# Press Enter
searchEntry.send_keys(Keys.RETURN)

# Get all search results into a list
searchResults = driver.find_elements_by_css_selector('.LC20lb')
time.sleep(generate_random_between_steps())

# Click on the first search result
searchResults[0].click()
time.sleep(generate_random_between_steps())

# Scroll down the webpage a 1000 pixels using y-position
driver.execute_script("window.scrollTo(0, 1000)")

# Scroll down 1000 pixels in a smooth way
# for i in range(1, 1000, 20):
#     driver.execute_script("window.scrollTo(" +str(i) +"," + str(i+20) + ")")
#     time.sleep(generate_random_between_letters())


# Scroll down the webpage to a specific element
#elements = driver.find_elements_by_css_selector('.row')
#driver.execute_script("arguments[0].scrollIntoView();", elements[4])



