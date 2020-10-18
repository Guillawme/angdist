FILES = \
	LICENSE \
	README.md \
	environment.yml \
	makefile \
	setup.py \
	angdist.py

.PHONY: all clean check upload

all: build check upload

build: $(FILES)
	python setup.py sdist bdist_wheel

check: build
	twine check dist/*

upload: check
	twine upload dist/*

clean:
	rm -rf angdist.egg-info build dist __pycache__
