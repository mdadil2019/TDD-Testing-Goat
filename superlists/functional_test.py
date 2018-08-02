from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Adil has heard about a cool new online to-do app. He goes to check out it's homepage
        self.browser.get('http://localhost:8000')

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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"New to-do item didn't appear in table Contents were:\n{table.text}"
        )

        # There is still a text box inviting him to add another item. He enters "Use peacock feathers to make a fly"
        self.fail("Finish the test!")
        # The page updates again, and now shows both items on his lists


        # Adil wonders that weather the site will remember the list. Then he sees that the site has generated a unique URL for his --
        # there is some explanatory text that effect.

        # He visited that url - his to do list is still there
        # Satisfied, he goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings=None)
