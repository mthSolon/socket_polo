import socket

def iniciar_servidor(port: int) -> None:
    """
    Inicia o servidor no IP local e na porta escolhida pelo usuário. Recebe o arquivo em bytes do cliente, converte
    e salva o arquivo no diretório atual.

    :param port: Número da porta

    :return: None
    """

    host = 'localhost'
    port = port

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Inicializando servidor no Host "{host}" e porta {port}')
    server.bind((host, port))
    server.listen()
    print('Aguardando conexão do cliente.')

    conn_socket, endereco = server.accept()
    print(f'Conectado ao endereço {endereco}')
    nome_arquivo = conn_socket.recv(1024).decode() # Recebe o nome do arquivo
    print(f'Arquivo: {nome_arquivo}')


    with open(nome_arquivo, 'wb') as f:
        while True:
            data = conn_socket.recv(10000000)
            if not data:
                break
            f.write(data)
    print('Recebido!')

if __name__ == '__main__':
    porta = int(input('Digite a porta em que o servidor irá escutar: '))
    iniciar_servidor(porta)