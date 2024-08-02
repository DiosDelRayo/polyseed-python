VERSION=$(shell grep version setup.py | awk -F'"' '{ print $$2 }')
URL=https://github.com/DiosDelRayo/polyseed-python/archive/refs/tags/v$(VERSION).tar.gz

version:
	@echo "Version      : $(VERSION)"

sha256-github: version
	@echo 'URL         :  ${URL}'
	@echo -n 'sha256(curl):  '
	@curl -L -s ${URL} | sha256sum | awk '{print $$1}'
	@echo -n 'sha256(wget):  '
	@wget -O - -q ${URL} | sha256sum | awk '{print $$1}'
