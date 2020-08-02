package: setup.py
	@rm -rf dist/
	@python setup.py sdist bdist_wheel

publish: package
	@twine upload dist/*

fmt:
	@black ./pelican_decorate_content/.

.PHONY: format
