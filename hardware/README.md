# Hardware do quarto PX

> **Documento vivo.** Fase: investigação de hardware. Última atualização: 2026-10-22.
> Este arquivo é o painel. O detalhe de cada parte fica no documento do subsistema.

## O que o sistema faz

1. O sistema PX calcula o horário da troca de motorista a partir do contrato. O sistema PX pré-reserva o quarto com data e horário. O contexto está no [README principal](../README.md#contexto-da-operação).
2. A Torre pede à API Intelbras uma senha para a fechadura, válida só na data e no horário da reserva.
3. O motorista recebe uma notificação. O app mostra a localização, o número do quarto e a senha.
4. O motorista entra no quarto com a senha. A luz acende automaticamente.
5. Alguns segundos depois, o assistente de voz dá as boas-vindas e informa o banho, o contrato e as regras.
6. O motorista usa o banheiro comunitário, fora do quarto. O primeiro banho é grátis. Para outro banho, o motorista paga. O fluxo do banho ainda não está definido.

O fluxo completo está no [README principal](../README.md#fluxo-de-uso-proposta).

> **Atenção:** os diagramas SVG ainda mostram a Alexa, o ar-condicionado e o banheiro dentro do quarto. Atualize `diagramas/gerar.py`.

![Visão geral do hardware do quarto PX](diagramas/visao-geral.svg)

## O quarto

| Item | Quantidade por quarto |
|---|---|
| Cama | 1 |
| Cômoda ou escrivaninha pequena | 1 |
| Ponto de luz | 1 |
| Interruptor | 1 |
| Tomada | 1 |

Escala inicial: cerca de 20 quartos.

## Subsistemas

| Subsistema | O que precisa | Estado | Documento |
|---|---|---|---|
| Fechadura do quarto | Senha com início e fim, criada pela Torre via API Intelbras | 🟡 investigando | [fechadura.md](fechadura.md) |
| Hub de automação | Hub Intelbras MCA + API de integração Intelbras (em avaliação) | 🟡 investigando | [hub-automacao.md](hub-automacao.md) |
| Luz + interruptor | 1 ponto de luz e 1 interruptor; acende quando a porta abre | 🟡 investigando | [rele-e-interruptores.md](rele-e-interruptores.md) |
| Assistente de voz | Alto-falante e microfone; boas-vindas e informações | 🟡 investigando | [assistente.md](assistente.md) |
| Banheiro comunitário | Controle de acesso, banho grátis e banho pago | ⚪ fluxo a definir | [banheiro.md](banheiro.md) |
| Planta baixa | Posição dos quartos, do quadro e do banheiro | ⚪ aguardando | [planta](#planta-ilustrativa) |

Legenda: 🟢 decidido · 🟡 investigando · ⚪ aguardando entrada externa

## Decisões de abordagem

Estas decisões orientam a investigação. Cada uma vira ADR em [`../ADRs/`](../ADRs/) quando for confirmada.

- **Dispositivos convencionais + controle central.** O quarto usa uma lâmpada comum. A inteligência fica no hub e no controle da luz, e não na lâmpada.
- **Fechadura inteligente é obrigatória.** A senha é criada remotamente, sem ninguém no local.
- **Quarto só com dormitório.** O banheiro é comunitário e fica fora do quarto.
- **Alexa descartada.** A Alexa não é mais uma opção de hub para comandos de voz.

> **Conflito a resolver:** o hub MCA usa Zigbee. A abordagem anterior usa um módulo relé com fio. Veja [hub-automacao.md](hub-automacao.md#conflito-com-as-decisões-atuais).

## Perguntas abertas

As perguntas que mais mudam o projeto aparecem primeiro.

1. A API de integração Intelbras permite à Torre criar senhas com início e fim? → [fechadura.md](fechadura.md)
2. Quantos hubs MCA são necessários para 20 quartos e o banheiro? O limite é 32 dispositivos por hub. → [hub-automacao.md](hub-automacao.md#escala-20-quartos)
3. Qual caminho leva o evento "porta aberta" até a luz e o assistente: cenário local no hub ou a Torre? → [hub-automacao.md](hub-automacao.md)
4. Qual hardware executa o assistente de voz em cada quarto? → [assistente.md](assistente.md)
5. Como o controle de acesso do banheiro conta os banhos? → [banheiro.md](banheiro.md)
6. Como a senha funciona quando o motorista chega antes ou depois do horário previsto? → [../docs/reserva.md](../docs/reserva.md)
7. O interruptor continua funcionando sem internet e sem hub? → [rele-e-interruptores.md](rele-e-interruptores.md)
8. Qual internet o quarto tem, e o que acontece quando ela cai?

## Planta ilustrativa

Esta figura é só um exemplo e está desatualizada. A planta baixa real substitui esta figura quando chegar.

![Planta ilustrativa do quarto PX](diagramas/planta-quarto.svg)

## Como manter este documento

- Este README só resume. O conteúdo novo vai para o documento do subsistema.
- Quando o estado de um subsistema mudar, atualize a linha da tabela e a data no topo.
- Quando uma decisão for fechada, escreva a ADR e troque o estado para 🟢.
- Um subsistema novo, por exemplo cortina ou sensor de presença, ganha um arquivo `.md` e uma linha na tabela.
- Para mudar um diagrama, siga [diagramas/README.md](diagramas/README.md).
