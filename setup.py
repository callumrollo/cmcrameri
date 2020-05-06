"""
setup.py for cmcrameri

"""
from distutils.core import setup
setup(
  name = 'cmcrameri',        
  packages = ['cmcrameri'],  
  version = '0.6',  
  license='MIT',   
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
)
