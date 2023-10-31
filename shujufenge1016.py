# -*-coding:utf-8-*-
# @Time    :2023/10/178:56
# @Author  :Trouble
# @Email   :651919278@qq.com
# @File    :shujufenge1016.py
# @Software:PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddt
import unittest
from parameterized import parameterized
import pytest
from parse_csv import *

data = parse_csv(r"D:\python\pycharm\test\unitest测试\po设计模块\testfenge.csv")


class Login_iwe_OBJ():
    Username = (By.ID, "inputUsername")
    Password = (By.ID, "inputPassword")
    Login_button = (By.XPATH, '/html/body/div/form/button')
    Login_info_err = (By.XPATH, '/html/body/div/form/p')


class BasePage():
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def enter_username(self, username):
        ele = self.driver.find_element(*Login_iwe_OBJ.Username)
        ele.clear()
        ele.send_keys(username)

    def enter_password(self, password):
        ele = self.driver.find_element(*Login_iwe_OBJ.Password)
        ele.clear()
        ele.send_keys(password)

    def click_login_button(self):
        ele = self.driver.find_element(*Login_iwe_OBJ.Login_button)
        ele.click()

    def login_err(self):
        ele = self.driver.find_element(*Login_iwe_OBJ.Login_info_err)
        print(ele.text)


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLoginTestCase():

    def test_login_01(self, username, password, status):
        url = "http://127.0.0.1:8000"

        self.driver = webdriver.Edge()
        self.driver.maximize_window()

        self.driver.get(url)
        LoginPage(self.driver).enter_username(username)
        LoginPage(self.driver).enter_password(password)
        LoginPage(self.driver).click_login_button()
        time.sleep(3)
        if status == "0":
            LoginPage(self.driver).login_err()
        else:
            print("success")


if __name__ == '__main__':
    pytest.main(["-s","shujufenge1016.py"])
    print(data)
