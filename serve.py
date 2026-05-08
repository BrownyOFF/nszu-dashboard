import http.server
import socketserver
import webbrowser
import socket
import sys
import os
import time

def find_free_port(start_port):
    port = start_port
    while port < start_port + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            res = sock.connect_ex(('localhost', port))
            if res != 0: # Port is free
                return port
        port += 1
    return None

def main():
    start_port = 8000
    port = find_free_port(start_port)
    
    if not port:
        print("Помилка: Не вдалося знайти вільний порт у діапазоні 8000-8100.")
        sys.exit(1)

    handler = http.server.SimpleHTTPRequestHandler
    
    # Вимикаємо кешування для розробки
    handler.extensions_map.update({
        '.html': 'text/html',
    })

    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            url = f"http://localhost:{port}/main.html"
            print(f"Сервер запущено: {url}")
            print("Натисніть Ctrl+C для зупинки.")
            
            # Відкриваємо браузер через секунду
            if os.fork() == 0:
                time.sleep(1)
                webbrowser.open(url)
                sys.exit(0)
                
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер зупинено.")
        sys.exit(0)
    except Exception as e:
        print(f"Помилка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
