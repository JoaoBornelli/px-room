# Hardware do quarto PX

> **Documento vivo.** Fase: investigação de hardware. Última atualização: 2026-10-21.
> Este arquivo é o painel. O detalhe de cada parte fica no documento do subsistema.

## O que o quarto faz

1. A transportadora reserva o quarto para um motorista.
2. O motorista recebe no app a senha da fechadura e as informações do quarto.
3. O motorista entra com a senha. Ele controla a luz e o ar-condicionado pelo interruptor ou pela voz.

![Visão geral do hardware do quarto PX](diagramas/visao-geral.svg)

## Subsistemas

| Subsistema | O que precisa | Estado | Documento |
|---|---|---|---|
| Fechadura | Senha criada remotamente e entregue no app | 🟡 investigando | [fechadura.md](fechadura.md) |
| Hub de automação | Alexa (caminho preferido) ou Home Assistant num Raspberry | 🟡 investigando | [hub-automacao.md](hub-automacao.md) |
| Módulo relé + interruptores | Entradas digitais + protocolo; interruptores de baixa tensão | 🟡 investigando | [rele-e-interruptores.md](rele-e-interruptores.md) |
| Iluminação | Lâmpadas convencionais, chaveadas pelo relé | 🟢 abordagem definida | [rele-e-interruptores.md](rele-e-interruptores.md) |
| Ar-condicionado | Modelo inteligente que integra no hub | 🟡 investigando | [hub-automacao.md](hub-automacao.md#ar-condicionado) |
| Planta baixa | Pontos de luz, circuitos e posição dos interruptores | ⚪ aguardando | [planta](#planta-ilustrativa) |

Legenda: 🟢 decidido · 🟡 investigando · ⚪ aguardando entrada externa

## Decisões de abordagem

Estas decisões orientam a investigação. Cada uma vira ADR em [`../ADRs/`](../ADRs/) quando for confirmada.

- **Dispositivos convencionais + controle central.** O quarto usa lâmpadas comuns e um ar-condicionado inteligente. A inteligência fica no módulo relé e no hub, e não em cada lâmpada.
- **Fechadura inteligente é obrigatória.** A senha é criada remotamente, sem ninguém no local.
- **Interruptor de baixa tensão.** O interruptor envia um sinal ao módulo relé. Ele não chaveia a carga.

## Perguntas abertas

As perguntas que mais mudam o projeto aparecem primeiro.

1. A Alexa controla o módulo relé? Por qual integração? → [hub-automacao.md](hub-automacao.md)
2. O backend PX consegue enviar comando ao quarto, por exemplo "desligar tudo no check-out"? → [hub-automacao.md](hub-automacao.md)
3. A fechadura tem API de nuvem para criar senha com início e fim? → [fechadura.md](fechadura.md)
4. O interruptor continua funcionando sem internet e sem hub? → [rele-e-interruptores.md](rele-e-interruptores.md)
5. Qual internet o quarto tem, e o que acontece quando ela cai?
6. Quantos circuitos e pontos existem? A resposta depende da planta baixa.

## Planta ilustrativa

Esta figura é só um exemplo. A planta baixa real substitui esta figura quando chegar.

![Planta ilustrativa do quarto PX](diagramas/planta-quarto.svg)

## Como manter este documento

- Este README só resume. O conteúdo novo vai para o documento do subsistema.
- Quando o estado de um subsistema mudar, atualize a linha da tabela e a data no topo.
- Quando uma decisão for fechada, escreva a ADR e troque o estado para 🟢.
- Um subsistema novo, por exemplo cortina ou sensor de presença, ganha um arquivo `.md` e uma linha na tabela.
- Para mudar um diagrama, siga [diagramas/README.md](diagramas/README.md).
