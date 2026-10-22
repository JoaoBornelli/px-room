# Banheiro comunitário

> Estado: 🟡 investigando · [← painel do hardware](README.md)

O quarto tem só o dormitório. O banheiro fica fora do quarto e é comunitário. O banheiro tem controle de acesso.

## Regras de negócio

| Regra | Valor | Estado |
|---|---|---|
| Banho grátis | 1 | Definido. Confirmar: 1 por reserva ou 1 por dia? |
| Banho extra | Pago pelo motorista | Definido. Preço e meio de pagamento: a definir |

## Controle do chuveiro

A automação do chuveiro aciona uma válvula solenoide. A válvula libera ou bloqueia a água. A automação não chaveia a energia do chuveiro.

## Perguntas

1. O controle de acesso fica na porta do banheiro ou em cada box?
2. Como o motorista se identifica no banheiro: senha, QR code ou Bluetooth?
3. O que conta como um banho: a entrada no box, a liberação da água ou um tempo de água?
4. O banho tem tempo máximo? O que acontece quando o tempo acaba?
5. Quem não tem reserva de quarto pode comprar um banho?
6. O que acontece quando a internet cai? O motorista com direito a banho consegue entrar?
7. O controle de acesso usa a mesma fechadura e a mesma API do quarto? → [fechadura.md](fechadura.md)

## Ligação com o resto do sistema

- O backend PX registra os banhos usados e os banhos pagos.
- O app do motorista mostra o direito ao banho e permite comprar outro banho.
- O hub ou outro controlador aciona a válvula solenoide → [hub-automacao.md](hub-automacao.md).
