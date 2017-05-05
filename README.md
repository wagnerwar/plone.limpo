# Plone.limpo

			yum groupinstall 'Development Tools'
	
			yum install nmap mod_ssl openssl openssl-devel zip unzip zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel libxml2-devel libxslt-devel python-setuptools wget
			
			baixar e compilar  versão específica de PYTHON (2.7.13)
			wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
			tar -vzxf Python-2.7.13.tgz
			cd Python-2.7.13
			./configure --prefix=DESTINO_INSTALACAO_PYTHON_2.7.13
			make
			make install
			
			cd DIRETORIO_PROJETOS

			easy_install virtualenv

			virtualenv --python=CAMINHO_EXECUTAVEL_PYTHON_2.7.13 MEU_AMBIENTE NOME_AMBIENTE

			source NOME_AMBIENTE/bin/activate

			mkdir projetos

			cd projetos

			Baixar o projeto do git (plone.limpo)
			git clone https://github.com/wagnerwar/plone.limpo.git
			cd plone.limpo
			wget https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py
			python bootstrap.py
			bin/buildout -vvvc buildout.cfg
			bin/instance fg para testar

