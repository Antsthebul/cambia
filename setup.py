import setuptools

with open('README.md', 'r', encoding="utf=8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "switch_mode",
    version = "0.0.1",
    author = "Antsthebul",
    author_email = "anthony.allen.srt@gmail.com",
    description = "Easy way to swap test variables/code blocks",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/Antsthebul/cambia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent"
    ],
    python_require = '>=python3.6',
    entry_points={
        'console_scripts':[
            "cambia=cambia.__main__:main"
        ]    }
)