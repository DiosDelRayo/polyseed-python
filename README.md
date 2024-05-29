Python Polyseed library meant to be compatible with https://github.com/tevador/polyseed (the original C implementation),
built for [Monero Signer Resurrection](https://github.com/DiosDelRayo/MoneroSigner)

Todo:
 - [ ] **investigate and fix wrong output**
       The isssue is that the original version works on byte level, while I used int, so
       I need to split the this bites on decode and join that two bytes for encode...
       - [x] Words to GFPoly coeff same result
       - [x] coeff the same before GFPoly -> PolyseedData
       - [x] PolyseedData secret is the same (TIP: never make assumptions, check, then check again, and check once more...)
       - [x] key salt is same
       - [ ] key is same
       - [ ] crypt salt is same
       - [ ] encode is same
       - [ ] crypt is same
 - [X] build some compare tools using the original library and `pbkdf2_sha256` implementation
 - [x] add convinience command line function to compare to original implementation
 - [ ] refactor, so everything necessary is directly under the module (__init__.py) and only the necessary
 - [ ] some docs
 - [ ] clean up
