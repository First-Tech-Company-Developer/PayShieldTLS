# PayShieldTLS
Script para conexão TLS com HSM PayShield com certificado TLS/SSL no LoadBalancer.

Esse script de testes foi desenvolvido em Python, seguindo as recomendações do manual do fabricante do HSM.

# Geração de chaves para conexão

Para abrir a conexão SSL com o LoadBalancer o client precisa de um certificado gerado locamente na aplicação.

Siga o exemplo abaixo para a geração de um par de chaves.

<code>
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -subj "/C=BR/ST=Sao Paulo/L=Sao Paulo/O=ORGANIZAÇÃO_NAME/CN=HOSTNAME"
</code>


Após gerar o par de chaves execute a apliação alterando os valores no aquivo main.py