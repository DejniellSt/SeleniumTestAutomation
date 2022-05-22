import unittest
from selenium import webdriver
import time
import random

# Initialize webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# Variable
fName = 'Tester'
fakeName = 'Programista'
lName = 'WSB'
mail = 'testMail@wsb.pl'
adrr = 'Reaktor 4'
city_area = 'Czarnobyl'
phone_number = '123321123'
pcode = '12-123'
regionn = 'Zachodniopomorskie'

# Main class
class Automation(unittest.TestCase):

    # Method setUp
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
        self.driver.get("http://www.tutorialsninja.com/demo/")
        self.driver.maximize_window()
        time.sleep(3)

    # Method testFunction
    def testFunction(self):
        phones = self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[6]/a').click()
        time.sleep(2)

        # Choose correct model of phone
        iPhone = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/div[1]/a').click()
        time.sleep(3)

        # Check pictures
        first_photo = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/ul[1]/li[1]/a').click()

        # Next picture
        next = self.driver.find_element_by_xpath('/html/body/div[2]/div/button[2]')

        for i in range(0, 5):
            next.click()
            time.sleep(2)

        # Save screenshot
        self.driver.save_screenshot('MY_screenshot#' + str(random.randint(0, 101)) + '.png')

        # Close view with picture
        close = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/button').click()

        # Select the correct quantity for your order
        addItem = self.driver.find_element_by_id('input-quantity')
        time.sleep(2)
        addItem.clear()
        time.sleep(2)
        addItem.send_keys('3')

        # Add to cart
        addToCart = self.driver.find_element_by_id("button-cart").click()
        time.sleep(3)

        # Find laptops
        laptop = self.driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
        action = ActionChains(self.driver)
        action.move_to_element(laptop).perform()
        time.sleep(2)
        laptop2 = self.driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]').click()
        time.sleep(3)

        # Choose the right one laptop
        mac = self.driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div/div[2]/div[1]/h4/a').click()
        addToCart2 = self.driver.find_element_by_xpath('//button[@id="button-cart"]')
        addToCart2.location_once_scrolled_into_view
        time.sleep(1)

        # Setting the correct date
        calendar = self.driver.find_element_by_xpath('//i[@class="fa fa-calendar"]').click()
        time.sleep(2)
        next_click_calendar = self.driver.find_element_by_xpath('//th[@class="next"]')
        month_years = self.driver.find_element_by_xpath('//th[@class="picker-switch"]')

        # year 2022
        while month_years.text != 'July 2022':
            next_click_calendar.click()
        time.sleep(2)

        # Choose day 31
        calendar_date = self.driver.find_element_by_xpath('//td[text()="20"]')
        calendar_date.click()
        time.sleep(2)
        addToCart2.click()

        goToDelivery = self.driver.find_element_by_id('cart-total').click()
        time.sleep(1)
        goToCheckOut = self.driver.find_element_by_xpath('//p[@class="text-right"]/a[2]').click()
        time.sleep(3)

        # Remove iphone
        acctuall = self.driver.find_element_by_xpath("//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input").get_attribute("value")
        self.assertIsNot(acctuall,'0')
        removePhone = self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/span/button[2]').click()
        time.sleep(5)
        checkout = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/a').click()
        time.sleep(5)

        # Create new user account
        new_user = self.driver.find_element_by_xpath('//input[@value="guest"]').click()

        continioue1 = self.driver.find_element_by_id('button-account').click()
        time.sleep(2)

        step2 = self.driver.find_element_by_xpath('//a[text()="Step 2: Billing Details "]')
        step2.location_once_scrolled_into_view
        time.sleep(2)

        # First name input
        Namee = self.driver.find_element_by_id('input-payment-firstname')
        Namee.click()
        time.sleep(1)
        Namee.send_keys(fName)

        # Last name input
        Lastt = self.driver.find_element_by_id('input-payment-lastname')
        Lastt.click()
        time.sleep(1)
        Lastt.send_keys(lName)

        # Email input
        email = self.driver.find_element_by_id('input-payment-email')
        email.click()
        time.sleep(1)
        email.send_keys(mail)

        # Telephone
        tell = self.driver.find_element_by_id('input-payment-telephone')
        tell.click()
        time.sleep(1)
        tell.send_keys(phone_number)

        # Address
        addresss = self.driver.find_element_by_id('input-payment-address-1')
        addresss.click()
        time.sleep(1)
        addresss.send_keys(adrr)

        # City
        cityy = self.driver.find_element_by_id('input-payment-city')
        cityy.click()
        time.sleep(1)
        cityy.send_keys(city_area)

        # Postalcode
        postall = self.driver.find_element_by_id('input-payment-postcode')
        postall.click()
        time.sleep(1)
        postall.send_keys(pcode)

        # Country
        country = self.driver.find_element_by_id('input-payment-country')
        dropdown = Select(country)
        dropdown.select_by_index(180)
        time.sleep(1)

        # Region
        region = self.driver.find_element_by_id('input-payment-zone')
        dropdown2 = Select(region)
        dropdown2.select_by_visible_text(regionn)
        time.sleep(1)

        # Continue button
        continue3 = self.driver.find_element_by_id('button-guest')
        continue3.click()
        time.sleep(2)

        # Continue button
        continue4 = self.driver.find_element_by_id('button-shipping-method')
        continue4.click()
        time.sleep(2)

        # Click checkbox
        checkbox = self.driver.find_element_by_xpath('//input[@name="agree"]').get_attribute("name")
        self.assertEqual(checkbox,"agree")
        checkbox1 = self.driver.find_element_by_xpath('//input[@name="agree"]')
        checkbox1.click()
        time.sleep(2)

        # Continue button
        continue5 = self.driver.find_element_by_xpath('//*[@id="button-payment-method"]')
        continue5.click()
        time.sleep(2)

        # Show final price
        final_price = self.driver.find_element_by_xpath('//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
        print("The final price is :" + final_price.text)

        # Confirm button
        confirm = self.driver.find_element_by_xpath('//*[@id="button-confirm"]')
        confirm.click()
        time.sleep(2)

        # Continue button
        continue6 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/a')
        continue6.click()
        time.sleep(2)

    # Method to close the windows
    def Down(self):
        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    # Create an object
    unittest.main()
    test = Automation()
    # Method call
    test.setUp()
    test.testFunction()
    test.Down()
