# rich-context-demo

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupytercalpoly/rich-context-demo/master?urlpath=lab/tree/src/Notebook.ipynb)

The goal of this repo is to build a docker image that can launch quickly
and have the [databus](https://github.com/jupyterlab/jupyterlab/pull/5857), [metadata](https://github.com/jupyterlab/jupyterlab-metadata-service), and [commenting](https://github.com/jupyterlab/jupyterlab-commenting) all working.

This uses [`repo2docker`](https://repo2docker.readthedocs.io/en/latest/usage.html) to create a Dockerfile, build it, and start it up:

```bash
python3 -m pip install jupyter-repo2docker
# Mount only `src` directory so we don't clobber `build` directory with built files.
jupyter-repo2docker -v "$PWD/src:/home/$USER/src" .
```

Now you can edit any files in the `src` directory in JupyterLab and those edits will be reflected in your host directory.


## FAQ

Q: Why use repo2docker instead of a Dockerfile?
A: We want it to be able to run on Binder so we need to make sure it works with their workflow. It's better to have one tool to
   run local and hosted usage so that we only need to make things work once.

Q: Shouldn't we check in the dependencies into this repo with submodules or subtree?
A: Possibly... It is simpler just to clone in the `binder/postBuild`, but if we included it in the repo then it wouldn't have to
   be re-cloned on every build (better caching).
