# Assistente de voz

> Estado: 🟡 investigando · [← painel do hardware](README.md)

O assistente fala com o motorista dentro do quarto. O desenvolvimento é interno, provavelmente.

## O que o assistente faz

1. Alguns segundos depois da entrada do motorista, o assistente dá as boas-vindas.
2. O assistente explica o funcionamento do quarto.
3. O assistente informa o banho, o contrato e as regras.

## Perguntas

1. Qual hardware fica em cada quarto: só alto-falante e microfone, com o processamento no mini PC central, ou um computador pequeno por quarto? Um computador por quarto fica caro para 20 quartos → [hub-automacao.md](hub-automacao.md#processamento-central-hipótese).
2. O assistente só fala, ou também recebe comandos de voz? Se recebe, precisa de palavra de ativação (wake word) em pt-BR.
3. O processamento da voz é local ou na nuvem?
4. Qual evento inicia as boas-vindas: o evento "porta aberta" da fechadura ou um sensor de presença?
5. Quais informações vêm da Torre: nome do motorista, contrato, direito ao banho?
6. O motorista pode desligar o assistente para dormir?
7. Qual é o custo por quarto, para 20 quartos?

## Ligação com o resto do sistema

- O evento "porta aberta" chega pelo hub ou pela Torre → [hub-automacao.md](hub-automacao.md).
- As informações do banho vêm do controle do banheiro → [banheiro.md](banheiro.md).
