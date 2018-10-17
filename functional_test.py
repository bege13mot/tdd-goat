from selenium import webdriver

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

        # Sho notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into text box

        # Weh she hits enter, the page updates, and now page list:
        # 1: Buy peacock feather
        # as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters:
        # Use peackok feather to make a fly

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