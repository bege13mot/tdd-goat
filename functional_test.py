from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # Sh goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into text box
        inputbox.send_keys('Buy peackock feathers')

        # Weh she hits enter, the page updates, and now page list:
        # 1: Buy peacock feather
        # as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table")

        # There is still a text box inviting her to add another item. She enters:
        # Use peackok feather to make a fly
        self.fail('Finish the test!!!!')

        # The page updates again, and now shows boths items on her list

        # Edith wonders whether the site will remember her list.
        # Then she sees that the site has generate unique URL for her --
        # there is some explanatory text to that effect

        # She visits that URL - her to-do lis is still there

        # Satisfied, she goes back to sleep

# Finally, we have the if __name__ == '__main__' clause (if you’ve not seen it before, that’s how a Python script checks if it’s been executed 
# from the command line, rather than just imported by another script). 
# We call unittest.main(), which launches the unittest test runner, which will automatically find test classes and methods in the file and run them.
if __name__ == '__main__':
    unittest.main(warnings='ignore')