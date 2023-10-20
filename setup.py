from setuptools import setup, find_packages

# Use https://packaging.python.org/en/latest/guides/tool-recommendations/ to verify the sea of tools
# that exist to help with packaging. For this example we will use setuptools
# Build a wheel with: python setup.py bdist_wheel and install the pre-required package (wheel)


# read the requirements.txt file and use it to install dependencies
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='fortune-cookie-demo',
    description='demo python CLI tool to generate random fortunes',
    packages=find_packages(),
    author='Simrun & Afraa',
    entry_points="""
    [console_scripts]
    fortune=src.main:main
    """,
    #install_requires=['click==7.1.2'],
    install_requires=install_requires,
    version='0.0.1',
    url= "https://github.com/nogibjj/week7_afraa_simrun_fortune_cookie",
)