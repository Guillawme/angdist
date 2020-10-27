PROJECT = angdist

FILES = \
	LICENSE \
	README.md \
	environment.yml \
	makefile \
	setup.py \
	$(PROJECT).py

.PHONY: all check upload clean create-env update-env

all: build check upload

build: $(FILES)
	python setup.py sdist bdist_wheel

check: build
	twine check dist/*

upload: check
	twine upload dist/*

clean:
	rm -rf $(PROJECT).egg-info build dist __pycache__

create-env:
	conda env create -f environment.yml

update-env:
	conda env export --name dev-$(PROJECT) > environment.yml
