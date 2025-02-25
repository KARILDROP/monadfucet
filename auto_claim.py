from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Address yang akan diklaim
ADDRESS = "0xE01673C4dFbEcCc6e545A4BF36E35977e8d51Db6"
FAUCET_URL = "https://testnet.monad.xyz/"

# Setup driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run tanpa tampilan UI (opsional)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    driver.get(FAUCET_URL)
    time.sleep(3)  # Tunggu loading

    # Masukkan address
    input_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter your address']")
    input_box.send_keys(ADDRESS)
    time.sleep(1)

    # Klik tombol "Claim"
    claim_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Claim')]")
    claim_button.click()
    time.sleep(3)  # Tunggu proses klaim

    print("Faucet claimed successfully!")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
