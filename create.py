import sys
import os
from github import Github #PyGithub 
from dotenv import load_dotenv #python-dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    # folderName = str(sys.argv[1])
    folderName = "recipe-app"
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import sys
# import os
# import errno

# MYPATH = "/Users/coachrye/Documents/TheHub/coachrye/"
# MY_COMMAND = "touch README.md"
# # Uncomment Once Game Time
# # if len(sys.argv) > 1:
# #     project_name = sys.argv[1]
# project_name = "ThisIsAnotherTestProject"

# try:
#     os.chdir(MYPATH)
#     os.makedirs(project_name)
#     os.chdir(MYPATH + project_name)
#     os.system(MY_COMMAND)
    
# except OSError as e:
#     print("folder exists, dude!")
#     if e.errno != errno.EEXIST:
#         print("something else, dude!")
#         raise

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)

# username = "rye@coachrye.com"
# password = "gitHub#34"

# driver.get("https://github.com/login")
# wait = WebDriverWait(driver, 10)

# u = driver.find_element_by_xpath('//*[@id="login_field"]')
# p = driver.find_element_by_xpath('//*[@id="password"]')
# u.send_keys(username)
# p.send_keys(password)
# driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

# all_activity_msg = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/main/div/div/div/h2')))
# assert "All activity" in all_activity_msg.text

# driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
# repository_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
# repository_name.send_keys(project_name)
# repository_name.send_keys(Keys.TAB)

# the_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new_repository"]/div[4]/button')))
# the_button.click()

# git_command = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="empty-setup-push-repo-echo"]/span[1]')))
# git_remote_command = git_command.text
# driver.close()

# os.chdir(MYPATH + project_name)
# os.system(git_remote_command)
# os.system("git add .")
# os.system('git commit -m "initial commit"')
# os.system("git push -u origin master")