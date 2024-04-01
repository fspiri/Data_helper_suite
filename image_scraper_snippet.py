import os
import time
import requests  # Import the requests module
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import math
import io
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor


# Custom exception
class SpecificTimeoutException(Exception):
    pass


def urls_scraper(driver, max_images):
    def scroll_down():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up():
        driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    image_urls = []
    # waits until the thumbnails are loaded
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'islrg')))
    except Exception:
        raise SpecificTimeoutException("Loading Thumbnails")
    # starts the loading process of all the thumbnails.
    # the 15 is the amount of loaded pics for each scrolldown. To be tested.
    for i in range(math.ceil(max_images / 15) + 1):
        scroll_down()
        time.sleep(0.5)
    for i in range(math.ceil(max_images / 15) + 1):
        scroll_up()
        time.sleep(0.5)

    # makes sure tot_thumbs is initialized correctly
    retrieval_trials = 0
    tot_thumbs = driver.find_elements(By.CSS_SELECTOR, '.rg_i img, .Q4LuWd')
    while len(tot_thumbs) == 0 and retrieval_trials < 3:
        time.sleep(5)
        tot_thumbs = driver.find_elements(By.CSS_SELECTOR, '.rg_i img, .Q4LuWd')
        retrieval_trials += 1
    if len(tot_thumbs) == 0:
        print("Error retrieving data. Please check your connection and try again."
              "\nSometimes there are bugs if there is another application running not minimized, check for that.")
        driver.quit()
        quit()

    # loops through every element inside the tot_thumbs scan
    image_counter = 0
    for element in tot_thumbs:
        if image_counter < max_images:
            try:
                WebDriverWait(element.click(), 10)
                #time.sleep(0.25)

                images = driver.find_elements(By.CSS_SELECTOR, '.r48jcc, .pT0Scc, .iPVvYb')
                for img in images:
                    if img.get_attribute('src') and 'http' in img.get_attribute('src'):
                        image_urls.append(img.get_attribute('src'))
                        image_counter += 1
                    if img.get_attribute('src') in image_urls:
                        break
            except selenium.common.exceptions.ElementClickInterceptedException:
                pass
        else:
            WebDriverWait(driver.minimize_window(), 10)
            diff = int(input(f'The amount of requested pictures is reached. {image_counter} pics in total.\n'
                             f'There are still at most {len(tot_thumbs) - image_counter} pics that can be downloaded.'
                             f' How many more would you like to download?'
                             f'\nEnter 0 to finish the scraping and start with the download: '))
            print("=" * 30)

            if diff == 0:
                break
            if diff >= len(tot_thumbs) - image_counter:
                print("proceeding with the download of all the remaining pics")
                max_images = len(tot_thumbs)
                WebDriverWait(driver.maximize_window(), 10)
            else:
                max_images += diff
                WebDriverWait(driver.maximize_window(), 10)
    print("Scraping process done. Proceeding with the download.")

    return image_urls


def download_image(url, file_path):
    """
    :param url: url to download
    :param file_path: path to save
    :return: success. :type: bool
    """
    try:
        image_content = requests.get(url, stream=True).content  # Stream for large images
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        if image.format in ["JPEG", "PNG", "JPG"]:
            file_path_with_ext = f"{file_path}.{image.format.lower()}"
            with open(file_path_with_ext, "wb") as f:
                image.save(f, image.format)  # Preserve original format
            return True  # Signal successful download
    except Exception as e:
        print(f'FAILED - {url}: {e}')
        return False


def download_images(urls_list, query):
    """
    :param urls_list: list of urls of the images to download
    :param query: Query string
    :return: :type: void
    """
    dwn_path = os.path.join(os.getcwd(), "downloads", query)
    if os.path.exists(dwn_path):
        dwn_path = dwn_path if input("folder already existing, overwrite? [Y/N] ") == 'Y' else dwn_path+"_new"
    os.makedirs(dwn_path, exist_ok=True)  # Create directory if needed

    with ThreadPoolExecutor() as executor:  # Use threading for concurrency
        executor.map(
            download_image, urls_list,
            [os.path.join(dwn_path, str(i)) for i in range(len(urls_list))]
        )
    print(f"Images downloaded successfully.")


def open_browser(query):
    """
    :param: query :type: basestring
    """
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(search_url)
    WebDriverWait(driver, 30)
    try:
        if driver.current_url[0:16] == "https://consent.":
            WebDriverWait(driver.find_element(By.XPATH, "//button[@jsname = 'tWT92d']"), 50)
            driver.find_element(By.XPATH, "//button[@jsname = 'tWT92d']").click()
        else:
            WebDriverWait(driver.find_element(By.ID, 'W0wltc'), 50)
            driver.find_element(By.ID, 'W0wltc').click()
    except selenium.common.exceptions.NoSuchElementException:
        print("URL not valid:\n" + driver.current_url + "\nor Element not found")
    time.sleep(1)
    return driver


if __name__ == '__main__':
    query = input("Enter search query: ")
    n_images = int(input("Enter amount of images: "))
    driver = open_browser(query)
    # Checks that the page is correctly loaded. Solves most of the bugs even with low connection.
    reloads = 0
    try:
        urls_list = urls_scraper(driver, n_images)
    except SpecificTimeoutException as e:
        if reloads <= 3:
            reloads += 1
            driver.quit()
            driver = open_browser(query)
            urls_list = urls_scraper(driver, n_images)
        else:
            print("Error loading the page properly. If the error persists, raise an issue on the project page")
            quit()

    print(len(urls_list))
    driver.quit()
    download_images(urls_list, query)
