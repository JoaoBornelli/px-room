# Banheiro comunitário

> Estado: 🟡 investigando · [← painel do hardware](README.md)

O quarto tem só o dormitório. O banheiro fica fora do quarto e é comunitário. O controle de acesso fica em cada box de chuveiro, e não na entrada do banheiro.

## A sala

A sala mede cerca de 6 m × 2,4 m. Sete boxes de 1,2 m × 0,85 m ficam em fileira ao longo de uma parede de 6 m. Os 1,2 m restantes formam o corredor.

| Item | Quantidade | Observação |
|---|---|---|
| Box de chuveiro | 4 | Fechadura na porta e válvula solenoide Zigbee com timer |
| Box de vaso | 3 | Sem fechadura controlada |
| Entrada | 1 | Porta numa parede de 2,4 m, sem controle de acesso |
| Detector de fumaça | 1 | No teto do corredor → [detector-fumaca.md](detector-fumaca.md) |

## Maquete

A maquete mostra os 4 boxes de chuveiro de um lado, os 3 boxes de vaso do outro, o corredor com a entrada e o detector de fumaça no teto. As medidas são aproximadas.

![Maquete do banheiro comunitário](diagramas/planta-banheiro.svg)

## Regras de negócio

| Regra | Valor | Estado |
|---|---|---|
| Banho grátis | 1 | Definido. Confirmar: 1 por reserva ou 1 por dia? |
| Banho extra | Pago pelo motorista | Definido. Preço e meio de pagamento: a definir |
| Controle de acesso | Em cada box de chuveiro | Definido. A entrada do banheiro fica livre |
| Tempo do banho | Timer da válvula solenoide | Definido. Duração: a definir |

## Fechadura do box de chuveiro

Cada box de chuveiro tem uma fechadura na porta. A fechadura libera a entrada do motorista no box. Os boxes de vaso não têm fechadura controlada.

O tipo de fechadura do box está a definir: marca, modelo e forma de abrir. Veja a pergunta 1.

## Controle do chuveiro

Cada chuveiro tem uma válvula solenoide. A válvula libera ou bloqueia a água. A automação não chaveia a energia do chuveiro.

- A válvula é controlada por Zigbee.
- A válvula é normalmente fechada (NF): sem energia, a válvula fecha a água.
- Um timer libera a água só durante o tempo do banho. O timer deve rodar no próprio dispositivo. Assim, a água fecha mesmo se a rede cair depois de abrir. A confirmar no produto.
- Montagem a investigar: relé Zigbee comercial com timer local + válvula solenoide NF (normalmente fechada) comum, ou válvula Zigbee pronta.

## Perguntas

1. A fechadura do box de chuveiro usa a mesma marca e a mesma senha da fechadura do quarto, ou outro meio (QR code, Bluetooth, outro)? → [fechadura.md](fechadura.md)
2. O que conta como um banho: a abertura do box, a liberação da água ou um tempo de água?
3. Quanto tempo o timer da válvula libera a água? O que acontece quando o tempo acaba?
4. Quem não tem reserva de quarto pode comprar um banho?
5. O que acontece quando a internet cai? O motorista com direito a banho consegue entrar no box?

## Ligação com o resto do sistema

- A Torre PX registra os banhos usados e os banhos pagos.
- O app do motorista mostra o direito ao banho e permite comprar outro banho.
- A central do local aciona a válvula pela mesh Zigbee → [hub-automacao.md](hub-automacao.md).
- O detector de fumaça do banheiro segue os requisitos de [detector-fumaca.md](detector-fumaca.md).
