# Diagramas do hardware

Cada diagrama tem duas versões:

- `.html`: a versão para abrir no navegador.
- `.svg`: a imagem que o GitHub mostra dentro dos `.md`.

O script `gerar.py` gera os cinco `.html`. Para mudar um diagrama, edite o `gerar.py`, e não o `.html`.

| Diagrama | Tipo | Usado em |
|---|---|---|
| `visao-geral` | Arquitetura | [../../README.md](../../README.md), [../README.md](../README.md) |
| `fluxo-senha` | Sequência | [../fechadura.md](../fechadura.md) |
| `rele-interruptores` | Arquitetura | [../rele-e-interruptores.md](../rele-e-interruptores.md) |
| `planta-quarto` | Maquete axonométrica do quarto (2 × 2,5 m) | [../../README.md](../../README.md), [../README.md](../README.md) |
| `planta-banheiro` | Maquete axonométrica do banheiro comunitário (6 × 2,4 m) | [../banheiro.md](../banheiro.md) |

## Atualizar

```bash
python3 hardware/diagramas/gerar.py
SKILL=~/.claude/plugins/cache/diagram-design/diagram-design/<versão>/skills/diagram-design
for f in visao-geral fluxo-senha rele-interruptores planta-quarto planta-banheiro; do
  python3 $SKILL/scripts/self_check.py hardware/diagramas/$f.html
  python3 $SKILL/scripts/export_svg.py hardware/diagramas/$f.html hardware/diagramas/$f.svg
done
```

O visual segue o perfil `px` da skill `diagram-design`. O arquivo `.diagram-design` na raiz do repo seleciona esse perfil.

A maquete do quarto usa 150 unidades de modelo por metro. Para ajustar uma medida ou um móvel, edite as listas `walls` e `things` da função `planta()`. A maquete do banheiro usa 100 unidades por metro, porque a sala de 6 m não cabe no quadro na escala do quarto. Para ajustar o banheiro, edite a função `planta_banheiro()`. As duas funções usam os helpers da classe `Axo`. A planta baixa do conjunto (vários quartos, quadro e banheiro) ainda não existe.
