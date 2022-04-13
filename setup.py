import setuptools

setuptools.setup(
    name="githubcommit",
    version='0.1.0',
    url="https://github.com/DanielCarmel/jupyterhub-githubcommit",
    author="Daniel Carmel",
    description="Jupyterhub extension to enable user push notebooks to a git repo for multiple users",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'githubcommit': ['static/*']},
)
