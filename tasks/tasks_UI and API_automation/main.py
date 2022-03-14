import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from xpaths import *
import os
from api_testing import *

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--hide-scrollbars")
options.add_argument("--headless")

baseURL = 'https://en.wikipedia.org/w/index.php?search'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 60)
file_path = os.path.dirname(os.path.dirname(__file__))
filename = os.path.join(file_path, 'tasks_UI_automation/screenshots/')


def normal_search_test():
    driver.get(baseURL)
    time_start = datetime.datetime.now()
    wait.until(EC.visibility_of_element_located((By.XPATH, search_page)))
    driver.find_element(By.XPATH, input_box).send_keys(f'{search_text}')
    driver.find_element(By.XPATH, search_button).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, search_result_page)))
    driver.save_screenshot(filename+f'general_search_{search_text}.png')
    print('Test Summary - General Search')
    print('=============================')
    print(f'Searched for text: {search_text}')
    try:
        result_found = driver.find_element(By.XPATH, search_exists)
        if result_found:
            print('Status: Passed')
            print('The searched text page exists in the wikipedia.')
    except:
        result_not_found = driver.find_element(By.XPATH, search_not_exists)
        if result_not_found:
            print('Status: Passed')
            print("The searched text page doesn't exists in the wikipedia.")

    time_end = datetime.datetime.now()
    total_time_taken = time_end - time_start
    time_sec = round((total_time_taken.total_seconds() / 60.0), 3)
    print(f'Total time taken to complete the test: {time_sec} seconds')


def advance_search_test():
    driver.get(baseURL)
    time_start = datetime.datetime.now()
    wait.until(EC.visibility_of_element_located((By.XPATH, ad_search_option)))
    driver.find_element(By.XPATH, ad_search_option).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, these_words_xpath)))
    driver.find_element(By.XPATH, these_words_xpath).send_keys(these_words)
    driver.find_element(By.XPATH, exactly_these_texts_xpath).send_keys(exactly_these_texts)
    driver.find_element(By.XPATH, not_these_words_xpath).send_keys(not_these_words)
    driver.find_element(By.XPATH, one_of_these_words_xpath).send_keys(one_of_these_words)
    driver.find_element(By.XPATH, page_title_xpath).send_keys(page_title)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, collapse_ad_search).click()
    driver.find_element(By.XPATH, search_in_remove).click()

    print('Test Summary - Advance Search')
    print('=============================')
    print('Searched criteria')
    print(f'These words: {these_words}')
    print(f'Exactly these text: {exactly_these_texts}')
    print(f'Not these words: {not_these_words}')
    print(f'One of these words: {one_of_these_words}')
    print(f'Page title contains: {page_title}')
    print('=============================')

    search_options = ['Talk', 'Wikipedia', 'File', 'Module talk', 'Gadget definition talk']
    for values in search_options:
        driver.find_element(By.XPATH, search_in).click()
        driver.find_element(By.XPATH, add_namespace).send_keys(values)
        driver.find_element(By.XPATH, f'.//*[@class="mw-advancedSearch-ui-itemMenuOptionWidget-label-title"]/bdi'
                                      f'/span[text()="{values}"]').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, search_button).click()
        driver.find_element(By.XPATH, search_in_remove_loop).click()
        driver.save_screenshot(filename + f'advances_search_{values}.png')
        try:
            title_text = driver.find_element(By.XPATH, title_match).text
            if page_title and values in title_text:
                print(f'Search in namespace: {values}')
                print('Status: Passed')
                print('The search title is present in the search result.')
        except:
            if ad_search_no_result:
                print(f'Search in namespace: {values}')
                print('Status: Passed')
                print('No matching result found.')
        print('\n')

    time_end = datetime.datetime.now()
    total_time_taken = time_end - time_start
    time_sec = round((total_time_taken.total_seconds() / 60.0), 3)
    print('==========================================================')
    print(f'Total time taken to complete the test: {time_sec} seconds')


if __name__ == '__main__':
    normal_search_test()
    print('\n')
    advance_search_test()
    driver.quit()
    print('\n')
    print('API Testing Summary')
    print('================================')
    print('Post Value')
    post_value()
    print('--------------------------------')
    print('Get Value')
    get_value()
    print('--------------------------------')
    print('Update Value')
    update_value()
    print('--------------------------------')
    print('Delete Order')
    delete_order()
