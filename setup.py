from setuptools import setup
setup(
  name = 'CuttApi',         # How you named your package folder (MyLib)
  packages = ['CuttApi'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'One of the best ways of shortening URLs using Cuttly URL shortener just by entering your API key and seeing the rest that is done automatically by the Module',   # Give a short description about your library
  author = 'Devraj Therani',                   # Type in your name
  author_email = 'ttctlc96e@mozmail.com',      # Type in your E-Mail
  url = 'https://github.com/devrajtherani/CuttApi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/devrajtherani/CuttApi/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['API', 'SIMPLE', ''],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'urllib3',
          'pyperclip'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
