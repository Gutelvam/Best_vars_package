from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='best_vars_pk',
      version='0.1.8',
      description='Bestvars feature_selection methods',
      packages=['best_vars_pk'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      author = 'Gutelvam Rodrigues de Jesus',
      author_email = 'gutto.rdj@gmail.com',
      zip_safe=False)