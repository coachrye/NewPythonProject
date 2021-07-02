from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import errno


MYPATH = "/Users/coachrye/Documents/TheHub/coachrye/"
MY_COMMAND = "touch README.md"
# Uncomment Once Game Time
# if len(sys.argv) > 1:
#     project_name = sys.argv[1]
project_name = "ThisIsMyTestProject"

try:
    os.chdir(MYPATH)
    # os.makedirs(project_name)
    os.chdir(MYPATH + project_name)
    # os.system(MY_COMMAND)
    
except OSError as e:
    print("folder exists, dude!")
    if e.errno != errno.EEXIST:
        print("something else, dude!")
        raise

driver = webdriver.Chrome()
driver.implicitly_wait(10)

username = "rye@coachrye.com"
password = "gitHub#34"

driver.get("https://github.com/login")

u = driver.find_element_by_xpath('//*[@id="login_field"]')
p = driver.find_element_by_xpath('//*[@id="password"]')
u.send_keys(username)
p.send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

print("pit stop")

all_activity_msg = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/main/div/div/div/h2')
assert "All activity" in all_activity_msg.text

driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
repository_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
repository_name.send_keys(project_name)
repository_name.send_keys(Keys.TAB)

print("pit stop #2")
# driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()

wait = WebDriverWait(driver, 10)
the_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new_repository"]/div[4]/button')))
the_button.click()

print("pit stop #3")
git_command = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="empty-setup-push-repo-echo"]/span[1]')))

print("pit stop #4")
print(git_command.text)
git_remote_command = git_command.text
driver.close()

# driver.find_element_by_xpath('/html/body/div[4]/div/aside/div[2]/div[2]/div/h2/a').click()

# https://github.com/login
    # driver.get("https://www.seeyoudoc.xyz/")
    # assert "Find and book medical appointments anytime, anywhere at SeeYouDoc" in driver.title

    # driver.find_element_by_xpath('//*[@id="patient-topnav"]/div[1]/form/ul/a[2]').click()
    # assert "Login and start booking medical appointments at SeeYouDoc" in driver.title

    # # Invalid Credential
    # login(driver, "admin1@syd.com", "P@ssw0rd")
    # assert "Login failed. Please try again." in driver.page_source

    # driver.get(driver.current_url)

    # # Valid Credential'
    # login(driver, "admin@syd.com", "P@ssw0rd")
    # welcome_msg = driver.find_element_by_xpath('//*[@id="account-dashboard"]/div/div[1]/div/div[2]/h4')
    # assert "Welcome" in welcome_msg.text
    # print("Successfully Logged In")
    # driver.close()

# driver.close()

os.system(git_remote_command)
os.system("git add .")
os.system('git commit -m "initial commit"')
os.system("git push -u origin master")