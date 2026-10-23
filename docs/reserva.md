# Reserva do quarto

> Estado: 🟡 investigando · [← README](../README.md)

## Por que a reserva existe

A operação usa troca de motoristas em viagens longas. A cada cerca de 12 h de direção, o motorista precisa descansar por, no mínimo, 11 h. Outro motorista assume o caminhão, e o caminhão não fica parado. O motorista que sai fica no quarto PX durante o descanso.

## Pré-reserva automática

O sistema PX pré-reserva o quarto a partir do contrato do motorista.

1. O contrato e a rota indicam onde e quando a troca de motorista acontece.
2. A Torre calcula o horário previsto da troca.
3. A Torre pré-reserva um quarto na unidade da troca. A reserva cobre, no mínimo, 11 h de descanso.
4. A Torre gera, pela API da marca da fechadura, uma senha offline válida só no período da reserva. A marca ainda não está escolhida → [fechadura.md](../hardware/fechadura.md).
5. A Torre envia uma notificação ao app do motorista. O app mostra a localização, o número do quarto e a senha.
6. A Torre registra o direito a um banho grátis.

## Plataforma interna com Keycloak (proposta complementar)

A proposta anterior era uma plataforma interna. Nesta plataforma, um usuário da PX faz a reserva. O Keycloak faz a autenticação e o controle de acesso.

Com a pré-reserva automática, a plataforma muda de função. Ela pode servir para ver, ajustar e cancelar reservas. A função ainda não está definida.

O Keycloak faz o login, o SSO e os papéis dos usuários. O Keycloak não faz a reserva. A disponibilidade, o registro da reserva e o pedido de senha ficam no serviço de reservas da Torre.

## Riscos

| Risco | Efeito | Mitigação possível (a avaliar) |
|---|---|---|
| O caminhão atrasa ou adianta | A senha ainda não vale ou já venceu quando o motorista chega | Margem antes e depois do período; a Torre emite uma senha nova pela posição do caminhão. Revogar a senha antiga exige gateway → [fechadura.md](../hardware/fechadura.md#senha-offline-por-algoritmo) |
| A troca é cancelada ou muda de unidade | O quarto fica reservado sem uso | A Torre cancela a reserva e a senha quando o contrato muda |
| Muitas trocas no mesmo período | Faltam quartos | Calcular a ocupação máxima por unidade antes de definir o número de quartos |
| O descanso termina e o motorista não sai | O próximo motorista não tem quarto | Intervalo de limpeza entre reservas e regra de saída |

## Perguntas

1. Qual dado da Torre dá o horário real de chegada do motorista: contrato, rota ou posição do caminhão?
2. Quanto tempo de margem a senha precisa antes e depois do período da reserva?
3. O descanso de 11 h pode ser dividido em partes? Se sim, a reserva muda de tamanho. Confirmar a regra no contrato e na legislação (Lei 13.103/2015).
4. O assistente acorda o motorista no fim do descanso?
5. O motorista que chega para assumir o caminhão também usa o quarto?
6. Quanto tempo a limpeza precisa entre duas reservas?
7. Com a pré-reserva automática, quem usa a plataforma com Keycloak, e para quê?
8. A PX já usa um provedor de identidade? Se sim, o Keycloak duplica esse provedor?
