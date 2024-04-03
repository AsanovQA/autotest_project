import os
import pytest
from dotenv import load_dotenv
import time
from pages.petspage import PetsPage

load_dotenv()
link = os.getenv('PROFILE_URL')

pets_length = 0


class TestPetsPage:

    @pytest.mark.regressions
    @pytest.mark.smoke
    def test_create_pet(self, tests_with_auth):
        pp = PetsPage(tests_with_auth, link)
        pets_length = pp.pets_list_length()
        pp.create_btn_click()
        pp.input_name(os.getenv('FIRST_NAME'))
        pp.input_age(12)
        pp.open_pet_dropdown()
        pp.select_pet_type(os.getenv('FIRST_TYPE'))
        pp.open_gender_selector()
        pp.select_gender(os.getenv('MALE'))
        pp.submit_click()
        pp.open_link()
        pp.refresh_page()
        time.sleep(2)
        assert pp.pets_list_length() > pets_length

    @pytest.mark.regressions
    def test_delete_pet_cart(self, tests_with_auth):
        pp = PetsPage(tests_with_auth, link)
        pets_length = pp.pets_list_length()
        if pets_length > 0:
            pp.delete_pet_cart()
            pp.refresh_page()
            assert pp.pets_list_length() < pets_length
        else:
            assert pp.pets_list_length() == 0

    @pytest.mark.regressions
    def test_edit_cart(self, tests_with_auth):
        pp = PetsPage(tests_with_auth, link)
        pp.edit_pet_cart()
        pp.input_name(os.getenv('SECOND_NAME'))
        pp.input_age(6)
        pp.refresh_page()
        pp.open_pet_dropdown()
        pp.select_pet_type(os.getenv('SECOND_TYPE'))
        pp.open_gender_selector()
        pp.select_gender(os.getenv('FEMALE'))
        pp.submit_click()
        # подождет пока разберусь как загружать файлы
        # pp.choose_picture()

    @pytest.mark.regressions
    def test_profile_btn(self, tests_with_auth):
        pp = PetsPage(tests_with_auth, link)
        pp.click_profile_btn()
        assert "profile" in tests_with_auth.current_url.lower()

    @pytest.mark.regressions
    def test_quit_from_profile(self, tests_with_auth):
        pp = PetsPage(tests_with_auth, link)
        pp.quit_from_profile()
        assert "login" in tests_with_auth.current_url.lower()






