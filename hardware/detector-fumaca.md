# Detector de fumaça

> Estado: 🟡 investigando · [← painel do hardware](README.md)

Cada quarto precisa de um detector de fumaça. O motorista dorme no quarto, e o alarme precisa acordar o motorista. O banheiro comunitário também tem 1 detector de fumaça, no teto do corredor.

## Requisitos

| Requisito | Obrigatório? | Por quê |
|---|---|---|
| 1 detector de fumaça por quarto | Sim | Segurança do motorista que dorme no quarto. |
| 1 detector de fumaça no banheiro comunitário | Sim | Segurança de quem usa o banheiro. |
| Alarme sonoro no próprio quarto | Sim | O alarme acorda o motorista sem depender de rede. |
| Funciona sem internet e sem a central | Sim | O alarme não pode depender da rede. |
| Alerta de bateria baixa | Sim | A equipe troca a bateria antes de o detector parar. |
| Aviso à central e à equipe da PX | Desejável | A equipe sabe qual quarto disparou. |
| Atende às exigências do Corpo de Bombeiros para o local | a confirmar | Veja a pergunta 1. |

## Perguntas

1. O local é hospedagem para o Corpo de Bombeiros? Se sim, a norma pode exigir um sistema de alarme de incêndio certificado (ABNT NBR 17240), com central própria. Nesse caso, um detector de automação residencial não basta. Confirmar com o projetista de incêndio.
2. O detector é a bateria ou ligado à rede elétrica?
3. O detector se comunica com a central de automação? Se sim, por qual protocolo? → [hub-automacao.md](hub-automacao.md)
4. Quando um quarto dispara, os outros quartos também tocam o alarme?
5. Quem recebe o alerta fora do horário comercial?

## Ligação com o resto do sistema

- Se o detector se comunica com a central, a central avisa a Torre PX → [hub-automacao.md](hub-automacao.md).
- O detector fica no centro do teto do quarto. A [maquete do quarto](README.md#maquete-do-quarto) mostra o detector.
- No banheiro, o detector fica no teto do corredor. A [maquete do banheiro](banheiro.md#maquete) mostra o detector.
