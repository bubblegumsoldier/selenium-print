import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="selenium-print",
    packages=setuptools.find_packages(),
    version="1.0.0",
    license="MIT",
    description="A minimal printing utility based on selenium and chrome that is able to render any HTML to PDF.",
    author="Henry Müssemann",
    author_email="henry@muessemann.de",
    url="https://github.com/bubblegumsoldier/selenium-print",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["print", "pdf", "converter", "selenium"],
    install_requires=['selenium'],
)
