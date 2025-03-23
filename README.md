Iscte Sintra - O Simulador

Descrição do Jogo
**Iscte Sintra - O Simulador** é um jogo de exploração e desafios para dois jogadores que se conhecem. Os jogadores podem navegar por diferentes salas do campus Iscte-Sintra e completar pequenos desafios para progredir ou ganhar freebies exclusivos. O jogo recria o ambiente do Iscte-Sintra e incentiva a interação e colaboração entre os jogadores.

Como Jogar
O jogo é projetado para dois jogadores que exploram o campus e interagem com NPCs, objetos e desafios para progredir. As principais mecânicas incluem:

- **Exploração**: Os jogadores podem percorrer diferentes salas do Iscte-Sintra.
- **Interação**: Conversas com NPCs, ativação de portas e outros elementos interativos.
- **Minigames**: Pequenos desafios dentro das salas, necessários para avançar ou desbloquear recompensas.

Salas Disponíveis
1. Entrada - Ponto de partida onde os jogadores iniciam a sua jornada.
2. Multiusos - Uma sala ampla com mesas e desafios interativos.
3. UATA - Espaço onde ocorre um minigame.
4. Laboratório (Lab) - Ambiente de sala de aula e minigame
5. Sala de Aula - Ambiente de sala de aula e minigame

Cada sala pode conter NPCs que fornecem informações e desafios a serem resolvidos.

Minigames
Durante a exploração, os jogadores encontrarão minigames, que podem incluir:
- Resolver quebra-cabeças para abrir portas.
- Desafios de memória.
- Provas de conhecimento sobre Unidades Curriculares do Iscte-Sintra

## Controles
Os jogadores utilizam o teclado para navegar e interagir com o ambiente:
- Setas direcionais (ou WASD): O jogador 1 é movido com WASD e o jogador 2 é movido com as setas direcionais
- Tecla E (Jogador 1) ou Shift direito (Jogador 2): Interagir com NPCs e elementos interativos.
- Mouse: Selecionar opções nos menus e minigames.

Instalação e Execução
Requisitos
- Python 3.x instalado
- Biblioteca Pygame instalada (`pip install pygame`)

Como Executar
1. Clone ou baixe o repositório do jogo.
2. Acesse a pasta do jogo no terminal/cmd.
3. Execute o seguinte comando:
   ```sh
   python main.py
   ```

O jogo iniciará na tela do menu principal, permitindo que os jogadores escolham seu caminho pelo Iscte-Sintra.

Estrutura do Código
O jogo é estruturado da seguinte forma:
```
/game
│-- main.py                  # Arquivo principal do jogo
│-- entrada.py               # Mapa e interações na Entrada
│-- multiusos.py             # Sala Multiusos e seus desafios
│-- uata.py                  # Sala UATA
│-- salaLab.py               # Laboratório
│-- main_menu.py             # Menu principal
│-- structures/              # Estruturas de interação e estáticas
│-- minigames/               # Pasta com os minigames
│-- characters/
│   │-- players/             # Jogadores
│   │-- npcs/                # NPCs
│-- assets/
                  # Recursos do jogo (imagens, sons, etc.)
```

Desenvolvedores
Este jogo foi desenvolvido para um hackathon do Iscte-Sintra.

Divirta-se explorando o Iscte Sintra - O Simulador! 🎮

