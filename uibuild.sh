#!/bin/bash

for f in UI/*.ui; do
	pyn=$(echo $f | sed 's/.ui/.py/' | sed 's/UI/GUI/')
	echo "Building $f to $pyn"
	python -m PyQt5.uic.pyuic $f -o $pyn
done

pyrcc5 Assets/icons.qrc -o icons_rc.py