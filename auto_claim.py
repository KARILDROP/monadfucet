import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Konfigurasi WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Jalankan tanpa tampilan GUI (opsional)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Path ke WebDriver (ganti sesuai dengan lokasi chromedriver Anda)
driver_path = "path/to/chromedriver"

# Alamat wallet Monad Tesnet
wallet_address = "0xE01673C4dFbEcCc6e545A4BF36E35977e8d51Db6"

# Fungsi untuk klaim faucet
def claim_faucet():
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    
    try:
        driver.get("https://testnet.monad.xyz/")
        time.sleep(5)  # Tunggu loading halaman

        # Temukan input wallet address
        wallet_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your wallet address']")
        wallet_input.send_keys(wallet_address)
        wallet_input.send_keys(Keys.RETURN)
        time.sleep(2)

        # Klik tombol claim
        claim_button = driver.find_element(By.XPATH, "//button[contains(text(),'Request Funds')]")
        claim_button.click()
        time.sleep(5)

        print("✅ Faucet claimed successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        driver.quit()

# Menjalankan bot setiap 12 jam
schedule.every(12).hours.do(claim_faucet)

print("🚀 Bot faucet berjalan...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Cek setiap 60 detik
