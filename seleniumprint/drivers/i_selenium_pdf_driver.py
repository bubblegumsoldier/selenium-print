from abc import ABC, abstractmethod


class ISeleniumPDFDriver(ABC):
    @abstractmethod
    def init_driver(self, browser_options, *args, **kwargs):
        pass

    @abstractmethod
    def load_page(self, url, *args, **kwargs):
        pass

    @abstractmethod
    def convert_current_page_to_pdf(self, *args, **kwargs):
        pass

    def quit(self, *args, **kwargs):
        pass
