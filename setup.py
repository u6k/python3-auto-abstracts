from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='auto_abstracts',
    version='1.0.0',
    description='The Automatic Creation of Literature Abstracts',
    long_description=readme,
    author='Chimera',
    author_email='ai-brain-lab@accel-brain.com',
    maintainer='u6k Apps',
    maintainer_email='u6k.apps@gmail.com',
    url='https://github.com/u6k/python3-auto-abstracts',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['mecab-python3', 'pyquery', 'nltk', 'numpy', 'pycrypto', 'six', 'pdfminer.six']
)
