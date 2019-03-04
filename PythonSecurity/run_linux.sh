#!/bin/sh

var=$PWD
if [ $# -eq 1 ]; then
  var=$1
fi

docker run -v $var:/home/pysec101 -u pysec101 -it --rm --net=host --privileged --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" pysec101:latest /bin/bash
