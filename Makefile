VERSION=$(shell grep version setup.py | awk -F'"' '{ print $$2 }')
URL=https://github.com/DiosDelRayo/polyseed-python/archive/refs/tags/v$(VERSION).tar.gz

version:
	@echo "Version: $(VERSION)"

sha256-github: version
	@echo 'URL:     ${URL}'
	@echo -n 'sha256:  '
	@curl -L -s ${URL} | sha256sum | awk '{print $$1}'

clean:
	@echo 'clean py cache files...'
	@find polyseed -name __pycache__ -exec rm -rf \{\} \; >&2

checksums: clean
	@echo 'generate sha256 checksums...'
	@find polyseed -type f -exec sha256sum --tag {} \; > SHA256
	@find tools -type f -exec sha256sum --tag {} \; >> SHA256
	@sha256sum --tag setup.py >> SHA256
	@sha256sum --tag Makefile >> SHA256
	@sha256sum --tag README.md >> SHA256
	@sha256sum --tag LICENSE.txt >> SHA256
	@rm -f SHA256.sig
	@git add SHA256

sign: checksums
	@echo 'Sign the checksums...'
	@tools/sign.sh
	@cat SHA256 >> SHA256.sig
	@git add SHA256.sig

verify:
	@echo 'Verify source files...'
	@signify-openbsd -C -p xmrsigner.pub -x SHA256.sig | grep -v ': OK'
	@echo 'Source is verified!'
