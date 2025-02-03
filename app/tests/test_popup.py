import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Front end test DATA SOURCES box
class TestPopupButton(unittest.TestCase): 
    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/dashboard/home/")  # URL of the page containing the popup

    def test_popup_clickable(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "datasources-box")  # Update with the actual trigger element ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "datasources-box")
        WebDriverWait(driver, 30).until(EC.visibility_of(popup))

        # Step 4: Verify that the popup is visible and can be clicked
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

        # You can further test if the popup is actually clickable
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(popup))
            print("Popup is clickable!")
        except:
            print("Popup is NOT clickable.")

    def test_popup_appears_when_clicked(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "datasources-box")  # Update this ID with your actual button's ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "datasources-box")  # Update this ID with your actual popup's ID

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(popup))
            print("Popup is visible after button click!")
        except:
            self.fail("Popup did not appear after clicking the button.")

        # Step 4: Verify if the popup is visible after clicking the button
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

#Front end test BNF CODES box
class TestPopupButton(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/dashboard/home/")  # URL of the page containing the popup

    def test_popup_clickable(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "bnfcodes-box")  # Update with the actual trigger element ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "bnfcodes-box")
        WebDriverWait(driver, 30).until(EC.visibility_of(popup))

        # Step 4: Verify that the popup is visible and can be clicked
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

        # You can further test if the popup is actually clickable
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(popup))
            print("Popup is clickable!")
        except:
            print("Popup is NOT clickable.")

    def test_popup_appears_when_clicked(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "bnfcodes-box")  # Update this ID with your actual button's ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "bnfcodes-box")  # Update this ID with your actual popup's ID

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(popup))
            print("Popup is visible after button click!")
        except:
            self.fail("Popup did not appear after clicking the button.")

        # Step 4: Verify if the popup is visible after clicking the button
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

#Front end test FAQ box
class TestPopupButton(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/dashboard/home/")  # URL of the page containing the popup

    def test_popup_clickable(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "faq-box")  # Update with the actual trigger element ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "faq-box")
        WebDriverWait(driver, 30).until(EC.visibility_of(popup))

        # Step 4: Verify that the popup is visible and can be clicked
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

        # You can further test if the popup is actually clickable
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(popup))
            print("Popup is clickable!")
        except:
            print("Popup is NOT clickable.")

    def test_popup_appears_when_clicked(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "faq-box")  # Update this ID with your actual button's ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "faq-box")  # Update this ID with your actual popup's ID

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(popup))
            print("Popup is visible after button click!")
        except:
            self.fail("Popup did not appear after clicking the button.")

        # Step 4: Verify if the popup is visible after clicking the button
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

#Front end test ABOUT box
class TestPopupButton(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/dashboard/home/")  # URL of the page containing the popup

    def test_popup_clickable(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "about-box")  # Update with the actual trigger element ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "about-box")
        WebDriverWait(driver, 30).until(EC.visibility_of(popup))

        # Step 4: Verify that the popup is visible and can be clicked
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

        # You can further test if the popup is actually clickable
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(popup))
            print("Popup is clickable!")
        except:
            print("Popup is NOT clickable.")

    def test_popup_appears_when_clicked(self):
        driver = self.driver

        # Step 1: Locate the button that triggers the popup
        button = driver.find_element(By.ID, "about-box")  # Update this ID with your actual button's ID

        # Step 2: Wait for the button to be clickable and click it
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(button))
        button.click()

        # Step 3: Wait for the popup to be visible
        popup = driver.find_element(By.ID, "about-box")  # Update this ID with your actual popup's ID

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(popup))
            print("Popup is visible after button click!")
        except:
            self.fail("Popup did not appear after clicking the button.")

        # Step 4: Verify if the popup is visible after clicking the button
        self.assertTrue(popup.is_displayed(), "Popup should be visible after clicking the button.")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
