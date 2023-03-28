from typing import List, Union
from .drivers import ISeleniumPDFDriver, ChromePDFDriver
from .selenium_pdf import SeleniumPDF


def url_to_pdf(
    url: str,
    *args,
    output_path: Union[str, None] = None,
    pdf_driver: ISeleniumPDFDriver = ChromePDFDriver(),
    additional_browser_options: Union[dict, None] = None,
    additional_arguments: Union[List[str], None] = None,
    **kwargs,
) -> Union[bytes, None]:
    driver = SeleniumPDF(
        *args,
        pdf_driver=pdf_driver,
        additional_browser_options=additional_browser_options,
        additional_arguments=additional_arguments,
        auto_start=True,
        **kwargs,
    )
    return driver.url_to_pdf(url=url, output_path=output_path)


def file_to_pdf(
    file_path: str,
    *args,
    output_path: Union[str, None] = None,
    pdf_driver: ISeleniumPDFDriver = ChromePDFDriver(),
    additional_browser_options: Union[dict, None] = None,
    additional_arguments: Union[List[str], None] = None,
    **kwargs,
) -> Union[bytes, None]:
    driver = SeleniumPDF(
        *args,
        pdf_driver=pdf_driver,
        additional_browser_options=additional_browser_options,
        additional_arguments=additional_arguments,
        auto_start=True,
        **kwargs,
    )
    return driver.file_to_pdf(file_path=file_path, output_path=output_path)
