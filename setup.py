from distutils.core import setup

setup(name='pinkie',
      version='1.0.1',
      license='MIT',
      description='Maybe the smallest machine-learning library',
      author='Jonas Weimar',
      author_email='None',
      url='https://github.com/jonas-weimar/pinkie',
      packages=['pinkie', 'pinkie.mlp', 'pinkie.knn'],
      install_requires=[
          'termcolor',
          'tqdm',
          'numpy',
      ],
      download_url="https://github.com/jonas-weimar/pinkie.git",
     )
