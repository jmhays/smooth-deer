import setuptools
import os


package_dir = os.path.abspath('src')


if __name__ == "__main__":
    setuptools.setup(
        name='smooth_deer',
        version='0.0.1',
        description='Package to run smooth DEER distributions',
        author='Jennifer Hays',
        author_email='jmh5sf@virginia.edu',
        url="https://github.com/jmhays/smooth-deer",
        license='LGPL-2.1',
        packages=setuptools.find_packages(),
        install_requires=[],
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },
        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=False,
    )
