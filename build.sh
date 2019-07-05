#!/bin/bash

set -ex

sphinx-build -W -n -a -b html source/ build/html/
