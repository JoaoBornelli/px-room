# Hub de automação

> Estado: 🟡 investigando · [← painel do hardware](README.md)

O hub recebe os comandos e os envia aos dispositivos do quarto. A opção em avaliação é o hub Intelbras MCA, controlado pela API de integração da Intelbras.

## Opções descartadas

| Opção | Motivo | Data |
|---|---|---|
| Alexa como hub de voz | a registrar numa ADR | 2026-10 |

## Hub Intelbras MCA: o que o fabricante informa

- Linha Mibo Smart (Casa Inteligente Intelbras). Configuração pelo app Mibo Smart.
- Rede Zigbee, até 32 dispositivos por hub.
- O MCA 1001 está descontinuado. O MCA 1002 é o modelo atual.
- O MCA 1001 tem Wi-Fi e Ethernet (RJ45). A loja descreve o MCA 1002 só com Wi-Fi. Confirmar se o MCA 1002 tem Ethernet.
- Segundo o guia do MCA 1001, os dispositivos Zigbee continuam operacionais sem internet.

Fontes: [MCA 1002](https://backend.intelbras.com/pt-br/hub-de-automacao-inteligente-mca-1002) · [datasheet MCA 1001](https://backend.intelbras.com/sites/default/files/2023-07/datasheet-mca-1001-pt.pdf) · [guia MCA 1001](https://backend.intelbras.com/sites/default/files/2026-02/Guia_MCA_1001_01-26_site.pdf)

## As duas opções

| Critério | Hub Intelbras MCA + API Intelbras | Home Assistant num Raspberry |
|---|---|---|
| Comando de voz em pt-BR | a confirmar: sem a Alexa, falta a fonte de voz | Precisa de integração (voz local ou outra) |
| Controla o módulo relé com fio | a confirmar: aceita só dispositivos Zigbee compatíveis? | Sim, por MQTT, Modbus ou ESPHome |
| Backend PX envia comando ao quarto | a confirmar: depende da API de integração | Sim, por API própria |
| Funciona sem internet | Dispositivos Zigbee: sim, segundo o fabricante. Cenários: a confirmar | Sim, para o controle local |
| Gestão de vários quartos e unidades | a confirmar: uma conta para todos os hubs? | Exige gestão de vários Raspberry |
| Dependência de fabricante | Alta: dispositivos da linha Intelbras | Baixa |
| Custo por quarto | Hub: cerca de R$ 224 (preço de tabela, 2026-10) | a confirmar |

## Perguntas para a Intelbras

1. Como a PX tem acesso à API de integração? Há contrato ou custo?
2. A API é de nuvem ou local?
3. Uma conta controla os hubs de todos os quartos e de todas as unidades?
4. A API envia comandos e lê o estado dos dispositivos? Ela envia eventos, por exemplo por webhook?
5. A API controla fechaduras Intelbras? Se sim, a mesma integração serve para o quarto e para o banheiro.
6. O que acontece com os comandos da API quando a internet cai?
7. Um hub serve um quarto ou um grupo de quartos? O limite é 32 dispositivos por hub.
8. Qual sistema de voz funciona com o MCA sem a Alexa?

## Conflito com as decisões atuais

O MCA usa Zigbee. As decisões atuais usam um módulo relé central com fio e interruptores de baixa tensão. Há duas saídas:

- Manter o módulo relé com fio e encontrar uma ponte para o MCA. A ponte pode não existir.
- Trocar o relé central por módulos Zigbee compatíveis com o MCA, um por circuito.

Um requisito anterior também é afetado: trocar dispositivos na manutenção sem depender de uma marca. Com o MCA, o quarto passa a depender da linha Intelbras.

## Escala: 20 quartos

Cada quarto precisa de, no mínimo, 2 dispositivos no hub: a fechadura e o controle da luz.

| Item | Dispositivos |
|---|---|
| 20 quartos × 2 dispositivos | 40 |
| Banheiro comunitário | a definir |
| Limite por hub MCA | 32 |

Resultado: 1 hub não é suficiente. São necessários, no mínimo, 2 hubs. O alcance do Zigbee entre os quartos também precisa de teste no local.

## Evento "porta aberta"

A luz e o assistente começam quando a porta abre. Há dois caminhos possíveis:

| Caminho | Vantagem | Risco |
|---|---|---|
| Cenário local no hub MCA (fechadura → luz) | Funciona sem internet, segundo o fabricante | O assistente não está no hub. Precisa de outro caminho para ele |
| Fechadura → nuvem Intelbras → Torre → quarto | A Torre sabe quem entrou e quando | Depende da internet e de webhook na API Intelbras (a confirmar) |

## Ligação com o resto do sistema

- O hub envia comandos ao módulo relé → [rele-e-interruptores.md](rele-e-interruptores.md).
- A escolha do hub decide qual protocolo o módulo relé precisa aceitar.
- O banheiro também precisa de controle de acesso → [banheiro.md](banheiro.md).
- O assistente recebe o evento "porta aberta" → [assistente.md](assistente.md).
