# jupyterhub-githubcommit
jupyterhub-githubcommit is a jupyterhub extension enabling users push ipython notebooks nad scripts to a git repo.

A git button gets displayed in the notebook toolbar.

After saving any notebook
the user can push notebook to pre-specified git repository.

There are few environment variables that must be exported, currently this extension supports
commits to a single github repo defined in environment variable.

## Installation
You can install jupyterhub-githubcommit directly from git:

```
pip install git+https://github.com/DanielCarmel/jupyterhub-githubcommit.git
jupyter nbextension install githubcommit --py --system
jupyter nbextension enable githubcommit --py --system
jupyter serverextension enable githubcommit --py --system
```
## Steps
* Install package using above commands
* Create Git repo where notebooks will be pushed if not already exists.
* Replace the values in env.sh present in this repo itself
* Run the command - source ~/jupyterhub-githubcommit/env.sh
* Configure access token in github account
* Run jupyterhub

## Example git configuration
GIT_PARENT_DIR=~ <br/>
GIT_REPO_NAME=gitjupyter <br/>
GIT_BRANCH_NAME=master <br/>
GIT_USER=DanielCarmel <br/>
GIT_EMAIL=danielcarmel6@gmail.com <br/>
GITHUB_ACCESS_TOKEN=github-access-token <br/>
GIT_USER_UPSTREAM=DanielCarmel <br/>

## Credits
Thanks to https://github.com/Lab41/sunny-side-up for laying the foundation of this extension.

Thanks to https://github.com/sat28 for making this extension for Jupyter notebook.

Thanks to https://github.com/DanielCarmel for adding support for Jupyterhub.
