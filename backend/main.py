import sqlite3
import bcrypt
import sys
import json

def login_verify(cpf, password):
    conn = sqlite3.connect("../data/auth.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE cpf = ?", (cpf,))
    result = cursor.fetchone()

    if not result:
        return {"ok": False, "msg": "CPF não encontrado", "cpf": cpf}
    
    password_hash = result[0]

    if bcrypt.checkpw(password.encode(), password_hash.encode()):
        cursor.execute("UPDATE users SET last_login = datetime('now') WHERE cpf = ?", (cpf,))
        conn.commit()
        return {"ok": True, "msg": "Login efetuado"}
    else:
        return {"ok": False, "msg": "Senha incorreta", "pass": password, "passh":password_hash}

for line in sys.stdin:
    try:
        data = json.loads(line)
        if data["type"] == "login":
            resultado = login_verify(data["cpf"], data["senha"])
            sys.stdout.write(json.dumps(resultado) + "\n")
            sys.stdout.flush()

    except Exception as e:
        sys.stdout.write(json.dumps({"ok": False, "msg": str(e)}) + "\n")
        sys.stdout.flush()