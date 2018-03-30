from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\DaTaScienceTuts\chromedriver.exe")
driver.get('https://www.myetherwallet.com/')

ele = driver.find_element_by_link_text('MyEtherWallet is not a Bank')
ele.click()
ele1 = driver.find_element_by_link_text('MyEtherWallet is an Interface')
ele1.click()
ele2 = driver.find_element_by_link_text('WTF is a Blockchain?')
ele2.click()
ele3 = driver.find_element_by_link_text('But...why?')
ele3.click()
ele4 = driver.find_element_by_link_text("What's the Point of MEW then?")
ele4.click()
ele5 = driver.find_element_by_link_text("How To Protect Yourself & Your Funds")
ele5.click()
ele6 = driver.find_element_by_link_text("How To Protect Yourself from Scams")
ele6.click()
ele7 = driver.find_element_by_link_text("How To Protect Yourself from Loss")
ele7.click()
ele8 = driver.find_element_by_link_text("One more click & you're done! 🤘")
ele8.click()
driver.refresh()

psd = driver.find_element_by_name("password")
psd.send_keys("Mahecode@123456")
button = driver.find_element_by_link_text("Create New Wallet")
button.click()

driver.find_element_by_link_text("Download Keystore File (UTC / JSON)").click()


