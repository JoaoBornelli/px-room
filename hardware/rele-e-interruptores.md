# Módulo relé e interruptores

> Estado: 🟡 investigando · [← painel do hardware](README.md)

As lâmpadas são convencionais. Um módulo relé central liga e desliga cada circuito de luz. O módulo aceita comandos de duas fontes: entradas digitais e um protocolo de comunicação. Os interruptores de parede são de baixa tensão e enviam um sinal ao módulo. Eles não chaveiam a carga.

> **Atenção:** o hub em avaliação (Intelbras MCA) usa Zigbee. Esta abordagem com fio pode mudar. Veja [hub-automacao.md](hub-automacao.md#conflito-com-as-decisões-atuais).

![Módulo relé e interruptores](diagramas/rele-interruptores.svg)

> **Nota:** cada quarto tem só 1 ponto de luz e 1 interruptor. Um módulo relé central por quarto é provavelmente excessivo. Avaliar: um módulo central para vários quartos, ou um módulo pequeno por quarto.

## Requisitos do módulo relé

| Requisito | Valor | Fonte |
|---|---|---|
| Número de saídas (circuitos de luz) | 1 por quarto, cerca de 20 no total | Descrição do quarto |
| Número de entradas digitais (interruptores) | 1 por quarto, cerca de 20 no total | Descrição do quarto |
| Protocolo de comunicação | a definir | Escolha do hub ([hub-automacao.md](hub-automacao.md)) |
| Corrente por saída | a definir | Carga de cada circuito |
| Montagem | a definir, ex.: trilho DIN no quadro | Instalação elétrica |
| Interruptor funciona sem hub e sem internet | Desejável | Segurança e conforto do motorista |
| Luz acende quando a porta abre | Obrigatório | Fluxo de uso |

## Perguntas

1. Cada entrada digital aciona a saída dela sem depender do hub? Este modo também se chama "standalone".
2. O módulo volta ao último estado depois de uma queda de energia?
3. O interruptor é um pulsador (aperta e solta) ou uma chave (liga e fica)?
4. Quem alimenta os interruptores: a fonte do módulo ou uma fonte separada?

## Candidatos a investigar

Nada aqui está confirmado.

| Candidato | Entradas digitais | Protocolos | Notas |
|---|---|---|---|
| Placas ESP32 com relés (ex.: Kincony KC868) | a confirmar | a confirmar: Wi-Fi, MQTT, ESPHome | Muito usadas com o Home Assistant. |
| Shelly Pro (trilho DIN) | a confirmar | a confirmar: Wi-Fi, LAN, API local | Caro para poucas saídas. |
| Módulo Modbus industrial | a confirmar | Modbus RTU/TCP | Precisa de ponte para o hub. |
| Módulos relé Zigbee da linha Casa Inteligente Intelbras | a confirmar | Zigbee | Integram no hub MCA. Verificar se aceitam interruptor de baixa tensão. |
