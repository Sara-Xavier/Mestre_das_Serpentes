# Mestre das Serpentes

"Mestre das Serpentes" é um jogo clássico da cobra onde o jogador controla uma cobra que cresce ao comer comida. O objetivo é evitar colisões com as bordas da tela e com o próprio corpo da cobra para obter a maior pontuação possível.

## Requisitos

- Python 3.11 ou superior
- Pygame (biblioteca para desenvolvimento de jogos)

## Instalação

1. **Clone o repositório**:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd Mestre_das_Serpentes
    ```

2. **Instale as dependências**:
    ```sh
    pip install pygame
    ```

## Execução do Jogo

Para iniciar o jogo, execute o script `Mestre_das_Serpentes.py`:

    ```sh
    python Mestre_das_Serpentes.py
    ```

## Controles

- **Seta para a Esquerda**: Move a cobra para a esquerda.
- **Seta para a Direita**: Move a cobra para a direita.
- **Seta para Cima**: Move a cobra para cima.
- **Seta para Baixo**: Move a cobra para baixo.
- **Enter**: Inicia o jogo a partir do menu.
- **C**: Continua o jogo após uma tela de fim de jogo.
- **Q**: Sai do jogo após uma tela de fim de jogo.

## Funcionalidades

- **Tela de Menu**: Mostra o título do jogo e a melhor pontuação. O jogo inicia ao pressionar a tecla Enter.
- **Jogo**: A cobra se move em resposta às setas direcionais. Ao comer a comida, a cobra cresce e o score aumenta.
- **Tela de Fim de Jogo**: Exibe uma mensagem de fim de jogo e opções para continuar ou sair.

## Código

O código está estruturado da seguinte forma:

- **Importações**: Importa as bibliotecas `pygame` e `random`.
- **Configurações**: Define cores, configurações da tela, fontes e a melhor pontuação.
- **Funções**:
  - `exibir_menu()`: Exibe a tela de menu do jogo.
  - `jogo()`: Função principal que gerencia a lógica do jogo, movimentação da cobra, detecção de colisões e renderização.

## Exemplos de Uso

Para alterar a imagem da comida, substitua o caminho do arquivo na linha onde o sprite da comida é carregado:

    ```python
    sprite_comida = pygame.image.load('C:/caminho/para/seu/sprite.png')
    ```

Certifique-se de que o arquivo da imagem está no formato correto e que o caminho está correto.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Abra um *issue* ou envie um *pull request*.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato com [Seu Nome](mailto:seu.email@example.com).
