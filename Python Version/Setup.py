from setuptools import setup, find_packages

setup(
    name='NeoLux',
    version='1.0.0',
    author='Joey Soprano',
    author_email='violetaurac@icloud.com',
    description='NeoLux: A refined programming language with elegant syntax and dynamic features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoeySoprano420/NeoLux',
    packages=find_packages(),
    install_requires=[
        'regex==2024.9.1',
        'antlr4-python3-runtime==4.9.3',
        'numpy==1.24.2',
        'opencv-python==4.7.0.72',
        'textblob==0.17.1',
        'nltk==3.8.1',
        'networkx==3.1',
        'pytest==7.4.1',
        'scikit-learn==1.2.1',
        'matplotlib==3.8.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: V.A.C. Approved :: MODIFIED QSRLC License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MODIFIED QSRLC License',
    license_files=('LICENSE.md',),
    entry_points={
        'console_scripts': [
            'neolux=neolux.cli:main',
        ],
    },
    package_data={
        'neolux': ['data/*.json', 'data/*.xml'],
    },
    include_package_data=True,
)
