from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):

    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")

    context.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    context.driver.maximize_window()





def after_scenario(context, scenario):

    context.driver.quit()

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()




## HEADLESS MODE ####
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# context.driver = webdriver.Chrome(
#     options=options
# )

## BROWSERSTACK ###
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
# bs_user = 'elaineoblitey_GqhT0b'
# bs_key = 'mPoZG7heZ47ii87ukpPg'
# url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#
# options = Options()
# bstack_options = {
#     "os" : "Windows",
#     "osVersion" : "11",
#     'browserName': 'Chrome',
#     'sessionName': scenario_name,
# }
# options.set_capability('bstack:options', bstack_options)
# context.driver = webdriver.Remote(command_executor=url, options=options)

# context.driver.maximize_window()

