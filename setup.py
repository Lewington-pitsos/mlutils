import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='mlutils',  
     version='0.1',
     scripts=['mlutils'] ,
     author="Louka Ewington-Pitsos",
     author_email="lewington@student.unimelb.edu.au",
     description="A machine learning utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Lewington-pitsos/mlutils",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )