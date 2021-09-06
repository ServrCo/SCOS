cd ..
find ../. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
7z a SCOS.7z ./bins/.