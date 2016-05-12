from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class TeacherTestCase(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	

	def tearDown(self):
		self.browser.quit()


	def test_teacher_can_register_on_the_site_and_add_groups_and_students(self):
		"""
		Test that teacher can register on our site and add
		group and students
		"""
		# Teacher John want to add new group and
		# a few student to new group.
		# So first he is going to do is register
		# on student-base.
		# He visits the main page of our site.
		self.browser.get(self.live_server_url + '/')


		# John seeing button register and he 
		# press mouse on that link.
		register = self.browser.find_element_by_link_text('Register')
		register.click()

		# He see register form. John must enter his username
		# password, and password confirmation. Then he press
		# Submit button.
		username = self.browser.find_element_by_id('id_username')
		username.send_keys('John Lennon')
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys('john1940')
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys('john1940')
		self.browser.find_element_by_tag_name('button').submit()

		# Now he see page that promt him to add personal info.
		# John enters his full name, date of birth and teacher ID.
		# Press Submit.
		name = self.browser.find_element_by_id('id_name')	
		name.send_keys('Lennon John')
		birthday = self.browser.find_element_by_id('id_birthday')
		birthday.send_keys('1940-10-09')
		teacher_id = self.browser.find_element_by_id('id_teacher_id')
		teacher_id.send_keys('19')
		self.browser.find_element_by_tag_name('button').submit()
	
		# Now John on the main page. He is seeing list of groups,
		# and "Add group" button. 
		self.browser.find_element_by_link_text('Add group').click()

		# He see the form to add new group.
		# He types name of new group and press Submit.
		group_name = self.browser.find_element_by_id('id_name')
		group_name.send_keys('Linux')
		self.browser.find_element_by_tag_name('button').submit()
		
		# John again on the main page. Now he goes to add a few
		# students to the group that he had add. First he press
		# the link on new group.
		self.browser.find_element_by_link_text('Linux').click()

		# He see button to add new student. He enters the button 
		# and his redirects to page to add new student.
		# John enters name, birthday, student ticket and chose to
		# which group add new student. Then he press submit.
		self.browser.find_element_by_link_text('Add student').click()
		name = self.browser.find_element_by_id('id_name')
		name.send_keys('Torvalds Linus')
		birthday = self.browser.find_element_by_id('id_birthday')
		birthday.send_keys('1969-12-28')
		student_ticket = self.browser.find_element_by_id('id_student_ticket')
		student_ticket.send_keys('28')
		student_group = self.browser.find_elements_by_tag_name('option')[-1].click()
		self.browser.find_element_by_tag_name('button').submit()

		# Finaly he edit new group to assign praepostor to new group.
		# He goes to main page and press Edit button that assosiated
		# with this group. He chose a student to be a praepostor
		# and press submit.

		edit_links = self.browser.find_elements_by_link_text('Edit')
		last_link = edit_links[-1]
		self.assertEqual(last_link.get_attribute('href'), self.live_server_url + '/students/linux/update_group')
		last_link.click()
		student_list = self.browser.find_elements_by_tag_name('option')
		for student in student_list:
			if student.text == 'Torvalds Linus':
				student.click()
		self.browser.find_element_by_tag_name('button').submit()

