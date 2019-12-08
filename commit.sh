#!/bin/bash
set -xe

git diff
git add .
git commit -m "Update contents"
git push origin master

