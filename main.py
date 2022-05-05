from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('/usr/local/chromedriver')
# browser = webdriver.Chrome(service=s)
# url='https://pubchem.ncbi.nlm.nih.gov/compound/4#section=Melting-Point&fullscreen=true'
# browser.get(url)


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "/Users/rmshrestha/Desktop", #Change default directory for downloads
"download.prompt_for_download": True, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://pubchem.ncbi.nlm.nih.gov/compound/4#section=Melting-Point&fullscreen=true')