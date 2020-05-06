"""
setup.py for cmcrameri

"""
from setuptools import setup 

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'cmcrameri',        
  packages = ['cmcrameri'],  
  version = '0.9',  
  license='MIT',   
  long_description=long_description,
  long_description_content_type='text/markdown',
  description = 'Perceptually uniform colourmaps',   
  author = 'Callum Rollo',         
  author_email = 'c.rollo@outlook.com',      
  url = 'https://github.com/callumrollo/cmcrameri',  
  download_url = 'https://github.com/callumrollo/cmcrameri/v_01.tar.gz',  
  keywords = ['colormaps', 'oceanography', 'plotting', 'visualization'],
  install_requires=[         
          'matplotlib',
          'numpy',
      ],
  package_dir={'mypkg': 'cmcrameri'},     
  package_data={'cmcrameri': ['cmaps/*.txt']},
)
