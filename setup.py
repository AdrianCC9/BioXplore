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
        'torch',
        'pandas',
        'numpy',
        'scikit-learn',
        'biopython',
        'flask',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
