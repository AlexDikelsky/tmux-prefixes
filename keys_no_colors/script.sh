#!/bin/bash

"./keyboard_generator.py" > "test.tex"
pdflatex "test.tex"
zathura "test.pdf"
