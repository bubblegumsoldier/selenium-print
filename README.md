# selenium-print

`selenium-print` is an open-source Python package that enables printing HTML to PDF using the Selenium framework. This package is especially useful when you want to render dynamic content that requires a JS engine or ajax calls to a server or complex layouts using state-of-the-art CSS like grid, flexbox, media queries or transform.

Note: This library uses [selenium](https://github.com/SeleniumHQ/selenium) which in turn requires the installation of the Google Chrome browser as well as a chromedriver. This library does not support any other browser at the moment. This makes it **not a lightweight solution** for generating PDF files. But it does make an easy to setup PDF generation solution that supports ALL browser functionality. Also note that starting a selenium browser is not very fast either, so if your priority is not ease-of-use, but performance, this is not the library for you. Although in benchmarks with [weasyprint](https://github.com/Kozea/WeasyPrint), which seems to also have one of the most impressive HTML/CSS support, this framework beat it by an average of 33% time decrease.

## Features

- Utilizes the full flexibility of the JS engine of the browser.
- Supports ajax calls to the server.
- Renders HTML to PDF.
- Easy to install and use.

## Installation

You can install `selenium-print` using pip:

```bash
pip install selenium-print
```

## Usage

### Simple usage

The simplest way to use selenium-print is to use the utility method that wraps all logic.

```python
from seleniumprint import file_to_pdf, url_to_pdf

input_html_file_path="/Users/user/path/to/input.html"
output_pdf_file_path="/Users/user/path/to/output.pdf"

file_to_pdf(input_html_file_path, output_pdf_file_path)

input_html_url="http://localhost:8000/report/1"
output_pdf_file_path="./report_pdfs/report_1.pdf"

url_to_pdf(input_html_url, output_pdf_file_path)
```

### Class-Based Usage

Another way to use SeleniumPDF is to call the url_to_pdf method with a URL and an optional output file path:

```python
from seleniumprint import SeleniumPDF

url = "https://www.example.com"
pdf_file_path = "example.pdf"

# Initialize SeleniumPDF
selenium_pdf = SeleniumPDF()

# Generate PDF from URL
selenium_pdf.url_to_pdf(url, pdf_file_path)`
```

In this example, `SeleniumPDF` is initialized with the default options and the `url_to_pdf` method is called with a URL and an output file path. The page at the specified URL is loaded and then converted to a PDF, which is saved to the specified file path, if an output file path was provided. If not it will return the raw bytes that you can work with.

### Custom Waiting

If you need to wait for some time after loading the page before converting it to a PDF, you can use the `load_page` and `convert_current_page_to_pdf` methods separately and add a sleep in between or some other kind of waiting logic, e.g. a JS based logic. Here's an example:

```python
from seleniumprint import SeleniumPDF
import time

url = "https://www.example.com"
pdf_file_path = "example.pdf"

# Initialize SeleniumPDF
selenium_pdf = SeleniumPDF()

# Load page and wait for 5 seconds
selenium_pdf.load_page(url)
time.sleep(5)

# Convert page to PDF and save to file
selenium_pdf.convert_current_page_to_pdf(pdf_file_path)

## Alternative JS-based waiting (needs appropriate HTML-side implementation)

selenium_pdf.load_page(url)

# wait manually until page is ready or some other condition is true
while selenium_pdf.driver.driver.execute_js("return window.readyState !== 'complete'"):
  time.sleep(0.5)

# Convert page to pdf now
selenium_pdf.convert_current_page_to_pdf(pdf_file_path)

```

In this example, `load_page` is called to load the page at the specified URL, and then a 5-second wait is added using the `time.sleep` function. Finally, `convert_current_page_to_pdf` is called to convert the loaded page to a PDF and save it to the specified file path.

### Specifying chromedriver location

The constructor of `SeleniumPDF` as well as the utility method `file_to_pdf` and `url_to_pdf` take a chrome-driver specific argument called `chrome_driver_path`.

```python
# Build path to HTML file relative to current script
html_file_path = os.path.join(script_dir, "test.html")

# Build path to output PDF file
pdf_file_path = os.path.join(script_dir, "test_direct.pdf")

# Generate PDF from HTML File Path
file_to_pdf(html_file_path, pdf_file_path, chrome_driver_path=CHROME_DRIVER_PATH)
```

## Contributing

Contributions are welcome! Here are some ways you can contribute:

- Report issues and bugs.
- Suggest new features or enhancements.
- Submit pull requests for bug fixes or new features.

Before submitting a pull request, please make sure that your code follows PEP 8 guidelines and includes tests.

## Support

This is a personal project, so support may be limited. However, I will do my best to answer any issues that are reported.

## License

This project is published under MIT license which means its basically free to use for everyone in any way whatsoever.
