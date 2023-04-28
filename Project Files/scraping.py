import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# data = pd.read_excel(r"D:\Academics\Data Science\Project\Internshala Submissions\Blackcoffer\Blackcoffer\Input.xlsx")
data = pd.read_excel(os.getcwd()[:70]+"Blackcoffer\Input.xlsx")


def scrap(file_name,url):

    # checking is file aldready scraped
    if not os.path.exists(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt") :
        # To open broweser
        browser = webdriver.Edge(executable_path="Blackcoffer/Project Files/msedgedriver.exe")
        browser.get(url)
        browser.maximize_window()

        # checking is page has 404 error
        value = browser.find_elements(By.XPATH, "//h3[normalize-space()='Ooops... Error 404']")
        # print(len(value))
        if len(value)==0:
            #  to get title from any of the 2 xpaths
            try:

                title = WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located((By.XPATH, r"// h1[ @class ='entry-title']"))  # title for all except 37th

                    )
                if os.path.exists(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt"):
                    os.remove(f"{(os.getcwd()[:])}/text files/{file_name}.txt")
                file1 = open(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt", "a",encoding="utf-8")  # append mode
                file1.write(f"Title : {title.text} \n")
                # print(title.text)
            except Exception as e :
                title = WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[@class='tdb-title-text']"))  # element for 37th type
                )
                # print(title.text)
                if os.path.exists(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt"):
                    os.remove(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt")
                file1 = open(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt", "a",encoding="utf-8")  # append mode
                file1.write(f"Title : {title.text} \n")
                # title = browser.find_element(By.XPATH, r"// h1[ @class ='entry-title']")

            try:

                text = WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH, r"//html[1]/body[1]/div[6]/article[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p"))
                    # text for all except 37th
                )
                headers = [h.text for h in browser.find_elements(By.XPATH,
                                                                 r"//html[1]/body[1]/div[6]/article[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p")]

                file1.write("Text :  \n")
                for i in headers:
                    # print(i)
                    # file1 = open(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt", "a")  # append mode
                    file1.write(f"{i} \n")
            except Exception as e:
                text = WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    r"/html[1]/body[1]/div[6]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/div[1]"))
                    # text for 37th type
                )
                headers = [h.text for h in browser.find_elements(By.XPATH,
                                                                 r"/html[1]/body[1]/div[6]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/div[1]")]
                file1.write("Text :  \n")
                for i in headers:
                    # print(i)
                    # file1 = open(f"{(os.getcwd()[:])}\\text files\\{file_name}.txt", "a")  # append mode
                    file1.write(f"{i} \n")


                try:
                    file1.close()
                except Exception as e:
                    print(e)
        else:
            print(f"{file_name} contains 404 error")
            with open("Error_Files.txt","a",encoding='utf-8') as f:
                f.write(f"{file_name} \n")
                f.close()
    else:
        print(f"{file_name} aldready scraped")

# url = (data["URL"][0])
# file_name = (data["URL_ID"][0])
# scrap(file_name,url)

# as iterrows gives generator hence storing all elemets in list for slicing required fields like url and url id
if __name__=="__main__":
    # print("true")
    lst = list()
    for i in data.iterrows():
        lst.append((i[1]))

    # scrapping from all urls usng for loop.
    # for i in range(len(os.listdir("text files")),len(lst)):
    for i in range(len(lst)):
        # print(i, " ", lst[i][0],lst[i][1])
        scrap(lst[i][0],lst[i][1])