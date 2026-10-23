# Relé e interruptor

> Estado: 🟡 investigando · [← painel do hardware](README.md)

Cada quarto tem 1 ponto de luz e 1 interruptor. Um relé Zigbee comercial fica na caixa da parede e liga a luz. O interruptor de parede se liga à entrada do relé. A central de automação envia comandos ao relé pela mesh Zigbee → [hub-automacao.md](hub-automacao.md).

> **Nota:** o diagrama `diagramas/rele-interruptores.svg` mostra a abordagem anterior, com um módulo relé central com fio. O diagrama precisa ser refeito.

## Requisitos do relé

| Requisito | Valor | Por quê |
|---|---|---|
| Protocolo | Zigbee, compatível com Zigbee2MQTT | [ADR 0001](../ADRs/0001-central-zigbee-por-local.md) |
| Saídas | 1 por quarto | 1 ponto de luz |
| Entrada de interruptor | 1, com acionamento local | O interruptor funciona sem a central |
| Tamanho | Cabe na caixa 4×2 atrás do interruptor | Instalação pelo eletricista, sem quadro novo |
| Fio neutro | a confirmar na obra | Relés sem neutro funcionam pior com lâmpada LED |
| Estado depois de queda de energia | Configurável | Evitar a luz acesa à noite depois de uma queda |
| Roteador Zigbee | Sim | Relé ligado à rede elétrica reforça a mesh |
| Luz acende quando a porta abre | Obrigatório | Regra na central, a partir do sensor de porta |

## Perguntas

1. O interruptor é um pulsador (aperta e solta) ou uma chave (liga e fica)? O relé precisa aceitar o tipo escolhido.
2. A caixa da parede tem fio neutro?
3. Qual relé e qual marca? Conferir a compatibilidade na lista de dispositivos do Zigbee2MQTT.

## Saída com fio

Se o teste piloto do Zigbee falhar, os relés vão para o quadro elétrico. Essa saída exige um fio do interruptor até o quadro. Na obra nova, peça ao eletricista esse fio de reserva → [hub-automacao.md](hub-automacao.md#coexistência-com-o-wi-fi).
