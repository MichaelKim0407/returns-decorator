from setuptools import setup

from returns import __version__

extra_test = [
    'pytest>=4',
    'pytest-runner>=4',
    'pytest-cov>=2',
]
extra_dev = extra_test

extra_ci = extra_test + [
    'python-coveralls',
]

setup(
    name='returns-decorator',

    version=__version__,

    extras_require={
        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

    py_modules=['returns'],

    url='https://github.com/MichaelKim0407/returns-decorator',

    license="MIT",

    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",

        "Topic :: Software Development :: Libraries",
    ]
)
