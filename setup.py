from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='MacAppOpener',
  version='0.0.1',
  description='A simple python module that offers a MacOS alternative to the AppOpener module.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ryann Elguessab',
  author_email='ryannelguessab@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='app' 'MacOS', 
  packages=find_packages(),
  install_requires=[''] 
)