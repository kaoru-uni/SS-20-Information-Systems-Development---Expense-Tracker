#!/bin/bash
make clean
sphinx-apidoc -o . ..
make html
