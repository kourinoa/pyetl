from selenium.webdriver import Chrome


def main():
    driver = Chrome("./chromedriver")
    driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https"
               "%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next"
               "%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253Fgl%253DTW%2526tab%253Dw1&hl=zh-TW&ec=65620&flowName"
               "=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element_by_id("identifierId").send_keys("djflsdflkl")
    driver.find_element_by_css_selector("span.RveJvd.snByac").click()


if __name__ == '__main__':
    main()
