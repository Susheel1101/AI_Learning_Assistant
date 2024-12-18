#!/bin/bash
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5901:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -e WIDTH=1024 \
    -e HEIGHT=768 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest