# githubcommit
githubcommit is a jupyterhub extension enabling users push ipython notebooks nad scripts to a git repo.

A git button gets displayed in the notebook toolbar.

After saving any notebook
the user can push notebook to pre-specified git repository.

There are few environment variables that must be exported, currently this extension supports
commits to a single github repo defined in environment variable.

## Installation
You can currently install this directly from git:

```
pip install git+https://github.com/DanielCarmel/jupyterhub-githubcommit.git
jupyter nbextension install githubcommit --py --system
jupyter nbextension enable githubcommit --py --system
jupyter serverextension enable githubcommit --py --system
```
## Steps
I have made this short video in which I install the extension from scratch (click on the image)- 

* Install package using above commands
* Create Git repo where notebooks will be pushed if not already exists and clone it in your `GIT_PARENT_DIR`
* Clone this repo as well in your `GIT_PARENT_DIR` directory
* Replace the values in env.sh present in this repo itself
* Run the command - source ~/githubcommit/env.sh
* Configure ssh key (present in ~/.ssh/id_rsa.pub or specified location) in github account
* Run jupyter notebook from within your repo directory

## Example git configuration
export GIT_PARENT_DIR=~ <br/>
export GIT_REPO_NAME=gitjupyter <br/>
export GIT_BRANCH_NAME=master <br/>
export GIT_USER=DanielCarmel <br/>
export GIT_EMAIL=danielcarmel6@gmail.com <br/>
export GITHUB_ACCESS_TOKEN=github-access-token <br/>
export GIT_USER_UPSTREAM=DanielCarmel <br/>

## Credits
Thanks to https://github.com/Lab41/sunny-side-up for laying the foundation of this extension.

Thanks to https://github.com/sat28 for making this extension for Jupyter notebook.

Thanks to https://github.com/DanielCarmel for adding support for Jupyterhub.
