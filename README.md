# Ana e Heitor

<p align="center">
  <img src="ana-heitor/game/images/bg%20kissing.png" alt="Ana e Heitor" width="760">
</p>

<p align="center">
  <strong>Uma visual novel / dating sim sobre duas pessoas, a Poli, muitos turnos livres e um amor que atravessa fusos.</strong>
</p>

<p align="center">
  <img alt="Ren'Py" src="https://img.shields.io/badge/Ren'Py-8.5-f47ca7?style=for-the-badge">
  <img alt="Idioma" src="https://img.shields.io/badge/Idioma-PT--BR-89c7f5?style=for-the-badge">
  <img alt="Plataformas" src="https://img.shields.io/badge/Windows%20%2B%20Linux-PC-f5c84b?style=for-the-badge">
</p>

## Sobre

**Ana e Heitor** é uma edição expandida de um presente em forma de jogo: uma visual novel feita em Ren'Py, reimaginada com mecânicas de dating sim, dois pontos de vista, mini-games, conquistas e um modo pós-jogo infinito.

A história acompanha o começo do relacionamento, a rotina na Escola Politécnica da USP, o primeiro beijo, namoro, distância, Austrália, França e um final de aniversário feito para continuar a brincadeira.

## O Que Tem

- **Dois pontos de vista**: Ana e Heitor têm HUD, cores, dinheiro e progressão próprios.
- **Dia a dia jogável**: escolha entre Poli, bandejão, presentes, dinheiro e rolês em casa.
- **Progressão de amor**: curiosidade vira atenção, interesse, carinho, paixão e amor.
- **Mini-games**: debug de EP, mosaico de fotos e ritmo estilo DDR.
- **Presentes e encontros**: chocolate, sushi, fotos, lanchinhos e escolhas com custo.
- **Conquistas**: lista completa para quem quer ver tudo.
- **Pós-jogo infinito**: troque POV, configure estados e reviva memórias.
- **Trilha sonora dinâmica**: músicas mudam com rotina, romance, tensão e saudade.

## Um Gostinho

<p align="center">
  <img src="ana-heitor/game/images/bg%20bandejao.png" alt="Bandejão" width="30%">
  <img src="ana-heitor/game/images/bg%20sala%20game.png" alt="Mini-games" width="30%">
  <img src="ana-heitor/game/images/bg%20airport.png" alt="Aeroporto" width="30%">
</p>

## Como Rodar Em Desenvolvimento

1. Instale o [Ren'Py](https://www.renpy.org/).
2. Abra o launcher do Ren'Py.
3. Aponte o launcher para a pasta `ana-heitor`.
4. Clique em **Launch Project**.

O projeto principal do jogo fica em:

```text
ana-heitor/
```

## Como Gerar Build

No launcher do Ren'Py:

1. Abra o projeto `ana-heitor`.
2. Entre em **Build Distributions**.
3. Gere o pacote para PC.
4. Envie o `.zip`: quem receber só precisa extrair e executar o `.exe` no Windows ou o `.sh` no Linux.

## Estrutura

```text
ana-heitor/
  game/
    script.rpy                 # história principal
    story_expansion.rpy        # expansão pós-Austrália / final
    relationship_system.rpy    # dia a dia, amor, dinheiro, mini-games, conquistas
    whatsapp_excerpts.rpy      # trechos estilizados de WhatsApp
    images/                    # personagens, cenários e fotos do mosaico
    ddr/                       # músicas e charts do mini-game de ritmo
    audio/                     # trilha sonora
```

## Observação

Este é um projeto pessoal, feito como presente. O código pode ser estudado, mas a história, fotos, conversas e assets pessoais existem para esse contexto específico.

<p align="center">
  Feito com carinho, bugs corrigidos no amor e um pouco de teimosia de engenharia.
</p>
