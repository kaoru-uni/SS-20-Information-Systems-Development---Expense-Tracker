#!/bin/bash
sphinx-apidoc -o . ..
make clean html
