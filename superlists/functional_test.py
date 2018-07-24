from selenium import webdriver
import unittest

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
        self.fail('Finish')

        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers " into a text box

        # When he hits enter, teh page updates and how the page lists "1: Buy peacock feathers" as an item in a to-do lists

        # The page updates again, and now hows both ietms on her lists


        # There is still a text box inviting him to add another item. He enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on his lists


        # Adil wonders that weather the site will remember the list. Then he sees that the site has generated a unique URL for his --
        # there is some explanatory text that effect.

        # He visited that url - his to do list is still there
        # Satisfied, he goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings=None)
