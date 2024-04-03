from .basepage import BasePage
from .locators import PetPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging


class PetsPage(BasePage):
    def create_btn_click(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.create_btn)).click()

    def delete_btn_click(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.delete_btn))

    def input_name(self, petname):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.name)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.name)).send_keys(petname)

    def input_age(self, age):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.age)).send_keys(age)

    def open_pet_dropdown(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.type_selector)).click()

    def select_pet_type(self, pettype: str):
        if pettype == 'dog':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.dog)).click()
        elif pettype == 'cat':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.cat)).click()
        elif pettype == 'reptile':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.reptile)).click()
        elif pettype == 'hamster':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.hamster)).click()
        elif pettype == 'parrot':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.parrot)).click()
        else:
            logging.error("Unknown type")

    def open_gender_selector(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.gender_selector)).click()

    def select_gender(self, gender: str):
        if gender == 'male':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.male)).click()
        elif gender == 'female':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.female)).click()
        else:
            logging.error("Unknown gender")

    def submit_click(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.submit)).submit()

    def discard_click(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.discard)).submit()

    def delete_pet_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.delete_cart)).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PetPageLocators.confirm_delete_cart)).click()

    def edit_pet_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.edit_pet_cart)).click()

    def choose_picture(self):
        self.driver.find_element(*PetPageLocators.choose_btn).click()

    def click_profile_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.profile_btn)).click()

    def quit_from_profile(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PetPageLocators.quit_btn)).click()

    def pets_list_length(self):
        pets = self.driver.find_elements(*PetPageLocators.pet_element)
        return len(pets)
