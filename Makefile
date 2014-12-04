default: buildout test

buildout: bin/buildout
	@bin/buildout

test:
	@bin/test --with-coverage --cover-package=cosent.buildtools --cover-erase

bin/buildout: bin/python
	@wget http://downloads.buildout.org/2/bootstrap.py
	@bin/python bootstrap.py
	@rm bootstrap.*

bin/python:
	@virtualenv --clear -p python .

travis:
	wget http://downloads.buildout.org/2/bootstrap.py
	python bootstrap.py
	rm bootstrap.*
	bin/buildout

clean:
	rm -rf bin/* .installed.cfg bootstrap.*
