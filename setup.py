from distutils.core import setup

setup(name='pinkie',
      version='1.0',
      description='Small Neural Network',
      author='Jonas Weimar',
      author_email='jonas-weimar@web.de',
      url='https://github.com/jonas-weimar/pinkie',
      packages=['.', '.mlp'],
      install_requires=[
          'termcolor',
          'tqdm',
          'numpy',
      ],
     )
