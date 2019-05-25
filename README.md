O projeto nina_user cadastra e autentica usuários. Possui uma API REST e uma API RPC.

Escrito em Python 2.7, utiliza uma base de dados SQLite3. Devido a problemas de compartilhamento de recursos, seu repositório foi separado em um serviço RPC. Atualmente utiliza a mesma base de dados para produção e execução dos testes automatizados (que limpa a base a cada execução).

Para sua execução é necessário instanciar separadamente os serviços RPC (API e repositório).

python nina_user/repo_service_server.py
python nina_user/user_service_server.py

A API REST é executada através de um servidor WSGI. No desenvolvimento foi utilizado o Gunicorn.

gunicorn --reload 'nina_user.app:get_app()'

Os testes automáticos foram escritos utilizando a biblioteca PyTest.