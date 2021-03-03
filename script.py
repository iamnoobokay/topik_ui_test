from selenium import webdriver
import threading
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logic():
    driver = webdriver.Firefox()
    url = 'file:///C:/Users/Pranav/Desktop/silverback/TOPIK_MOCK_TEST_FRONTEND/login.html'
    driver.get(url)
    # Implement your test logic
    user_email = driver.find_element_by_id('userEmail')
    user_password = driver.find_element_by_name('password')
    submit_button = driver.find_element_by_class_name('btn')
    user_email.send_keys('student@student.com')
    user_password.send_keys('student1234')
    submit_button.click()
    time.sleep(20)

    language_name = driver.find_element_by_class_name('language-badge')
    language_name.click()

    time.sleep(5)
    test_button = driver.find_element_by_class_name('btn-success')
    test_button.click()

    time.sleep(5)
    question_20 = driver.find_element_by_id('listeningBtn_20')
    question_20.click()

    time.sleep(5)
    play_btn = driver.find_element_by_class_name('playBtn')
    play_btn.click()
    # driver.quit()

N = 5   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(1)
    print(t.name+' started!')
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')