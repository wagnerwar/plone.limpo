# plone.limpo

			yum groupinstall 'Development Tools'
			yum install bzip2 bzip2-devel openssl openssl-devel libxml2-devel libxslt-devel python-setuptools
			
			Baixar o projeto do git (plone.limpo)
			wget https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py
			python bootstrap.py
			bin/buildout -vvvc buildout.cfg
			
			para testar:
			bin/instance fg
