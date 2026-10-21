# Hub de automação

> Estado: 🟡 investigando · [← painel do hardware](README.md)

O hub recebe a voz do motorista e envia os comandos ao módulo relé e ao ar-condicionado. O caminho preferido é a Alexa. A investigação mede quanto controle e quanta integração a Alexa permite.

## As duas opções

| Critério | Alexa | Home Assistant num Raspberry |
|---|---|---|
| Comando de voz em pt-BR | Nativo | Precisa de integração (Alexa, Google ou voz local) |
| Controla o módulo relé | a confirmar: precisa de skill, Matter ou ponte | Sim, por MQTT, Modbus ou ESPHome |
| Controla o ar-condicionado | a confirmar: depende da marca do ar | a confirmar: depende da marca do ar |
| Backend PX envia comando ao quarto | a confirmar | Sim, por API própria |
| Funciona sem internet | a confirmar | Sim, para o controle local |
| Manutenção em vários quartos | a confirmar | Exige gestão de vários Raspberry |
| Custo por quarto | a confirmar | a confirmar |

Uma terceira opção também existe: o Home Assistant controla tudo, e a Alexa serve só para a voz.

## Perguntas para a Alexa

1. Como a Alexa controla um módulo relé genérico? A resposta pode ser uma skill do fabricante, o Matter ou uma ponte.
2. O backend PX consegue enviar um comando ao quarto sem a voz do motorista, por exemplo "desligar tudo no check-out"?
3. A Amazon tem um programa para hotelaria (Alexa Smart Properties) disponível no Brasil? O que ele permite?
4. Como fica a conta Amazon de cada quarto? O motorista não pode ver o histórico do motorista anterior.
5. O que a Alexa faz quando a internet cai?

## Ar-condicionado

O ar-condicionado é um modelo inteligente e não passa pelo relé. Ele precisa integrar no hub escolhido.

- Opção 1: um ar com Wi-Fi e integração nativa com o hub.
- Opção 2: um ar comum e um emissor infravermelho controlado pelo hub.

## Ligação com o resto do sistema

- O hub envia comandos ao módulo relé → [rele-e-interruptores.md](rele-e-interruptores.md).
- A escolha do hub decide qual protocolo o módulo relé precisa aceitar.
