from setuptools import setup

setup(name='AuraMiddleware',
      version='0.1',
      author='Vinícius Matos da Silveira Fraga',
      author_email='vinicius.vmsf@gmail.com',
      packages=['aura',
                'aura.managers'],
      install_requires=[
          'zeroless',
          'paho-mqtt',
      ],
      entry_points = {
        'console_scripts': ['aura=aura.aura_worker:main'],
      }
      )