# ADR 0001: central Zigbee por local

- Estado: aceita
- Data: 2026-10-23

## Contexto

O número de quartos aumentou muito em relação à escala inicial de cerca de 20 quartos. O valor novo ainda não está confirmado. Um hub ou um computador por quarto fica caro e difícil de manter nessa escala. A instalação também precisa ser simples para um eletricista comum.

## Decisão

1. Cada local (unidade) tem uma central: um mini PC com broker MQTT, Zigbee2MQTT e o orquestrador do local.
2. A parte elétrica do quarto e do banheiro usa dispositivos Zigbee comerciais. Exemplos: relé de parede, sensor de porta, emissor infravermelho e válvula do chuveiro.
3. Os dispositivos Zigbee formam uma rede mesh. Os relés ligados à rede elétrica funcionam como roteadores.
4. Um coordenador Zigbee de rede (Ethernet ou PoE) liga a mesh à central. Um local grande pode ter mais de um coordenador.
5. A fechadura do quarto fica fora da rede Zigbee. A fechadura aceita senha com início e fim, gerada offline por algoritmo.
6. O assistente de voz é uma camada separada e fica para a fase 2.

## Consequências

- O quarto continua a funcionar sem a central. O interruptor aciona o relé localmente, e a fechadura aceita a senha.
- Sem a central, param só a automação (por exemplo, a luz que acende quando a porta abre) e o envio de eventos à Torre.
- O Zigbee e o Wi-Fi usam a faixa de 2,4 GHz. O projeto precisa de canais fixos, de Wi-Fi para os motoristas só em 5 GHz e de um teste piloto antes da compra em escala.
- A central é um ponto único de falha da automação do local. A redundância fica a avaliar.

## Opções descartadas

| Opção | Motivo |
|---|---|
| Hub Intelbras MCA | Limite de 32 dispositivos por hub. A API de integração não tem documentação pública. O quarto passa a depender da linha Intelbras. |
| Hub ou computador por quarto | Custo e manutenção por quarto altos na escala nova. |
| Placa única por quarto (ESP32 com relé e áudio) | O relé, o microfone e o sensor de porta ficam em lugares diferentes. O relé exige eletricista. Um defeito no áudio não pode apagar a luz. |
| Alexa | Descartada em 2026-10. |
