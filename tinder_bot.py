from selenium import webdriver
from time import sleep
import random

from secrets import username, password

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome('C:\\chromedriver')
		# sleep(2)

	def login(self):
		self.driver.get('https://tinder.com')
		sleep(3)

		terms_use = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
		terms_use.click()
		print('Убрал user соглашение')
		sleep(2)

		try:
			google_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
			google_btn.click()
			print('Кликнул на google')
		except:
			print("Ошибка со входом через Google")
			self.driver.close()

		sleep(1)

		#переключиться на всплывающее окно ввода
		base_window = self.driver.window_handles[0]
		sleep(3)
		self.driver.switch_to_window(self.driver.window_handles[1])

		email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
		email_in.send_keys(username)

		next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
		next_btn.click()
		sleep(1)

		pw_btn = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
		pw_btn.send_keys(password)

		next_pw_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
		next_pw_btn.click()

		self.driver.switch_to_window(base_window)
		sleep(3)

		self.driver.implicitly_wait(10)
		geo_yes = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		sleep(3)
		geo_yes.click()

		self.driver.implicitly_wait(10)
		notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
		notifications.click()
  
		sleep(3)
		self.driver.implicitly_wait(10)
		change_location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span')
		change_location.click()

		print('Авторизация завершина')

	def like(self):
		like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
		like_btn.click()
	
	def dislike(self):
		dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
		dislike_btn.click()

	def random_click(self):
		list = [0.5, 1, 1.5, 2, 2.5]
		return random.choice(list)
		
	def auto_swipe(self):
		while True:
			# sleep(1)
			try:
				sleep(self.random_click())
				self.like()
			except Exception:
				try:
					self.close_popup()
				except Exception:
					self.close_match()

	def close_popup(self):
		popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
		popup_3.click()

	def close_match(self):
		write_hello = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
		write_hello.send_keys('Привет)')

		send_hello = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
		send_hello.click()

		match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
		match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()