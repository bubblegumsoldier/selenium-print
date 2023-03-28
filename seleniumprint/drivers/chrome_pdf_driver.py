import base64
from typing import Union
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH
from .i_selenium_pdf_driver import ISeleniumPDFDriver

class ChromePDFDriver(ISeleniumPDFDriver):
    driver = None
    def init_driver(
        self,
        *args,
        additional_browser_options: Union[dict, None] = None,
        additional_arguments: Union[list[str], None] = None,
        **kwargs
    ):
        additional_browser_options = additional_browser_options or {}
        additional_arguments = additional_arguments or []
        chrome_options = webdriver.ChromeOptions()
        for key in additional_browser_options:
            setattr(chrome_options, key, additional_browser_options[key])
        for arg in additional_arguments:
            chrome_options.add_argument(arg)
        app_state = {
            "recentDestinations": [
                {"id": "Save as PDF", "origin": "local", "account": ""}
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
        }
        prefs = {
            "printing.print_preview_sticky_settings.appState": json.dumps(app_state)
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--kiosk-printing")
        if not kwargs.get("disable_headless") is True:
            chrome_options.add_argument("--headless")
        chrome_driver_path = kwargs.get("chrome_driver_path") or DEFAULT_EXECUTABLE_PATH
        self.driver = webdriver.Chrome(
            executable_path=chrome_driver_path, options=chrome_options
        )

    def load_page(self, url, *args, **kwargs):
        self.driver.get(url)

    def convert_current_page_to_pdf(self, *args, **kwargs):
        self.driver.execute_script("return window.print()")
        pdf = self.driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
        pdf_data = base64.b64decode(pdf["data"])
        return pdf_data

    def quit(self, *args, **kwargs):
        self.driver.quit()
