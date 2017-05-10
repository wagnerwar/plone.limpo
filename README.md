# Plone.limpo

			yum install nmap mod_ssl openssl openssl-devel zip unzip zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel libxml2-devel libxslt-devel python-setuptools wget
			Baixar o projeto do git (plone.limpo)
			git clone https://github.com/wagnerwar/plone.limpo.git
			cd plone.limpo
			wget https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py
			python bootstrap.py
			bin/buildout -vvvc buildout.cfg
			bin/instance fg para testar

