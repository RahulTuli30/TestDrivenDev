from selenium import webdriver
import os

def testDjango():
    print(os.getcwd())
    browser = webdriver.Chrome("../chromedriver")
    browser.get("http://localhost:8000")
    assert 'Django' in browser.title, "Django not up and running!"


def main():
    testDjango()


if __name__ == "__main__":
    main()
