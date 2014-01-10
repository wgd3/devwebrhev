from setuptools import setup

setup(name='WebRHEV',
      version='0.1',
      description='Minimalist web app for analyzing RHEV databases',
      author='Wallace Daniel',
      author_email='wdaniel@redhat.com',
      url='http://webrhev-wdaniel.itos.redhat.com',
      install_requires=['Flask>=0.10.1', 'MarkupSafe','Jinja2>=2.7.1']
     )
