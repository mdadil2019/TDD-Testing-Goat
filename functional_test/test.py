from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox(executable_path = '/Users/mdadil2019/Documents/PythonProjects/geckodriver')

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])


    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = self.browser.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise(e)
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Adil has heard about a cool new online to-do app. He goes to check out it's homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do list
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        # He types "Buy peacock feathers " into a text box
        inputbox.send_keys('Buy peacock feathers')


        # When he hits enter, teh page updates and how the page lists "1: Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)

        # We have occurance of same code more then two time to assert the strings so we will replace the code
        # with helper function so the concept is "Three strikes and refractor"

        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])



        # There is still a text box inviting him to add another item. He enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his lists

        # We have occurance of same code more then two time to assert the strings so we will replace the code
        # with helper function so the concept is "Three strikes and refractor"

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #    '2: Use peacock feathers to make a fly', [row.text for row in rows]
        # )
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")


        # Adil wonders that weather the site will remember the list. Then he sees that the site has generated a unique URL for his --
        # there is some explanatory text that effect.

        self.fail("Finish the test!")

        # He visited that url - his to do list is still there
        # Satisfied, he goes back to sleep

    def test_multiple_user_can_start_lists_at_different_urls(self):
        #adil starts a new to do lists
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #He notices that his list has a unique URL
        adil_list_url = self.browser.current_url
        self.assertRegex(adil_list_url,'/lists/.+')

        #Now a new user, Yasir, comes along to the site
        ##we use a new browser session to make sure that no information of adil is coming through cookies
        self.browser.quit()
        self.browser = webdriver.Firefox(executable_path = '/Users/mdadil2019/Documents/PythonProjects/geckodriver')

        #Yasir visited the home page, there is no sign of Adil's lists
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        print(page_text)
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Yasir starts a new list by entering a new item. He is less intesting then Adil
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy laptop')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy laptop')

        #Yasir gets his own unique url
        yasir_list_url = self.browser.current_url
        self.assertRegex(yasir_list_url,'/lists/.+')
        self.assertNotEqual(yasir_list_url,adil_list_url)

        # Again, there is no trace of Adil's lists
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy laptop', page_text)

        #Satisfactly both of them have been returned
