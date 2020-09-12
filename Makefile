init:
	pip install -r requirements.txt

test:
	nosetests --pdb -v tests


install:
	pip install .