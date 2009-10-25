from setuptools import setup

version = '0.1.1'

setup_args = dict(
    name='trie',
    version=version,
    description=('A prefix tree (trie) implementation.'),
    author='David Hain',
    author_email='dhain@spideroak.com',
    url='https://spideroak.com/code',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    py_modules=['trie'],
    test_suite='nose.collector',
    test_requires=['Nose'],
)

if __name__ == '__main__':
    setup(**setup_args)
