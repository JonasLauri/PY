from selenium import webdriver

def lrt_auto_fill(nm, mob, mail, text):
    browser = webdriver.Chrome()
    #browser.get('https://www.lrt.lt/')
    #ikelk = browser.find_element_by_css_selector("#site_header > div > div.header__head-block.head-block > div.head-block__right > a.btn.btn--primary.js-upload-button.d-none.d-xs-inline-flex")
    #ikelk.click()
    browser.get('https://apie.lrt.lt/bendraukime/rasykite')
    radio = browser.find_element_by_css_selector("#radio1")
    radio.submit()
    name = browser.find_element_by_name("Vardas_Pavarde")
    name.send_keys(nm)
    name.submit()
    tel = browser.find_element_by_name("Telefonas")
    tel.send_keys(mob)
    tel.submit()
    el = browser.find_element_by_name("EL_pastas")
    el.send_keys(mail)
    el.submit()
    radio2 = browser.find_element_by_css_selector("#radio2")
    radio2.submit()
    text = browser.find_element_by_css_selector("#fieldUploadNotice")
    text.send_keys(text)
    text.submit()
    

#lrt_auto_fill()
