<div align = "center">

# ASL Translator
[![](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/download/releases/3.5.0/) 
[![GitHub issues](https://img.shields.io/github/issues/MLH-Fellowship/TeamKerberos_Pod1.0.2?logo=github)](https://github.com/MLH-Fellowship/TeamKerberos_Pod1.0.2/issues)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Size](https://github-size-badge.herokuapp.com/MLH-Fellowship/TeamKerberos_Pod1.0.2.svg)


[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/MLH-Fellowship/TeamKerberos_Pod1.0.2/blob/main/.pre-commit-config.yaml)
[![License](https://img.shields.io/github/license/MLH-Fellowship/TeamKerberos_Pod1.0.2)](https://github.com/MLH-Fellowship/TeamKerberos_Pod1.0.2/blob/main/LICENSE)![GitHub pull requests by-label](https://img.shields.io/github/issues-pr/developer-student-club-thapar/officialWebsite/dependencies?label=Dependencies%20Status)

This project is a sign language alphabet recognizer using Python, openCV and tensorflow for training InceptionV3 model, a convolutional neural network model for classification.

The framework used for the CNN implementation can be found here:

[Simple transfer learning with an Inception V3 architecture model](https://github.com/xuetsing/image-classification-tensorflow) by xuetsing



**This is the demo repository of our first hackathon at MLH-Fellowship Fall'2020.**

# Installation and Setup
## Setup and running of project (Backend)

- Fork the repo and clone it.
- The project now uses `pipenv` to manage dependencies.
- Install [Pipenv](https://pypi.org/project/pipenv/) using the following command:
```bash
pip install pipenv
```
- Navigate to the project directory and initialize the environment using the following command -
```bash
pipenv shell --python 3.5
```
- The above step also activates the environment, for activating the environment in subsequent sessions type the following command:
```bash
pipenv shell
```
- At the root of your project directory <br>

```bash
pipenv install
pre-commit install
```

- This will setup the project requirements and pre-commit test hooks!


## Contribution to the project


<div align="center">

[![GitHub issues](https://img.shields.io/github/issues/developer-student-club-thapar/officialWebsite?logo=github)](https://github.com/MLH-Fellowship/TeamKerberos_Pod1.0.2/issues) ![GitHub pull requests](https://img.shields.io/github/issues-pr/MLH-Fellowship/TeamKerberos_Pod1.0.2) ![GitHub contributors](https://img.shields.io/github/contributors/MLH-Fellowship/TeamKerberos_Pod1.0.2)

</div>
We follow a systematic Git Workflow -

- Create a fork of this repo.
- Clone your fork of your repo on your pc.
- [Add Upstream to your clone](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
- **Every change** that you do, it has to be on a branch. Commits on master would directly be closed.
- Make sure that before you create a new branch for new changes,[syncing with upstream](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) is neccesary.

## Commits

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).
- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)
- If you're making very, very small changes to your PR (such as fixing a failed Travis build, or making some minor style corrections or minor changes requested by reviewers), make sure you squeeze your commits afterwards, so you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))
- If you are submitting a PR for a UI-related topic, it would be really awesome if you could add a screenshot of your change or a link to a deployment where it can be tested along with your PR. This makes it very easy for reviewers and you will also get reviews faster.

<div align = "center">

# Contributors
<a href="https://github.com/MLH-Fellowship/TeamKerberos_Pod1.0.2/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=MLH-Fellowship/TeamKerberos_Pod1.0.2" />
</a>
# Maintainers of the project
Amazing members of Team Kerberos!
<table>
  <tr>
        <td align="center"><a href="http://shubhank.codes"><img src="https://avatars3.githubusercontent.com/u/29003047?v=4" width="100px;" alt=""/><br /><sub><b>Shubhank Saxena</b></sub></a><br /><a title="Code">💻</a> <a title="Design">🎨</a> <a  title="Maintenance">🚧</a></td>
                <td align="center"><img src="https://avatars3.githubusercontent.com/u/36269212?s=400&u=a759563a72bf9bb03f1f94c5e9b98a367ff98677&v=4" width="100px;" alt=""/><br /><sub><b>Abhishek Chaurasia</b></sub></a><br /><a title="Code">💻</a> <a title="Design">🎨</a> <a  title="Maintenance">🚧</a></td>
                <td align="center"><img src="https://avatars0.githubusercontent.com/u/33135343?s=400&u=73bed27968847ffbd2c6425c295da2aa4e285ba6&v=4" width="100px;" alt=""/><br /><sub><b>Shreya Gupta</b></sub></a><br /><a title="Code">💻</a> <a title="Design">🎨</a> <a  title="Maintenance">🚧</a></td>
  </tr>
</table>