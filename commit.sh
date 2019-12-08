#!/bin/bash
set -ex

git diff
git add .
git commit -m "Update contents"
git push origin master

