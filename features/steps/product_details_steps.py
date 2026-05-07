from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
CLOSE_POPUP = (By.ID, 'VA_HEALTH_CONSENT_BUTTON')

@given('Open target product A-91269718 page')
def open_target(context):

    context.driver.get(
        'https://www.target.com/p/women-s-smocked-blouse-universal-thread-red/-/A-95081560?preselect=95162150#lnk=sametab'
    )

    # close popup if it appears
    try:
        popup = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable(CLOSE_POPUP)
        )
        popup.click()
    except:
        pass

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(COLOR_OPTIONS)
    )

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue', 'Brown', 'Red']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(c)
        )

        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print(repr(selected_color))
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'