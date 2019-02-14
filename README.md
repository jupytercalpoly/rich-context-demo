# rich-context-demo

The goal of this repo is to build a docker image that can launch quickly
and have the datastore, metadata, and commenting all working.

You should also be able to mount your current directory in the image and use it as
a scratch space.

```bash
docker build -t rich-context-demo .
docker run --rm -p 8888:8888 -v "$PWD":/app rich-context-demo
```

To rebuild from source:

```bash
docker rmi rich-context-demo
docker build -t rich-context-demo .
```