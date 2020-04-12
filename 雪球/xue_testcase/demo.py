from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.xueqiu.trade.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["automationName"] = 'uiautomator2'
caps["sessionId"]=["f48c595c-634f-4893-a921-4e174a7afa4e"]

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath("//*[@text='自选']")
el1.click()
