from setuptools import setup, find_packages

setup(
    name='BioXplore',
    version='0.1.0',
    author='Adrian Caricari',
    author_email='adrian.caricari9@gmail.com',
    description='A tool for exploring genetic influences on fitness traits',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/BioXplore',
    packages=find_packages(),
    install_requires=[
        'torch>=1.7.1',
        'pandas>=1.2.0',
        'numpy>=1.19.5',
        'scikit-learn>=0.24.0',
        'biopython>=1.78',
        'flask>=1.1.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
