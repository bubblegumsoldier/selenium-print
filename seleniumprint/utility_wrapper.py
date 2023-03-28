from typing import List, Union
from .drivers import ISeleniumPDFDriver, ChromePDFDriver
from .selenium_pdf import SeleniumPDF


def url_to_pdf(
    url: str,
    output_path: Union[str, None] = None,
    pdf_driver: ISeleniumPDFDriver = ChromePDFDriver(),
    additional_browser_options: dict = {},
    additional_arguments: List[str] = [],
    *args,
    **kwargs,
) -> Union[bytes, None]:
    driver = SeleniumPDF(
        pdf_driver=pdf_driver,
        additional_browser_options=additional_browser_options,
        additional_arguments=additional_arguments,
        auto_start=True,
        *args,
        **kwargs,
    )
    return driver.url_to_pdf(url=url, output_path=output_path)


def file_to_pdf(
    file_path: str,
    output_path: Union[str, None] = None,
    pdf_driver: ISeleniumPDFDriver = ChromePDFDriver(),
    additional_browser_options: dict = {},
    additional_arguments: List[str] = [],
    *args,
    **kwargs,
) -> Union[bytes, None]:
    driver = SeleniumPDF(
        pdf_driver=pdf_driver,
        additional_browser_options=additional_browser_options,
        additional_arguments=additional_arguments,
        auto_start=True,
        *args,
        **kwargs,
    )
    return driver.file_to_pdf(file_path=file_path, output_path=output_path)
