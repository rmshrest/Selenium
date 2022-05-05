from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('/usr/local/chromedriver')
browser = webdriver.Chrome(service=s)
url='https://pubchem.ncbi.nlm.nih.gov/compound/4#section=Melting-Point&fullscreen=true'
browser.get(url)
