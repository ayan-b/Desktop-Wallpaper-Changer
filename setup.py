from setuptools import find_packages, setup

requirement_list = [r.strip()
                    for r in open('requirements.txt', 'r').readlines() if r]

LICENSE = "MIT"
KEYWORDS = [
    "wallpaper",
    "customization",
    "personalization",
]

CLASSIFIERS = [
    "Topic :: Personalization",
    "Programming Language :: Python",
    "Intended Audience :: All",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

if __name__ == '__main__':
    setup(
        name='dtwc',
        author='Ayan Banerjee',
        version='0.0.2',
        install_requires=requirement_list,
        description='Change your desktop wallpaper daily!',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        entry_points={
            'console_scripts': [
                'dwc = dwc.main:main'
            ],
        },
        license=LICENSE,
        keywords=KEYWORDS,
        python_requires='>=3.5',
        author_email='ayanbanerjee7777@gmail.com',
        url='https://github.com/ayan-b/Desktop-Wallpaper-Changer',
        packages=find_packages(),
    )
