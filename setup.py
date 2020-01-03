from setuptools import setup, find_packages


setup(
    name="py-find-injection",
    version="0.1.1",
    author="James Brown",
    author_email="jbrown@uber.com",
    url="https://github.com/uber/py-find-injection",
    description="simple python ast consumer which searches for common SQL injection attacks",
    license='MIT (Expat)',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Security",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "py-find-injection = py_find_injection:main",
        ]
    },
    tests_require=["nose", "mock"],
    test_suite="nose.collector",
    long_description="""py_find_injection

Walks the AST and looks for arguments to cursor.execute or session.execute; then
determines whether string interpolation, concatenation or the .format() call is used
on those arguments. Not at all comprehensive, but better than nothing.
"""
)
