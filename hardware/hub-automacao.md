# Central de automação (Zigbee)

> Estado: 🟢 direção decidida ([ADR 0001](../ADRs/0001-central-zigbee-por-local.md)), produtos a escolher · [← painel do hardware](README.md)

Cada local tem uma central. A central recebe os eventos dos quartos e do banheiro, aplica as regras do local e conversa com a Torre PX. Os dispositivos dos quartos e do banheiro são Zigbee comerciais, ligados em mesh.

## Arquitetura

```
Torre PX (nuvem)
   │ internet
Central do local (mini PC)
   ├─ broker MQTT
   ├─ Zigbee2MQTT ◄── coordenador Zigbee de rede (Ethernet ou PoE)
   │                     └─ mesh Zigbee
   │                          ├─ quarto: relé de parede, detector de fumaça
   │                          └─ banheiro: válvula de cada chuveiro, detector de fumaça
   └─ orquestrador: regras do local (comando da luz, alarme de fumaça, timer do banho)

Fechadura do quarto: fora da rede Zigbee (senha offline por algoritmo) → fechadura.md
Assistente de voz: camada separada por Wi-Fi, fase 2 → assistente.md
```

## Componentes da central

| Componente | Função | Produto |
|---|---|---|
| Mini PC | Executa o broker, o Zigbee2MQTT e o orquestrador | a escolher |
| Broker MQTT | Recebe e distribui os eventos e os comandos, por exemplo `quarto/<n>/porta` | Mosquitto (proposta) |
| Zigbee2MQTT | Traduz a rede Zigbee para MQTT, sem depender de marca de dispositivo | Zigbee2MQTT |
| Coordenador Zigbee de rede | Liga a mesh à central por Ethernet. Fica no meio do prédio, longe do mini PC se preciso | a escolher |
| Orquestrador | Aplica as regras do local e envia os eventos à Torre | desenvolvimento interno |

## Dispositivos Zigbee por quarto

| Dispositivo | Função | Papel na mesh |
|---|---|---|
| Relé de parede com entrada de interruptor | Liga a luz. O interruptor aciona o relé sem a central | Roteador (ligado à rede elétrica) |
| Detector de fumaça | Envia o sinal de alarme à central (protocolo a confirmar) | a confirmar |

O quarto não tem sensor de porta nem emissor infravermelho por enquanto. A luz acende pelo interruptor e pelo comando da central ao relé. O protocolo do detector de fumaça está a confirmar → [detector-fumaca.md](detector-fumaca.md).

## Escala

- Os relés ligados à rede elétrica roteiam as mensagens. Quartos pequenos e próximos formam uma mesh densa.
- Um coordenador tem limite prático de dispositivos. O valor fica a medir no teste piloto. Um local grande usa um coordenador por bloco ou por andar.
- O número de quartos aumentou e ainda não está confirmado.

## Coexistência com o Wi-Fi

O Zigbee e o Wi-Fi usam a faixa de 2,4 GHz. O Wi-Fi transmite com potência muito maior. Para reduzir a interferência:

1. O Wi-Fi dos motoristas fica só em 5 GHz.
2. O canal Zigbee fica fixo, escolhido por varredura de energia no local. Os candidatos são 15, 20 e 25. Evite o 20 perto de micro-ondas.
3. Se existe Wi-Fi em 2,4 GHz, ele usa só os canais 1, 6 e 11, com 20 MHz.
4. O coordenador fica a pelo menos 2 m de um access point.
5. O teste piloto num bloco de quartos mede a perda de mensagens e o LQI com celulares em hotspot e com o Wi-Fi de vizinhos ligado.

Saída com fio, se o teste piloto falhar: relés no quadro elétrico. Por isso, na obra nova, peça ao eletricista um fio de reserva do interruptor até o quadro.

## Quando a central falha

| Função | Sem a central |
|---|---|
| Luz pelo interruptor | Funciona: o relé aciona a luz localmente |
| Fechadura do quarto | Funciona: a senha é validada na fechadura |
| Comando da central que liga a luz | Para |
| Sinal do detector de fumaça à central | Para. O alarme sonoro local continua |
| Timer do chuveiro | Depende de o timer rodar no próprio dispositivo → [banheiro.md](banheiro.md) |
| Eventos para a Torre | Param. A central precisa guardar e reenviar os eventos quando voltar (a definir) |

## Opções descartadas

| Opção | Motivo | Data |
|---|---|---|
| Hub Intelbras MCA | Limite de 32 dispositivos por hub, API sem documentação pública, dependência da linha Intelbras | 2026-10-23 |
| Hub ou computador por quarto | Custo e manutenção altos na escala nova | 2026-10-23 |
| Placa única por quarto (ESP32 com relé e áudio) | Relé, microfone e sensor ficam em lugares diferentes. Um defeito no áudio não pode apagar a luz | 2026-10-23 |
| Alexa como hub de voz | Descartada | 2026-10 |

## Perguntas

1. Qual mini PC e qual coordenador Zigbee?
2. Quantos dispositivos um coordenador aceita com estabilidade? Medir no teste piloto.
3. A central precisa de redundância, por exemplo um segundo mini PC de reserva?
4. Qual contrato liga a central à Torre? O contrato vai para [`../contracts/`](../contracts/).
5. Quem faz o pareamento dos dispositivos na instalação, e com qual procedimento?
