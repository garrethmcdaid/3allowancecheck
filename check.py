from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
Update username (your mobile number) and password
Change path_to_phantomjs_executable to the path of the phantomjs file provided in the original zip:
'''
username = 'xxxxxxxxxxxx'
password = 'xxxxxxxxxxx'
path_to_phantomjs_executable = '/usr/local/bin/phantomjs'


def main():
    driver = webdriver.PhantomJS(executable_path=path_to_phantomjs_executable)

    driver.get('https://login.three.ie')

    wait = WebDriverWait(driver, 30, poll_frequency=0.5)

    driver.find_element_by_css_selector('#username').send_keys(username)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#myAccount > form > table > tbody > tr:nth-child(3) > td.login_links > input.buttonBlack.medium').click()

    driver.get('https://my3account.three.ie/My_allowance')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#allowanceRemBody > tr > td.rightBorder.alignRight')))

    allowance = driver.find_element_by_css_selector('#allowanceRemBody > tr > td.rightBorder.alignRight').text

    print allowance


if __name__ == '__main__':
    main()
