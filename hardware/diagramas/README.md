# Diagramas do hardware

Cada diagrama tem duas versões:

- `.html`: a versão para abrir no navegador.
- `.svg`: a imagem que o GitHub mostra dentro dos `.md`.

O script `gerar.py` gera os quatro `.html`. Para mudar um diagrama, edite o `gerar.py`, e não o `.html`.

| Diagrama | Tipo | Usado em |
|---|---|---|
| `visao-geral` | Arquitetura | [../README.md](../README.md) |
| `fluxo-senha` | Sequência | [../fechadura.md](../fechadura.md) |
| `rele-interruptores` | Arquitetura | [../rele-e-interruptores.md](../rele-e-interruptores.md) |
| `planta-quarto` | Planta axonométrica (ilustrativa) | [../README.md](../README.md) |

## Atualizar

```bash
python3 hardware/diagramas/gerar.py
SKILL=~/.claude/plugins/cache/diagram-design/diagram-design/<versão>/skills/diagram-design
for f in visao-geral fluxo-senha rele-interruptores planta-quarto; do
  python3 $SKILL/scripts/self_check.py hardware/diagramas/$f.html
  python3 $SKILL/scripts/export_svg.py hardware/diagramas/$f.html hardware/diagramas/$f.svg
done
```

O visual segue o perfil `px` da skill `diagram-design`. O arquivo `.diagram-design` na raiz do repo seleciona esse perfil.

Quando a planta baixa chegar, troque as listas `walls` e `things` da função `planta()` pelas medidas reais.
