from selenium.webdriver import Chrome

def main():
    driver = Chrome("./chromedriver")
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)

    board = driver.find_element_by_css_selector("div.board-name")
    board.click()
    driver.find_element_by_css_selector("button.btn-big").click()

if __name__ == '__main__':
    main()