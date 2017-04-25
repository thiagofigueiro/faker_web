test:
	python setup.py test

release:
	rm -rf build dist
	python setup.py sdist bdist_wheel upload
