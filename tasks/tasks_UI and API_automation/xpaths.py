search_page = ".//*[@id='firstHeading']"
input_box = ".//*[@title='Search Wikipedia']"
search_button = ".//*[@class='oo-ui-inputWidget-input oo-ui-buttonElement-button']"
search_text = 'Hello world'
search_result_page = ".//h1[text()='Search results']"
search_exists = ".//div/p[@class='mw-search-exists']"
search_not_exists = ".//p[@class='mw-search-createlink']"

these_words = 'Mountain, Nepal'
exactly_these_texts = 'Mountain'
not_these_words = 'China'
one_of_these_words = 'Mount, Everest'
page_title = 'Mountain'


ad_search_option = '//*[@id="search"]/div[4]/div[1]'
these_words_xpath = '//*[@id="ooui-31"]'
exactly_these_texts_xpath = '//*[@id="ooui-33"]'
not_these_words_xpath = '//*[@id="ooui-35"]'
one_of_these_words_xpath = '//*[@id="ooui-37"]'
page_title_xpath = '//*[@id="ooui-39"]'

collapse_ad_search = '//*[text()="Advanced search:"]'
search_in_remove = '//*[@id="search"]/div[4]/div[2]/span/a/span[2]/div/div/span[2]/a'
search_in = './/*[text()="Search in:"]'
add_namespace = './/*[@placeholder="Add namespaces…"]'
search_in_remove_loop = '//*[@id="powersearch"]/div[4]/div[2]/span/a/span[2]/div/div/span[2]/a'

title_match = './/*[@data-serp-pos=0]'
ad_search_no_result = './/p[@class="mw-search-nonefound"]'
