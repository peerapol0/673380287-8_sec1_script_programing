import json
import time
from pathlib import Path
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def save_data_to_json(data: list[dict[str, Any]], filepath: str):
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)


def wait_for_element(driver, selector: str, timeout: int = 10):
    return WebDriverWait(timeout=timeout, driver=driver).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


def safe_click(driver, element: WebElement):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    WebDriverWait(driver, 10).until(lambda current_driver: element.is_enabled())
    element.click()
    time.sleep(0.5)
