# Fechadura

> Estado: 🟡 investigando · [← painel do hardware](README.md)

A fechadura inteligente é obrigatória. O sistema PX pré-reserva o quarto a partir do contrato, e o motorista recebe a senha no app. Ninguém da PX vai ao local para cadastrar a senha.

A fechadura fica fora da rede Zigbee → [ADR 0001](../ADRs/0001-central-zigbee-por-local.md). O critério principal de escolha é a senha offline por algoritmo, e não o protocolo de rede.

![Fluxo da senha, da reserva à porta aberta](diagramas/fluxo-senha.svg)

## Senha offline por algoritmo

A Torre gera a senha, com início e fim, pela API da marca. A fechadura valida a senha por algoritmo, sem rede. Assim, a senha não precisa chegar à fechadura, e o quarto funciona sem internet e sem a central.

A senha offline tem um limite: a revogação. A fechadura só apaga uma senha quando recebe a ordem, por gateway ou por Bluetooth perto da porta. Sem gateway, uma senha emitida vale até o fim do período.

| Opção | Revogação | Custo |
|---|---|---|
| Só senha offline | Não. A Torre emite períodos curtos para reduzir o risco | Menor |
| Senha offline + gateway por grupo de quartos | Sim, pelo gateway. O gateway também envia o registro de acesso e a bateria | Gateway por grupo de quartos |

## Requisitos

| Requisito | Obrigatório? | Por quê |
|---|---|---|
| Criar senha por API, sem o app do fabricante | Sim | A Torre PX cria a senha quando pré-reserva o quarto. |
| Senha com início e fim, validada offline por algoritmo | Sim | A senha vale só durante a reserva e não depende de rede. |
| Revogar senha | a decidir | A troca de motorista pode ser cancelada ou mudar. Veja a tabela acima. |
| Teclado numérico na fechadura | Sim | O motorista digita a senha. |
| Chave mecânica de emergência | Sim | A bateria pode acabar. |
| Alerta de bateria baixa por API | Desejável | A equipe troca a bateria antes de a fechadura parar. Exige gateway. |
| Registro de acesso por API | Desejável | O registro ajuda a resolver reclamações. Exige gateway. |

## Perguntas para cada candidata

1. A API é pública, ou só para parceiros? Qual é o custo mensal?
2. A fechadura valida senha com início e fim offline, por algoritmo?
3. Quantas fechaduras um gateway atende, e a que distância?
4. A fechadura tem homologação e assistência técnica no Brasil?
5. Quanto custam a fechadura e o gateway?

## Candidatas a investigar

Nada aqui está confirmado. Preencha a tabela com a fonte de cada resposta.

| Candidata | Senha offline por algoritmo | Gateway | Notas |
|---|---|---|---|
| Ecossistema TTLock (várias marcas) | sim, segundo a documentação (a confirmar) | Bluetooth → Wi-Fi, por grupo de fechaduras (a confirmar) | Muito usada em hotelaria e aluguel de curta duração. API de nuvem chinesa. |
| Tuya (fechadura Wi-Fi) | "offline password" (a confirmar) | Não precisa. A fechadura Wi-Fi dorme para poupar bateria | Custo da API comercial e dependência da nuvem Tuya. |
| Intelbras | a confirmar | a confirmar | Verificar se existe API aberta. O hub MCA foi descartado → [ADR 0001](../ADRs/0001-central-zigbee-por-local.md). |
| Yale / August | a confirmar | a confirmar | Verificar se a API é só para parceiros. |

## Ligação com o resto do sistema

- A Torre PX pré-reserva o quarto e chama a API da marca. O contrato desta chamada vai para [`../contracts/`](../contracts/) quando a marca for escolhida.
- O quarto não tem sensor de porta. A fechadura fica fora da rede, e a central não recebe o evento de abertura → [hub-automacao.md](hub-automacao.md).
- A fechadura do box de chuveiro ainda não está definida → [banheiro.md](banheiro.md).
