from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

mainURL = "https://translate.google.com"
spanishURL = "#view=home&op=translate&sl=en&tl=es"
germanURL = "#view=home&op=translate&sl=en&tl=de"

repeat = True

chrome_options = Options()
chrome_options.add_argument("--headless")

while repeat:

    languageChoice = input("\nWhich language would you like to translate to? \nSpanish? Type '1' \nGerman? Type '2' \nEnter Here: ")

    try:

        if int(languageChoice) in range(1, 3):

            userInput = input("Enter the word/phrase you would like to be translated: ")

            print("Calculating...")

            driver = webdriver.Chrome((r"C:\Users\Colten\Desktop\Drivers\chromedriver.exe"), options=chrome_options)

            if int(languageChoice) == 1:

                driver.get(f"https://translate.google.com/{spanishURL}")

            elif int(languageChoice) == 2:

                driver.get(f"https://translate.google.com/{germanURL}")

            time.sleep(float(.5))

            driver.find_element_by_id("source").send_keys(userInput)

            time.sleep(float(.5))

            translated = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span").text

            print("\n" + translated)

            runAgain = input("\nTranslate again? Type 'q' to quit or press any other key to translate again: \n")

            if runAgain == "q":
                repeat = False
            else:
                repeat = True

        else:
            print("Please make a valid number choice, either 1 or 2\n")

    except Exception as e:
        print("Please make a valid number choice.\n")
        continue
