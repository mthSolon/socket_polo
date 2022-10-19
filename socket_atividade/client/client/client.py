import socket
from typing import BinaryIO, Tuple

def conectar_cliente(port: int, hostname: str) -> None:
    """
    Conecta o cliente no servidor com o IP local e porta escolhida pelo usuário e envia o arquivo em bytes.

    :param port: Número da porta

    :return: None
    """

    host = hostname
    port = port

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f'Cliente conectado no Host {host} e porta {port}')

    nome_arquivo, arquivo = ler_dados()
    client.send(nome_arquivo.encode()) # Envia o nome do arquivo
    try:
        for data in arquivo.readlines():
            client.send(data)
    except IOError:
        pass
    arquivo.close()
    print(f'{nome_arquivo} enviado')

def ler_dados() -> Tuple[str, BinaryIO]:
    """
    Lê o arquivo no destino informado pelo o usuário e o nome que o usuário deseja ao enviar o arquivo.

    :returns: (nome_arquivo(str), file(BinaryIO)): Retorna nome do arquivo que será enviado ao servidor e o arquivo
    lido em bytes.
    """
    caminho = input('Digite o caminho do arquivo para ser enviado: ')
    try:
        file = open(caminho , 'rb')
        nome = input('Digite o nome do arquivo com extensão: ')
        return nome, file
    except FileNotFoundError:
        print(f'Arquivo não encontrado no caminho: {caminho}')
        ler_dados()

def main():
    porta = int(input('Digite a porta que deseja se conectar: '))
    hostname = input('Digite o host que deseja se conectar: ')
    try:
        conectar_cliente(porta, hostname)
    except ConnectionRefusedError:
        print('Conexão recusada.')