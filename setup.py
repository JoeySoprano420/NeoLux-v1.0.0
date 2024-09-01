from setuptools import setup, find_packages

setup(
    name='NeoLux',
    version='1.0.0',
    author='Joey Soprano',
    author_email='violetaurac@icloud.com',
    description='LuxLang: A refined programming language with elegant syntax and dynamic features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoeySoprano420/NeoLux',
    packages=find_packages(),
    install_requires=[
        # List of dependencies (filled in requirements.txt)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MODIFIED QSRLC License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MODIFIED QSRLC License',
    license_files=('LICENSE.md',),
)
