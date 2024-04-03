from selenium.webdriver.common.by import By


class LoginLocators:
    login_input = (By.ID, "login")
    password_input = (By.XPATH, '//*[@id="password"]/input')
    login_button = (By.CLASS_NAME, 'p-button-label')


class PetPageLocators:
    pet_element = (By.CLASS_NAME, 'product-list-item')
    create_btn = (By.CSS_SELECTOR, ".pi-plus")
    delete_btn = (By.CLASS_NAME, 'pi pi-trash p-button-icon')
    first_tab = (By.XPATH, '//*[@id="pv_id_1"]/ul/li[1]')
    second_tab = (By.XPATH, '//*[@id="pv_id_1"]/ul/li[2]')
    name = (By.ID, 'name')
    age = (By.XPATH, '//span[@id=\'age\']/input')
    type_selector = (By.ID, 'typeSelector')
    dropdown_list = (By.ID, 'pv_id_5_list')
    dog = (By.XPATH, "//li[@aria-label='dog']")
    cat = (By.XPATH, "//li[@aria-label='cat']")
    reptile = (By.XPATH, "//li[@aria-label='reptile']")
    hamster = (By.XPATH, "//li[@aria-label='hamster']")
    parrot = (By.XPATH, "//li[@aria-label='parrot']")
    gender_selector = (By.ID, 'genderSelector')
    male = (By.XPATH, "//li[@aria-label='Male']")
    female = (By.XPATH, "//li[@aria-label='Female']")
    submit = (By.XPATH, "//button[@type='submit']")
    discard = (By.XPATH, "//span[text()='Cancel']/..")
    delete_cart = (By.XPATH, "//span[text()='Delete']/..")
    confirm_delete_cart = (By.XPATH, "//span[text()='Yes']/..")
    edit_pet_cart = (By.XPATH, "//span[text()='Edit']/..")
    choose_btn = (By.XPATH, "p-button-label")
    profile_btn = (By.XPATH, "//span[text()='Profile']/..")
    quit_btn = (By.XPATH, "//span[text()='Quit']/..")
