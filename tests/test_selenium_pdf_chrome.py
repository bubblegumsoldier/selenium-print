import unittest
import os
import sys
import time

# Add the parent directory of seleniumprint to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from seleniumprint import SeleniumPDF, file_to_pdf, url_to_pdf

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")


class SeleniumPDFTest(unittest.TestCase):
    def test_generate_pdf_utility_method(self):
        # Get absolute path to current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to HTML file relative to current script
        html_file_path = os.path.join(script_dir, "test.html")

        # Build path to output PDF file
        pdf_file_path = os.path.join(script_dir, "test_direct.pdf")

        # Generate PDF from HTML file path
        file_to_pdf(
            html_file_path, pdf_file_path, chrome_driver_path=CHROME_DRIVER_PATH
        )

        # Assert that PDF file was created
        self.assertTrue(os.path.isfile(pdf_file_path))

        # Construct URL based on html file path
        url = "file://" + html_file_path

        # Build path to output PDF file
        pdf_file_path_url = os.path.join(script_dir, "test_direct_url.pdf")

        # Generate PDF using URL instead of file path
        url_to_pdf(
            url,
            pdf_file_path_url,
            chrome_driver_path=CHROME_DRIVER_PATH,
            additional_arguments=["--lang=en"],
            additional_browser_options={'irrelevant-custom-arg': True}
        )

        # Assert that PDF file was created with URL, too
        self.assertTrue(os.path.isfile(pdf_file_path_url))

    def test_generate_pdf(self):
        # Get absolute path to current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to HTML file relative to current script
        html_file_path = os.path.join(script_dir, "test.html")

        # Build path to output PDF file
        pdf_file_path = os.path.join(script_dir, "test.pdf")

        # Initialize SeleniumPDF
        selenium_pdf = SeleniumPDF(chrome_driver_path=CHROME_DRIVER_PATH)

        # Generate PDF from URL
        url = "file://" + html_file_path
        selenium_pdf.url_to_pdf(url, pdf_file_path)

        # Assert that PDF file was created
        self.assertTrue(os.path.isfile(pdf_file_path))

        # Won't remove pdf as it will be an artifact in the actions

    def test_no_auto_init(self):
        # Get absolute path to current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to HTML file relative to current script
        html_file_path = os.path.join(script_dir, "test.html")

        # Build path to output PDF file
        pdf_file_path = os.path.join(script_dir, "test.pdf")

        # Initialize SeleniumPDF
        selenium_pdf = SeleniumPDF(chrome_driver_path=CHROME_DRIVER_PATH, auto_start=False)

        # Driver in chrome driver must be None
        self.assertFalse(hasattr(selenium_pdf.driver, 'driver'))

        # Now init manually
        selenium_pdf.init()

        # Driver in chrome driver must not be None
        self.assertNotEqual(getattr(selenium_pdf.driver, 'driver'), None)

        # Quit again - no need to generate pdf now... just testing the auto start here
        selenium_pdf.quit()


    def test_generate_pdf_with_bytes_returned(self):
        # Get absolute path to current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to HTML file relative to current script
        html_file_path = os.path.join(script_dir, "test.html")

        # Initialize SeleniumPDF
        selenium_pdf = SeleniumPDF(chrome_driver_path=CHROME_DRIVER_PATH)

        # Generate PDF from URL and get raw bytes
        url = "file://" + html_file_path
        pdf_bytes = selenium_pdf.url_to_pdf(url)

        # Assert that raw bytes were returned
        self.assertIsInstance(pdf_bytes, bytes)

    def test_generate_pdf_with_sleep(self):
        # Get absolute path to current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to HTML file relative to current script
        html_file_path = os.path.join(script_dir, "test.html")

        # Initialize SeleniumPDF
        selenium_pdf = SeleniumPDF(chrome_driver_path=CHROME_DRIVER_PATH)

        # Load page and convert to PDF without sleeping
        url = "file://" + html_file_path

        # Load page and wait for 2 seconds
        selenium_pdf.load_page(url)
        time.sleep(2)

        # Convert page to PDF and get raw bytes
        pdf_bytes_2 = selenium_pdf.convert_current_page_to_pdf()

        # Assert that PDF bytes were returned
        self.assertIsInstance(pdf_bytes_2, bytes)


if __name__ == "__main__":
    unittest.main()
