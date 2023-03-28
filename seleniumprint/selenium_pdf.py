from typing import List, Union
from selenium import webdriver

from seleniumprint.drivers import ISeleniumPDFDriver, ChromePDFDriver


def _file_path_to_url(file_path: str) -> str:
    return f"file://{file_path}"


class SeleniumPDF:
    """
    A class for rendering HTML to PDF using the Selenium framework.

    Attributes:
        driver (ISeleniumPDFDriver): The PDF driver to use.
        additional_browser_options (dict): Additional browser options to use.
        additional_arguments (List[str]): Additional arguments to use.
        extra_args: Extra arguments to pass to the driver initialization.
        extra_kwargs: Extra keyword arguments to pass to the driver initialization.
    """

    driver: ISeleniumPDFDriver = None
    additional_browser_options: dict = None
    additional_arguments: dict = None
    extra_args = None
    extra_kwargs = None

    def __init__(
        self,
        pdf_driver: ISeleniumPDFDriver = None,
        additional_browser_options: dict = {},
        additional_arguments: List[str] = [],
        auto_start: bool = True,
        *args,
        **kwargs,
    ):
        """
        Initializes a new instance of the SeleniumPDF class.

        Args:
            pdf_driver (ISeleniumPDFDriver): The PDF driver to use. Defaults to ChromePDFDriver().
            additional_browser_options (dict): Additional browser options to use. Defaults to an empty dictionary.
            additional_arguments (List[str]): Additional arguments to use. Defaults to an empty list.
            auto_start (bool): Whether to automatically start the driver. Defaults to True.
            *args: Extra arguments to pass to the driver initialization.
            **kwargs: Extra keyword arguments to pass to the driver initialization.
        """
        self.driver = pdf_driver
        if not self.driver:
            self.driver = ChromePDFDriver()
        self.additional_browser_options = additional_browser_options
        self.additional_arguments = additional_arguments
        self.extra_args = args
        self.extra_kwargs = kwargs
        if not auto_start:
            return
        self.init()

    def init(self):
        """
        Initializes the driver with the specified options and arguments.
        """
        self.driver.init_driver(
            self.additional_browser_options,
            self.additional_arguments,
            *self.extra_args,
            **self.extra_kwargs,
        )

    def load_page(self, url):
        """
        Loads the specified URL in the driver.

        Args:
            url (str): The URL to load.
        """
        self.driver.load_page(url)

    def _save_bytes_to_file(self, raw_bytes: bytes, file_path: str):
        """
        Saves the specified raw bytes to a file.

        Args:
            raw_bytes (bytes): The raw bytes to save.
            file_path (str): The file path to save to.
        """
        with open(file_path, "wb") as f:
            f.write(raw_bytes)

    def convert_current_page_to_pdf(self, output_path=None) -> Union[bytes, None]:
        """
        Converts the current page to a PDF.

        Args:
            output_path (str): The file path to save the PDF to. Defaults to None.

        Returns:
            bytes: The raw PDF bytes if output_path is not specified, otherwise None.
        """
        raw_bytes = self.driver.convert_current_page_to_pdf()
        if not output_path:
            return raw_bytes
        self._save_bytes_to_file(raw_bytes, output_path)

    def url_to_pdf(self, url, output_path=None, auto_quit=True):
        """
        Loads the specified URL and converts it to a PDF.

        Args:
            url (str): The URL to load and convert.
            output_path (str): The file path to save the PDF to. Defaults to None.

        Returns:
            bytes: The raw PDF bytes if output_path is not specified, otherwise None.
        """
        self.load_page(url)
        result = self.convert_current_page_to_pdf(output_path)
        if auto_quit:
            self.driver.quit()
        return result

    def file_to_pdf(self, file_path, output_path=None, auto_quit=True):
        return self.url_to_pdf(
            _file_path_to_url(file_path), output_path=output_path, auto_quit=auto_quit
        )
    
    def quit(self):
        self.driver.quit()
