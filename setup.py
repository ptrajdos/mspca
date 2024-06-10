from setuptools import setup, find_packages

setup(
    name='mspca',
    version='0.0.4',
    py_modules=['mspca'],
    install_requires=[
        'PyWavelets>=1.1.1',
        'numpy',
        'pandas',
        'scikit-learn',
    ],
    
    author='',
    author_email='',
    description='mspca',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ptrajdos/mspca',
    python_requires='>=3.6',
)
