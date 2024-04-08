from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='masonite-ide-helper',
    version='0.1.0',
    author='Jarriq Rolle',
    author_email='jrolle@baysidetechgroup.com',
    description='A utility for generating Python type hinting stub files for Masonite ORM models.',
    long_description='A utility for generating Python type hinting stub files for Masonite ORM models.',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/masonite-ide-helper',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.9',
    install_requires=[
        "masonite-orm"
    ],
)
