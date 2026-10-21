# Quarto PX

Quarto inteligente de descanso para motoristas PX.

A transportadora reserva o quarto. O motorista recebe no app a senha da fechadura e as informações do quarto. No quarto, ele controla a luz e o ar-condicionado pelo interruptor ou pela voz.

![Visão geral do hardware do quarto PX](hardware/diagramas/visao-geral.svg)

## Fase atual: escolha do hardware

O hardware define o resto do projeto. A investigação está no painel [`hardware/`](hardware/README.md).

| Peça | Situação |
|---|---|
| Hub de automação | Alexa é o caminho preferido. Home Assistant num Raspberry é a alternativa. |
| Fechadura | Obrigatória. A senha é criada remotamente e chega ao app do motorista. |
| Luz | Lâmpadas convencionais, com um módulo relé central e interruptores de baixa tensão. |
| Ar-condicionado | Modelo inteligente, controlado pelo hub. |
| Planta baixa | Aguardando. Ela define o número de circuitos e de interruptores. |

## Estrutura do repo

| Pasta | Conteúdo |
|---|---|
| [`hardware/`](hardware/README.md) | Painel vivo do hardware, um documento por subsistema e os diagramas |
| [`ADRs/`](ADRs/) | Decisões de arquitetura fechadas (vazia por enquanto) |
| [`contracts/`](contracts/) | Contratos entre sistemas, por exemplo backend PX ↔ API da fechadura (vazia por enquanto) |
| [`docs/`](docs/) | Documentação geral do projeto (vazia por enquanto) |

## Como contribuir com a documentação

- A decisão fechada vira uma ADR em `ADRs/`, e o estado do subsistema muda para 🟢 no painel.
- Os diagramas saem de `hardware/diagramas/gerar.py`. Veja [`hardware/diagramas/README.md`](hardware/diagramas/README.md).
