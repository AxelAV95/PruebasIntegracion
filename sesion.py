# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSesion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sesion(self):
    self.driver.get("http://localhost/23-UNA-supermercado-Web-23-UNA-supermercado-Movil/web/supermercado/view/loginview.php")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "usuariocedula").click()
    self.driver.find_element(By.ID, "usuariocedula").send_keys("12345678")
    self.driver.find_element(By.NAME, "usuariopassword").send_keys("12345")
    self.driver.find_element(By.ID, "btnIniciarSesion").click()
  
