from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'printing_data', 'pricing_info'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
