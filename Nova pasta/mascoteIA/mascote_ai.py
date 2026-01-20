import subprocess
import platform # Para identificar o sistema operacional

def executar_comando_simples():
    """Função para simular o recebimento e execução de comandos."""
    print("Mascote IA: Olá! Estou pronto para receber seus comandos.")
    print("Mascote IA: Em que posso ajudar, é só pedir que irei tentar te auxiliar.")

    while True:
        comando = input("Você: ").lower().strip() # .lower() para minúsculas, .strip() para remover espaços extras

        if "abrir bloco de notas" in comando:
            print("Mascote IA: Abrindo o Bloco de Notas...")
            try:
                # Comando para abrir o Bloco de Notas (Windows)
                if platform.system() == "Windows":
                    subprocess.Popen(['notepad.exe'])
                # Comando para abrir TextEdit (macOS)
                elif platform.system() == "Darwin": # Darwin é o nome do kernel do macOS
                    subprocess.Popen(['open', '-a', 'TextEdit'])
                # Comando para abrir gedit (Linux - comum em ambientes GNOME)
                elif platform.system() == "Linux":
                    subprocess.Popen(['gedit'])
                else:
                    print("Mascote IA: Sistema operacional não reconhecido para abrir o editor de texto.")

            except FileNotFoundError:
                print("Mascote IA: O programa não foi encontrado. Verifique se está instalado ou se o comando está correto.")
            except Exception as e:
                print(f"Mascote IA: Ocorreu um erro ao tentar abrir o programa: {e}")

        elif "abrir navegador" in comando or "abrir chrome" in comando:
            print("Mascote IA: Abrindo o navegador padrão...")
            try:
                # O módulo webbrowser é mais robusto para abrir URLs ou o navegador padrão
                import webbrowser
                webbrowser.open('https://www.google.com/') # Abre o navegador padrão em google.com
            except Exception as e:
                print(f"Mascote IA: Ocorreu um erro ao tentar abrir o navegador: {e}")
        
        elif "abrir youtube" in comando or "youtube" in comando:
            print("Mascote IA: Abrindo o seu youtube!!")
            try:
                import webbrowser
                webbrowser.open('https://www.youtube.com/')
            except Exception as e:
                print(f"Mascote IA: Ocorreu um erro ao abrir o youtube: {e}")

        elif "sair" in comando or "desligar" in comando or "tchal" in comando:
            print("Mascote IA: Desligando. Até mais!")
            break # Sai do loop

        else:
            print("Mascote IA: Não entendi o comando. Tente novamente.")

# Chama a função para iniciar o assistente
if __name__ == "__main__":
    executar_comando_simples()