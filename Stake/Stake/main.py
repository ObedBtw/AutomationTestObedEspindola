from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    options = Options()
    options.add_argument("--headless")
    driver_path = "./chromedriver.exe"
    website = "https://stake.com/?gad_source=1&gad_campaignid=22459486521&gbraid=0AAAAA_XBMpdl6BJDHNVYXi_x_N4WmrG4E&gclid=CjwKCAjwtrXFBhBiEiwAEKen16pTXtQ5OXQBQIAQ1UCUmbe4-s_f8L-pPsLMR9iFFldMWKdbt5JSDRoCx1gQAvD_BwE"

    # Selenium Configuration
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(options=options, service=service)

    driver.get(website)

    # Wallet Button action
    wallet_button = driver.find_element(
        by=By.XPATH, value='//div[@class="balance-toggle svelte-17vz5au"]/button'
    )

    wallet_button.click()

    # Waitn until modal appears
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_all_elements_located(
            (
                By.CLASS_NAME,
                "rounded-md bg-cover bg-center relative w-full min-w-[200px] max-w-[500px] max-h-[calc(100%-4em)] flex flex-col bg-grey-600 text-grey-200 overflow-hidden",
            )
        )
    )

    # Deposit button action
    wallet_deposit_button = driver.find_element(
        by=By.XPATH, value='//button[@data-testid="wallet-nav-deposit"]'
    )

    wallet_deposit_button.click()

    time.sleep(2)

    directly_deposit_button = driver.find_element(
        by=By.XPATH,
        value='//button[@class="inline-flex relative items-center gap-2 justify-center rounded-(--ds-radius-md,0.25rem) font-semibold whitespace-nowrap ring-offset-background transition disabled:pointer-events-none disabled:opacity-50 focus-visible:outline-2 focus-visible:outline-offset-2 active:scale-[0.98] bg-grey-400 text-white hover:bg-grey-300 hover:text-white focus-visible:outline-white text-sm leading-none shadow-md py-[0.8125rem] px-[1rem] w-full" and @tabindex=0]',
    )

    directly_deposit_button.click()

    time.sleep(3)

    accounts_list = driver.find_elements(by=By.XPATH, value='//div[@role="listbox"]')

    coinbase_button = [
        account.find_element(by=By.XPATH, value='//div[@role="listbox"]/button/span')
        for account in accounts_list
        if account.text.strip().lower() == "coinbase"
    ][0]

    coinbase_button.click()

    driver.quit()


if __name__ == "main":
    main()
