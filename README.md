SHA-1 Password Cracker
Este projeto implementa um cracker de senha que utiliza o algoritmo de hash SHA-1 para descobrir senhas a partir de uma lista das 10.000 senhas mais usadas. Ele também pode utilizar salts conhecidos para aumentar a eficácia na descoberta de senhas.

Funcionalidades
Crackeamento de Senhas Simples: A função crack_sha1_hash compara o hash fornecido com os hashes das senhas na lista top-10000-passwords.txt.
Crackeamento de Senhas com Salts: Quando o parâmetro use_salts é definido como True, a função combina cada senha com os salts da lista known-salts.txt em ambas as ordens (salt+senha e senha+salt) antes de comparar os hashes.
Testes Automatizados: Inclui testes unitários em test_module.py para verificar a precisão da função com diferentes hashes e configurações de salts.
Estrutura do Projeto
main.py: Ponto de entrada para desenvolvimento e execução dos testes. Inclui uma função de exemplo para testar diferentes hashes e imprimir os resultados.
password_cracker.py: Contém a função principal crack_sha1_hash e funções auxiliares para carregar senhas e salts.
test_module.py: Testes unitários para validar a funcionalidade do cracker de senha.

Exemplo de Uso:

import password_cracker
# Testar sem salts
cracked_password = password_cracker.crack_sha1_hash("fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password)  # Deve retornar a senha correspondente ou "PASSWORD NOT IN DATABASE"

# Testar com salts
cracked_password_with_salt = password_cracker.crack_sha1_hash("dcc466796201f7232b22a03781110a8871fd038c", True)
print(cracked_password_with_salt)  # Deve retornar a senha correspondente ou "PASSWORD NOT IN DATABASE"
