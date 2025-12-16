import bcrypt

# A senha que você quer usar para logar
senha_conhecida = "123456"

# Gerando o hash correto
bytes_senha = senha_conhecida.encode('utf-8')
salt = bcrypt.gensalt()
hash_nova = bcrypt.hashpw(bytes_senha, salt)

print("--- Copie os dados abaixo para o seu Banco de Dados ---")
print(f"Senha (para você digitar no login): {senha_conhecida}")
print(f"Hash (para salvar no campo 'senha' da tabela): {hash_nova.decode('utf-8')}")


import bcrypt

# 1. O HASH que você tirou do banco de dados
# Nota: É importante colocar o 'b' na frente para indicar que são bytes, 
# ou usar .encode('utf-8') se vier como string do banco.
hash_do_banco = b"$2b$12$TyD.uqSbIZS2/QRm1mPSO.CxrulEu8/ETco2G9wTZhbI9dt7eWiSK"

# 2. A SENHA que você quer testar (simulando o input do usuário)
senha_digitada = "123456"  # Tente mudar isso para ver o erro

# 3. Fazendo a verificação
# O primeiro argumento é a senha digitada (em bytes)
# O segundo argumento é o hash do banco (em bytes)
if bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_do_banco):
    print("✅ ACESSO PERMITIDO: A senha corresponde ao hash!")
else:
    print("❌ ACESSO NEGADO: A senha está incorreta.")