from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='LightsCameraExtremism',
    version='0.1.30',
    description='A simulation of social network interactions using language models.',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'LightsCameraExtremism=LightsCameraExtremism.stage:main',
        ],
    },
)
