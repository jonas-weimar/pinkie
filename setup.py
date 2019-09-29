from distutils.core import setup

setup(name='pinkie',
      version='1.0.15',
      license='MIT',
      description='Maybe the smallest machine-learning library',
      author='Jonas Weimar',
      author_email='None',
      url='https://github.com/jonas-weimar/pinkie',
      packages=['pinkie', 'pinkie.mlp', 'pinkie.knn', 'pinkie.regression'],
      install_requires=[
          'termcolor',
          'tqdm',
          'numpy==1.16.1',
          'scipy'
      ],
      download_url="https://github.com/jonas-weimar/pinkie.git",
     )
