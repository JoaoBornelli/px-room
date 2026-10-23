"""Gera os diagramas de hardware do quarto PX (HTML + SVG inline, skin PX).

Uso: python3 hardware/diagramas/gerar.py
Depois exporte cada .html para .svg com o export_svg.py da skill diagram-design
(veja hardware/diagramas/README.md).
"""
from math import ceil
from pathlib import Path

OUT = Path(__file__).parent

# Skin PX (perfil ~/.diagram-design/profiles/px.md)
PAPER = "#f6f7f9"
WHITE = "#ffffff"
INK = "#0F3D66"
MUTED = "#4B5563"
SOFT = "#5b6578"
ACCENT = "#1f6fbf"
LINK = "#117a42"
FN = "'Nunito', system-ui, sans-serif"
FM = "'Geist Mono', ui-monospace, monospace"
FS = "'Instrument Serif', 'Noto Serif', serif"


def ink(a):
    return f"rgba(15,61,102,{a})"


def acc(a):
    return f"rgba(31,111,191,{a})"


def mut(a):
    return f"rgba(75,85,99,{a})"


def r4(v):
    return int(ceil(v / 4.0) * 4)


TREAT = {
    "focal": (acc(0.08), ACCENT, None),
    "backend": (WHITE, INK, None),
    "device": (ink(0.05), MUTED, None),
    "external": (ink(0.03), ink(0.30), None),
    "input": (mut(0.10), SOFT, None),
    "optional": (ink(0.02), ink(0.30), "4,3"),
}

LEGEND_LABEL = {
    "focal": "FOCO DA INVESTIGAÇÃO",
    "backend": "SISTEMA PX / CONTROLE",
    "device": "DISPOSITIVO",
    "external": "SERVIÇO EXTERNO",
    "input": "PESSOA / ENTRADA",
    "optional": "A DEFINIR",
}

PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Nunito:wght@400;600;700&family=Geist+Mono:wght@400;500;600&family=Noto+Serif:ital@0;1&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --color-paper:   {paper};
      --color-ink:     {ink};
      --color-muted:   {muted};
      --color-accent:  {accent};
      --font-sans:     {fn};
      --font-serif:    {fs};
      --font-mono:     {fm};
    }}
    body {{
      font-family: var(--font-sans);
      background: var(--color-paper);
      color: var(--color-ink);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 3rem 2rem;
    }}
    .frame {{ max-width: 1200px; width: 100%; }}
    .diagram-container {{ width: 100%; overflow-x: auto; }}
    .eyebrow {{
      font-family: var(--font-mono);
      font-size: 0.66rem;
      font-weight: 500;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-muted);
      margin-bottom: 0.5rem;
    }}
    h1 {{
      font-family: var(--font-serif);
      font-size: clamp(1.5rem, 2.4vw + 0.75rem, 2rem);
      font-weight: 400;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: var(--color-ink);
      margin-bottom: 1.5rem;
    }}
    svg {{ width: 100%; min-width: {w}px; display: block; }}
    @media print {{
      .diagram-container {{ overflow-x: visible; }}
      svg {{ min-width: 0; }}
    }}
  </style>
</head>
<body>
  <div class="frame">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <div class="diagram-container">
      <svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="{slug}-title {slug}-desc">
        <title id="{slug}-title">{title}</title>
        <desc id="{slug}-desc">{desc}</desc>
        <defs>
          <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
          <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
          <marker id="arrow-link" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{link}"/></marker>
          <marker id="arrow-open" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polyline points="0 0, 8 3, 0 6" fill="none" stroke="{muted}" stroke-width="1.2"/></marker>
        </defs>
        <rect width="100%" height="100%" fill="{paper}"/>
{body}
      </svg>
    </div>
  </div>
</body>
</html>
"""


def page(slug, eyebrow, title, desc, w, h, parts):
    body = "\n".join("        " + p for p in parts)
    html = PAGE.format(
        slug=slug, eyebrow=eyebrow, title=title, desc=desc, w=w, h=h, body=body,
        paper=PAPER, ink=INK, muted=MUTED, accent=ACCENT, link=LINK, fn=FN, fs=FS, fm=FM,
    )
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")


# ---------- primitivas ----------

MARK = {MUTED: "arrow", ACCENT: "arrow-accent", LINK: "arrow-link"}


def arrow(d, color=MUTED, dashed=False, marker=None):
    m = marker or MARK[color]
    dash = ' stroke-dasharray="5,4"' if dashed else ""
    sw = "1" if dashed else "1.2"
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{dash} marker-end="url(#{m})"/>'


def label_w(text):
    return r4(len(text) * 8 * 0.62 + 12)


def label_above(cx, line_y, text):
    w = label_w(text)
    return (f'<rect x="{cx - w / 2:g}" y="{line_y - 20}" width="{w}" height="12" rx="2" fill="{PAPER}"/>'
            f'<text x="{cx:g}" y="{line_y - 11}" fill="{SOFT}" font-size="8" font-family="{FM}" '
            f'text-anchor="middle" letter-spacing="0.06em">{text}</text>')


def label_right(line_x, cy, text):
    w = label_w(text)
    x = line_x + 8
    return (f'<rect x="{x}" y="{cy - 6}" width="{w}" height="12" rx="2" fill="{PAPER}"/>'
            f'<text x="{x + w / 2:g}" y="{cy + 3}" fill="{SOFT}" font-size="8" font-family="{FM}" '
            f'text-anchor="middle" letter-spacing="0.06em">{text}</text>')


def node(x, y, w, h, kind, tag, name, sub):
    fill, stroke, dash = TREAT[kind]
    d = f' stroke-dasharray="{dash}"' if dash else ""
    cx, cy = x + w / 2, y + h / 2
    tag_color = ACCENT if kind == "focal" else SOFT
    tag_stroke = acc(0.40) if kind == "focal" else ink(0.25)
    tw = r4(len(tag) * 7 * 0.62 + 10)
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{PAPER}"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1"{d}/>'
        f'<rect x="{x + 8}" y="{y + 6}" width="{tw}" height="12" rx="2" fill="none" stroke="{tag_stroke}" stroke-width="0.8"/>'
        f'<text x="{x + 8 + tw / 2:g}" y="{y + 15}" fill="{tag_color}" font-size="7" font-family="{FM}" '
        f'text-anchor="middle" letter-spacing="0.08em">{tag}</text>'
        f'<text x="{cx:g}" y="{cy + (4 if sub else 10):g}" fill="{INK}" font-size="12" font-weight="600" font-family="{FN}" '
        f'text-anchor="middle">{name}</text>'
        f'<text x="{cx:g}" y="{cy + 18:g}" fill="{MUTED}" font-size="9" font-family="{FM}" '
        f'text-anchor="middle">{sub}</text>'
    )


def zone(x, y, w, h, text):
    lw = r4(len(text) * 7 * 0.62 + 16)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{ink(0.02)}" stroke="{ink(0.10)}" stroke-width="0.8"/>'
            f'<rect x="{x + 12}" y="{y + 4}" width="{lw}" height="12" rx="2" fill="{PAPER}"/>'
            f'<text x="{x + 12 + lw / 2:g}" y="{y + 13}" fill="{SOFT}" font-size="7" font-family="{FM}" '
            f'text-anchor="middle" letter-spacing="0.14em">{text}</text>')


def legend(y, w, kinds, arrows):
    """kinds: lista de tratamentos de nó; arrows: lista de (cor, tracejado, texto)."""
    out = [f'<line x1="24" y1="{y - 8}" x2="{w - 24}" y2="{y - 8}" stroke="{ink(0.10)}" stroke-width="0.8"/>',
           f'<text x="24" y="{y + 12}" fill="{MUTED}" font-size="8" font-family="{FM}" letter-spacing="0.14em">LEGENDA</text>']
    x = 100
    for k in kinds:
        fill, stroke, dash = TREAT[k]
        d = f' stroke-dasharray="{dash}"' if dash else ""
        text = LEGEND_LABEL[k]
        out.append(f'<rect x="{x}" y="{y + 4}" width="16" height="10" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="1"{d}/>')
        out.append(f'<text x="{x + 22}" y="{y + 12}" fill="{MUTED}" font-size="8" font-family="{FM}" letter-spacing="0.08em">{text}</text>')
        x += r4(22 + len(text) * 8 * 0.62 + 20)
    for color, dashed, text, *marker in arrows:
        dash = ' stroke-dasharray="5,4"' if dashed else ""
        m = marker[0] if marker else MARK[color]
        out.append(f'<line x1="{x}" y1="{y + 9}" x2="{x + 24}" y2="{y + 9}" stroke="{color}" stroke-width="1.2"{dash} marker-end="url(#{m})"/>')
        out.append(f'<text x="{x + 32}" y="{y + 12}" fill="{MUTED}" font-size="8" font-family="{FM}" letter-spacing="0.08em">{text}</text>')
        x += r4(32 + len(text) * 8 * 0.62 + 20)
    assert x <= w, f"legenda estoura a largura: {x} > {w}"
    return out


# ---------- 1. visão geral ----------

def visao_geral():
    W, H = 960, 648
    A, B, C = 64, 400, 736          # colunas (x da caixa), largura 160
    NW, NH = 160, 56
    R1, R2, R3, R4 = 96, 216, 344, 480
    p = []
    p.append(zone(376, 64, 544, 112, "NUVEM"))
    p.append(zone(40, 312, 880, 256, "LOCAL (UNIDADE)"))
    p.append(zone(40, 448, 664, 104, "QUARTO · MESH ZIGBEE"))
    p.append(zone(720, 448, 200, 104, "BANHEIRO"))
    # nuvem
    p.append(arrow(f"M {A + NW},{R1 + 28} H {B}"))
    p.append(label_above((A + NW + B) / 2, R1 + 28, "TROCA PREVISTA"))
    p.append(arrow(f"M {B + NW},{R1 + 28} H {C}", LINK))
    p.append(label_above((B + NW + C) / 2, R1 + 28, "PEDE SENHA"))
    p.append(arrow(f"M 440,{R1 + NH} V {R2 + 20} Q 440,{R2 + 28} 432,{R2 + 28} H {A + NW}"))
    p.append(label_above(328, R2 + 28, "SENHA + QUARTO"))
    p.append(arrow(f"M {B + 80},{R1 + NH} V {R3}"))
    p.append(label_right(B + 80 - 16 - label_w("INTERNET"), 296, "INTERNET"))
    # app → fechadura (o motorista digita a senha)
    p.append(arrow(f"M {A + 80},{R2 + NH} V {R3}", dashed=True))
    p.append(label_right(A + 80, 288, "DIGITA A SENHA"))
    # voz (fase 2) → central
    p.append(arrow(f"M {C},{R2 + 28} H 528 V {R3}", dashed=True))
    p.append(label_above((528 + C) / 2, R2 + 28, "WI-FI"))
    # central → coordenador → mesh
    p.append(arrow(f"M {B + NW},{R3 + 28} H {C}"))
    p.append(label_above((B + NW + C) / 2, R3 + 28, "ETHERNET / PoE"))
    bus = R3 + NH + 24
    drops = [A + 80, 368, 592, C + 80]
    p.append(f'<path d="M {C + 80},{R3 + NH} V {bus} H {drops[0]}" fill="none" stroke="{MUTED}" stroke-width="1.2"/>')
    for x in drops:
        p.append(arrow(f"M {x},{bus} V {R4}"))
    p.append(label_above(480, bus, "MESH ZIGBEE"))
    # caixas
    p.append(node(A, R1, NW, NH, "external", "EXT", "Contrato e rota", "define a troca"))
    p.append(node(B, R1, NW, NH, "backend", "API", "Torre PX", "pré-reserva → senha"))
    p.append(node(C, R1, NW, NH, "external", "EXT", "API da fechadura", "marca a definir"))
    p.append(node(A, R2, NW, NH, "input", "APP", "App do motorista", "senha + info"))
    p.append(node(C, R2, NW, NH, "optional", "VOZ", "Assistente de voz", "fase 2 · ESP32-S3"))
    p.append(node(A, R3, NW, NH, "focal", "LOCK", "Fechadura do quarto", "fora da Zigbee · offline"))
    p.append(node(B, R3, NW, NH, "focal", "HUB", "Central do local", "MQTT · Zigbee2MQTT"))
    p.append(node(C, R3, NW, NH, "device", "ZB", "Coordenador Zigbee", "de rede"))
    p.append(node(A, R4, NW, NH, "device", "ZB", "Relé de parede", "roteador + interruptor"))
    p.append(node(288, R4, NW, NH, "device", "ZB", "Sensor de porta", "bateria"))
    p.append(node(512, R4, NW, NH, "device", "ZB", "Emissor IR", "ar-condicionado"))
    p.append(node(C, R4, NW, NH, "device", "ZB", "Válvula do chuveiro", "NF · timer"))
    p += legend(600, W, ["focal", "backend", "external", "input", "device", "optional"],
                [(LINK, False, "API")])
    page("visao-geral", "Arquitetura · Quarto PX", "Quarto PX: central do local e mesh Zigbee",
         "Arquitetura do quarto PX: a Torre PX pré-reserva o quarto, pede a senha offline à API da fechadura (marca a definir) e a envia ao app; "
         "o motorista digita a senha na fechadura, que fica fora da rede Zigbee. A central do local fala com a Torre e, pelo coordenador Zigbee, "
         "com a mesh do quarto (relé de parede, sensor de porta, emissor infravermelho) e do banheiro (válvula do chuveiro). O assistente de voz é opcional, fase 2.",
         W, H, p)


# ---------- 2. fluxo da senha (sequência) ----------

def frag(fx, fy, fw, fh, tag, text):
    tw = 8 + len(tag) * 8
    return [f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="4" fill="{ink(0.02)}" stroke="{ink(0.22)}" stroke-width="1"/>',
            f'<rect x="{fx}" y="{fy}" width="{tw}" height="16" rx="2" fill="{PAPER}" stroke="{ink(0.22)}" stroke-width="1"/>',
            f'<text x="{fx + tw / 2:g}" y="{fy + 12}" fill="{MUTED}" font-size="8" font-family="{FM}" text-anchor="middle" letter-spacing="0.12em">{tag}</text>',
            f'<text x="{fx + tw + 12}" y="{fy + 12}" fill="{MUTED}" font-size="8" font-family="{FM}" letter-spacing="0.04em">{text}</text>']


def fluxo_senha():
    W, H = 1100, 852
    X = [90, 238, 386, 534, 682, 830, 978]
    names = [("EXT", "Contrato e rota", "external", ""), ("API", "Torre PX", "backend", ""),
             ("EXT", "API da fechadura", "external", "marca a definir"), ("APP", "Motorista (app)", "input", ""),
             ("LOCK", "Fechadura", "focal", "offline"), ("HUB", "Central do local", "backend", ""),
             ("ZB", "Sensor de porta", "device", "")]
    BW, BH, TOP = 128, 48, 48
    BOTTOM = 776
    p = []
    for x in X:
        p.append(f'<line x1="{x}" y1="{TOP + BH}" x2="{x}" y2="{BOTTOM}" stroke="{ink(0.20)}" stroke-width="1" stroke-dasharray="3,3"/>')
    p += frag(40, 484, 1020, 156, "PAR", "[em paralelo: o sensor de porta avisa a central]")
    p += frag(40, 664, 420, 104, "OPT", "[troca cancelada · só com gateway]")

    def msg(a, b, y, text, color=MUTED, dashed=False, marker=None, lx=None):
        x1, x2 = X[a], X[b]
        end = x2 - 2 if x2 > x1 else x2 + 2
        p.append(arrow(f"M {x1},{y} H {end}", color, dashed, marker))
        p.append(label_above(lx if lx is not None else (x1 + x2) / 2, y, text))

    def selfmsg(a, sy, text):
        sx = X[a]
        p.append(f'<path d="M {sx},{sy} H {sx + 24} Q {sx + 32},{sy} {sx + 32},{sy + 8} V {sy + 16} Q {sx + 32},{sy + 24} {sx + 24},{sy + 24} H {sx + 2}" '
                 f'fill="none" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#arrow)"/>')
        w = label_w(text)
        p.append(f'<rect x="{sx + 40}" y="{sy + 6}" width="{w}" height="12" rx="2" fill="{PAPER}"/>'
                 f'<text x="{sx + 40 + w / 2:g}" y="{sy + 15}" fill="{SOFT}" font-size="8" font-family="{FM}" text-anchor="middle" letter-spacing="0.06em">{text}</text>')

    msg(0, 1, 140, "TROCA PREVISTA")
    selfmsg(1, 176, "PRÉ-RESERVA")
    msg(1, 2, 236, "PEDE SENHA", LINK)
    msg(2, 1, 272, "SENHA", dashed=True)
    msg(1, 3, 320, "SENHA + QUARTO", ACCENT)
    msg(3, 4, 368, "DIGITA SENHA")
    selfmsg(4, 400, "VALIDA OFFLINE")
    msg(4, 3, 452, "DESTRAVA", dashed=True)
    msg(6, 5, 528, "PORTA ABERTA", ACCENT)
    selfmsg(5, 556, "LIGA A LUZ")
    msg(5, 1, 616, "REGISTRA ENTRADA", dashed=True)
    msg(0, 1, 712, "CANCELA TROCA")
    msg(1, 2, 748, "REVOGA SENHA", LINK)
    for x, (tag, name, kind, sub) in zip(X, names):
        p.append(node(x - BW // 2, TOP, BW, BH, kind, tag, name, sub))
    p += legend(800, W, ["focal", "backend", "external", "input", "device"],
                [(LINK, False, "API"), (MUTED, True, "RESPOSTA / REGISTRO")])
    page("fluxo-senha", "Sequência · Quarto PX", "Quarto PX: da reserva à porta aberta",
         "Sequência da senha do quarto: o contrato prevê a troca, a Torre PX pré-reserva o quarto, pede a senha offline à API da fechadura (marca a definir) "
         "e a envia ao app. O motorista digita a senha, e a fechadura valida sem rede e abre. Em paralelo, o sensor de porta avisa a central do local, "
         "que liga a luz e registra a entrada na Torre. Se a troca é cancelada, a Torre revoga a senha, desde que exista gateway.",
         W, H, p)


# ---------- 3. relé e interruptores ----------

def rele_interruptores():
    W, H = 960, 560
    A, B, C = 48, 400, 752
    NW, NH = 160, 56
    R1, R2, R3 = 96, 264, 408
    p = []
    p.append(zone(728, 232, 208, 256, "127/220 V"))
    # linha 1: sensor → coordenador ⇄ central
    p.append(arrow(f"M {A + NW},{R1 + 28} H {B}"))
    p.append(label_above((A + NW + B) / 2, R1 + 28, "PORTA ABERTA"))
    p.append(arrow(f"M {C},{R1 + 16} H {B + NW}"))
    p.append(label_above((B + NW + C) / 2, R1 + 16, "EVENTO"))
    p.append(arrow(f"M {B + NW},{R1 + 44} H {C}"))
    p.append(label_above((B + NW + C) / 2, R1 + 44, "COMANDO"))
    # coordenador → relé pela mesh
    p.append(arrow(f"M {B + 80},{R1 + NH} V {R2}", dashed=True))
    p.append(label_right(B + 80, (R1 + NH + R2) / 2, "MESH ZIGBEE"))
    # interruptor → relé (local, sem a central)
    p.append(arrow(f"M {A + NW},{R2 + 28} H {B}", LINK))
    p.append(label_above((A + NW + B) / 2, R2 + 28, "LOCAL, SEM A CENTRAL"))
    p.append(arrow(f"M {B + NW},{R2 + 28} H {C}", ACCENT))
    p.append(label_above((B + NW + C) / 2, R2 + 28, "LIGA / DESLIGA"))
    p.append(arrow(f"M {C},{R3 + 28} H {B + 88} Q {B + 80},{R3 + 28} {B + 80},{R3 + 20} V {R2 + NH}"))
    p.append(label_above((B + 88 + C) / 2, R3 + 28, "FASE E NEUTRO?"))
    p.append(node(A, R1, NW, NH, "device", "ZB", "Sensor de porta", "bateria"))
    p.append(node(B, R1, NW, NH, "device", "ZB", "Coordenador Zigbee", "de rede"))
    p.append(node(C, R1, NW, NH, "backend", "HUB", "Central do local", "Zigbee2MQTT + regras"))
    p.append(node(A, R2, NW, NH, "input", "IN", "Interruptor", "pulsador ou chave?"))
    p.append(node(B, R2, NW, NH, "focal", "ZB", "Relé Zigbee de parede", "roteador + entrada"))
    p.append(node(C, R2, NW, NH, "device", "DEV", "Lâmpada", "ponto de luz"))
    p.append(node(C, R3, NW, NH, "external", "AC", "Rede elétrica", "disjuntor"))
    p += legend(512, W, ["focal", "backend", "input", "device", "external"],
                [(LINK, False, "SINAL LOCAL"), (MUTED, True, "ZIGBEE")])
    page("rele-interruptores", "Arquitetura · Quarto PX", "Quarto PX: relé Zigbee e interruptor",
         "O interruptor liga na entrada do relé Zigbee de parede e aciona a luz sem a central. A central do local também comanda o relé pela mesh Zigbee, "
         "por meio do coordenador. Quando o sensor de porta abre, o evento chega à central, que liga a luz pelo relé. O relé chaveia a fase da rede elétrica para a lâmpada.",
         W, H, p)


# ---------- 4. maquetes axonométricas (quarto e banheiro) ----------

def iso(x, y, z, ox, oy):
    return ox + x - y, oy + (x + y) / 2 - z


def caixa(nome, x0, y0, x1, y1, z, h, focal=False, estilo=""):
    """Caixa da maquete. estilo: "" (móvel), "parede", "vidro" ou "redondo" (cilindro)."""
    return (nome, x0, y0, x1, y1, z, h, focal, estilo)


class Axo:
    """Helpers da maquete axonométrica (projeção dimétrica 2:1, origem em ox, oy)."""

    def __init__(self, ox, oy, w):
        self.ox, self.oy, self.w = ox, oy, w

    def pt(self, x, y, z):
        return iso(x, y, z, self.ox, self.oy)

    def P(self, x, y, z):
        sx, sy = self.pt(x, y, z)
        return f"{sx:g} {sy:g}"

    @staticmethod
    def poly(pts):
        return "M " + " L ".join(pts) + " Z"

    def prism(self, x0, y0, x1, y1, z, h, focal=False, strong=False, glass=False):
        P, poly, t = self.P, self.poly, z + h
        sil = poly([P(x0, y1, t), P(x0, y0, t), P(x1, y0, t), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)])
        left = poly([P(x0, y1, t), P(x1, y1, t), P(x1, y1, z), P(x0, y1, z)])
        right = poly([P(x1, y1, t), P(x1, y0, t), P(x1, y0, z), P(x1, y1, z)])
        top = poly([P(x0, y1, t), P(x0, y0, t), P(x1, y0, t), P(x1, y1, t)])
        edges = f"M {P(x0, y1, t)} L {P(x1, y1, t)} L {P(x1, y0, t)} M {P(x1, y1, t)} L {P(x1, y1, z)}"
        sw = "1.2" if strong else "0.8"
        out = f'<path data-role="silhouette" d="{sil}" fill="{WHITE}"/>'
        if focal:
            out += (f'<path d="{top}" fill="{acc(0.10)}"/><path d="{left}" fill="{acc(0.20)}"/>'
                    f'<path d="{right}" fill="{acc(0.32)}"/>')
        elif glass:
            out += f'<path d="{left}" fill="{ink(0.03)}"/><path d="{right}" fill="{ink(0.06)}"/>'
        else:
            out += f'<path d="{left}" fill="{ink(0.07)}"/><path d="{right}" fill="{ink(0.15)}"/>'
        out += (f'<path d="{edges}" fill="none" stroke="{ink(0.55)}" stroke-width="0.8"/>'
                f'<path d="{sil}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>')
        return out

    def cylinder(self, cx, cy, r, z, h, focal=False):
        """Cilindro de raio r em pé no ponto (cx, cy). Na projeção 2:1 o círculo vira elipse r*sqrt(2) x r/sqrt(2)."""
        rx, ry = r * 2 ** 0.5, r / 2 ** 0.5
        sx, st = self.pt(cx, cy, z + h)
        sb = st + h
        L, R = f"{sx - rx:g} {st:g}", f"{sx + rx:g} {st:g}"
        Lb, Rb = f"{sx - rx:g} {sb:g}", f"{sx + rx:g} {sb:g}"
        a = f"{rx:g} {ry:g} 0 0"
        sil = f"M {L} A {a} 1 {R} L {Rb} A {a} 1 {Lb} Z"
        side = f"M {L} L {Lb} A {a} 0 {Rb} L {Rb} L {R} A {a} 1 {L} Z"
        side_fill = acc(0.32) if focal else ink(0.15)
        top_fill = acc(0.10) if focal else WHITE
        return (f'<path data-role="silhouette" d="{sil}" fill="{WHITE}"/>'
                f'<path d="{side}" fill="{side_fill}"/>'
                f'<ellipse cx="{sx:g}" cy="{st:g}" rx="{rx:g}" ry="{ry:g}" fill="{top_fill}"/>'
                f'<path d="M {L} A {a} 0 {R}" fill="none" stroke="{ink(0.55)}" stroke-width="0.8"/>'
                f'<path d="{sil}" fill="none" stroke="{INK}" stroke-width="0.8" stroke-linejoin="round"/>')

    def boxes(self, boxes):
        """Pinta as caixas de trás para frente (ordem topológica, como pede a skill)."""
        ox, oy = self.ox, self.oy

        def screen_bbox(b):
            _, x0, y0, x1, y1, z, h, _, _ = b
            pts = [iso(x, y, zz, ox, oy) for x in (x0, x1) for y in (y0, y1) for zz in (z, z + h)]
            xs, ys = [q[0] for q in pts], [q[1] for q in pts]
            return min(xs), min(ys), max(xs), max(ys)

        def overlap(a, b):
            A_, B_ = screen_bbox(a), screen_bbox(b)
            return A_[0] < B_[2] and B_[0] < A_[2] and A_[1] < B_[3] and B_[1] < A_[3]

        def behind(a, b):
            if a[3] <= b[1] or a[4] <= b[2]:          # a.x1 <= b.x0 ou a.y1 <= b.y0
                return True
            stacked = a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]
            return stacked and a[5] + a[6] <= b[5]    # a embaixo de b, na mesma planta

        order, rest = [], list(boxes)
        while rest:
            for cand in rest:
                if not any(o is not cand and overlap(o, cand) and behind(o, cand) for o in rest):
                    order.append(cand)
                    rest.remove(cand)
                    break
            else:
                raise RuntimeError("ordem de pintura sem solução")

        out = []
        for name, x0, y0, x1, y1, z, h, focal, estilo in order:
            kind = "wall" if estilo == "parede" else "furniture"
            f = " data-focal" if focal else ""
            if estilo == "redondo":
                r = (x1 - x0) / 2
                shape = self.cylinder((x0 + x1) / 2, (y0 + y1) / 2, r, z, h, focal)
            else:
                r = 0
                shape = self.prism(x0, y0, x1, y1, z, h, focal, glass=(estilo == "vidro"))
            out.append(f'<g data-box data-rect="{x0:g} {y0:g} {x1:g} {y1:g} {r:g}" data-z="{z:g}" data-h="{h:g}" '
                       f'data-kind="{kind}"{f}>{shape}</g>')
        return out

    def ceiling(self, cx, cy, r, floor_z, ceil_z, h=6):
        """Item de teto: cilindro rente ao teto, prumo tracejado até o piso e a marca do ponto no piso."""
        sx, sf = self.pt(cx, cy, floor_z)
        _, sb = self.pt(cx, cy, ceil_z - h)
        rx, ry = r * 2 ** 0.5, r / 2 ** 0.5
        return [
            f'<ellipse cx="{sx:g}" cy="{sf:g}" rx="{rx:g}" ry="{ry:g}" fill="none" stroke="{ink(0.35)}" stroke-width="0.8" stroke-dasharray="3,3"/>',
            f'<path d="M {sx:g} {sb:g} L {sx:g} {sf:g}" fill="none" stroke="{ink(0.35)}" stroke-width="0.8" stroke-dasharray="3,3"/>',
            f'<g data-box data-rect="{cx - r:g} {cy - r:g} {cx + r:g} {cy + r:g} {r:g}" data-z="{ceil_z - h:g}" data-h="{h:g}" '
            f'data-kind="furniture">{self.cylinder(cx, cy, r, ceil_z - h, h)}</g>',
        ]

    def dim(self, a, b, tk, label, z=0):
        A, B = self.pt(*a, z), self.pt(*b, z)
        out = f'<path d="M {A[0]:g} {A[1]:g} L {B[0]:g} {B[1]:g}" fill="none" stroke="{MUTED}" stroke-width="0.8"/>'
        for q in (a, b):
            t0 = self.pt(q[0] - tk[0], q[1] - tk[1], z)
            t1 = self.pt(q[0] + tk[0], q[1] + tk[1], z)
            out += f'<path d="M {t0[0]:g} {t0[1]:g} L {t1[0]:g} {t1[1]:g}" fill="none" stroke="{MUTED}" stroke-width="0.8"/>'
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        w = r4(len(label) * 9 * 0.62 + 12)
        out += (f'<rect x="{mx - w / 2:g}" y="{my - 8:g}" width="{w}" height="16" rx="2" fill="{PAPER}"/>'
                f'<text x="{mx:g}" y="{my + 4:g}" fill="{SOFT}" font-size="9" font-family="{FM}" text-anchor="middle" letter-spacing="0.06em">{label}</text>')
        return out

    def tags(self, tags):
        """tags: (nome, sublabel, ponto de modelo, deslocamento em tela, focal)."""
        out, placed = [], []
        for name, sub, (mx, my, mz), (dx, dy), focal in tags:
            sx, sy = self.pt(mx, my, mz)
            sx, sy = sx + dx, sy + dy
            w = r4(max(len(name) * 12 * 0.6, len(sub) * 8 * 0.62) + 16)
            rx, ry = sx - w / 2, sy - 16
            assert rx >= 8 and rx + w <= self.w - 8 and ry >= 8, f"etiqueta fora do quadro: {name}"
            for (ax, ay, aw) in placed:
                assert rx + w <= ax or ax + aw <= rx or ry + 32 <= ay or ay + 32 <= ry, f"etiquetas sobrepostas: {name}"
            placed.append((rx, ry, w))
            stroke = ACCENT if focal else ink(0.12)
            color = ACCENT if focal else INK
            subc = ACCENT if focal else MUTED
            out.append(f'<g data-role="tag" data-name="{name}" data-at="{mx:g} {my:g} {mz:g}">'
                       f'<rect x="{rx:g}" y="{ry:g}" width="{w}" height="32" rx="2" fill="{WHITE}" stroke="{stroke}" stroke-width="0.8"/>'
                       f'<text data-role="name" x="{sx:g}" y="{sy:g}" text-anchor="middle" fill="{color}" font-size="12" font-weight="600" font-family="{FN}">{name}</text>'
                       f'<text x="{sx:g}" y="{sy + 11:g}" text-anchor="middle" fill="{subc}" font-size="8" font-family="{FM}" letter-spacing="0.08em">{sub}</text></g>')
        return out

    def plate(self, px, py, t):
        return (f'<g data-plate data-rect="0 0 {px} {py} 0" data-z="0" data-t="{t}">'
                f'{self.prism(0, 0, px, py, 0, t, strong=True)}</g>')

    def note(self, y, text):
        return [f'<text x="96" y="{y}" fill="{ACCENT}" font-size="8" font-family="{FM}" letter-spacing="0.18em">MAQUETE</text>',
                f'<text x="168" y="{y}" fill="{MUTED}" font-size="10" font-family="{FS}" font-style="italic">{text}</text>']


def planta():
    """Quarto PX: 2 m x 2,5 m. Escala: 150 unidades de modelo por metro."""
    W = 1000
    OX, OY = 480, 280
    PX, PY = 312, 387                 # placa: interior 300 x 375 (2 m x 2,5 m) + paredes de 6
    T = 6                             # espessura da placa
    WH = 22                           # parede cortada na altura da mesa
    TETO = T + 390                    # teto a 2,6 m
    ax = Axo(OX, OY, W)

    # paredes (x0, y0, x1, y1). Parede dos fundos (y=0): janela. Parede da frente (y=381..387): porta, vão de x=180 a x=300.
    walls = [
        (0, 0, 312, 6), (0, 6, 6, 387), (306, 6, 312, 387),
        (6, 381, 180, 387), (300, 381, 306, 387),
    ]
    things = [
        caixa("Cama", 12, 12, 140, 297, T, 8),
        caixa("Colchão", 14, 14, 138, 295, T + 8, 10),
        caixa("Travesseiro", 20, 18, 132, 58, T + 18, 6),
        caixa("Cômoda", 246, 150, 306, 270, T, 30),
        caixa("Assistente", 266, 190, 284, 208, T + 30, 10),
        caixa("janela", 144, 1, 270, 5, T + WH, 46, estilo="vidro"),
        caixa("Ar-condicionado", 144, 6, 270, 24, T + WH + 48, 18),
        caixa("Interruptor", 300, 381, 306, 387, T + WH, 12),
        caixa("Fechadura", 168, 381, 180, 387, T + WH, 14, focal=True),
    ]
    boxes = [caixa("parede", *w, T, WH, estilo="parede") for w in walls] + things

    p = [f'<g data-axo-plan data-origin="{OX} {OY}">', ax.plate(PX, PY, T),
         '<g data-room data-name="Quarto" data-rect="6 6 306 381 0"></g>']
    p += ax.boxes(boxes)
    # detector de fumaça: disco de 12 cm no centro do teto, com prumo até o piso
    p += ax.ceiling(156, 193.5, 9, T, TETO)
    p.append(ax.dim((0, PY + 22), (PX, PY + 22), (0, 6), "2 m"))
    p.append(ax.dim((PX + 22, 0), (PX + 22, PY), (6, 0), "2,5 m"))
    p += ax.tags([
        ("Cama", "solteiro", (76, 170, T + 18), (0, 0), False),
        ("Ar-condicionado", "sobre a janela", (207, 15, T + WH + 66), (-30, -22), False),
        ("Janela", "parede de 2 m", (270, 3, T + WH + 24), (70, 0), False),
        ("Porta", "fechadura com senha", (200, 340, T), (0, 0), True),
        ("Interruptor", "ao lado da porta", (303, 384, T + WH + 12), (70, 24), False),
        ("Assistente", "sobre a cômoda", (275, 199, T + 40), (90, -10), False),
        ("Detector de fumaça", "no teto, a 2,6 m", (156, 193.5, TETO - 3), (112, 4), False),
    ])
    p.append("</g>")
    p += ax.note(680, "Medidas aproximadas. O teto não aparece: as paredes estão cortadas na altura da mesa. "
                      "A luz e o detector de fumaça ficam no teto.")
    page("planta-quarto", "Maquete axonométrica · Quarto PX", "Quarto PX: 2 × 2,5 m",
         "Maquete do quarto PX com 2 por 2,5 metros: cama de solteiro, janela com ar-condicionado em cima na parede dos fundos, "
         "porta com fechadura na parede oposta, cômoda com o assistente de voz, interruptor ao lado da porta "
         "e detector de fumaça no centro do teto.",
         W, 704, p)


def planta_banheiro():
    """Banheiro comunitário: 6 m x 2,4 m. Escala: 100 unidades de modelo por metro."""
    W = 1000
    OX, OY = 320, 228
    PX, PY = 612, 252                 # placa: interior 600 x 240 (6 m x 2,4 m) + paredes de 6
    T, WH = 6, 22
    TETO = T + 260                    # teto a 2,6 m
    FUNDO = 126                       # boxes de 1,2 m junto à parede dos fundos; o resto é corredor
    PORTA = (151, 231)                # vão de 80 cm na parede da direita (2,4 m), no corredor
    ax = Axo(OX, OY, W)
    bw = 600 / 7                      # 7 boxes de ~0,85 m em 6 m
    xs = [6 + bw * k for k in range(8)]
    CHUVEIROS, VASOS = range(0, 4), range(4, 7)   # chuveiros no fundo à esquerda, vasos perto da entrada

    walls = [
        (0, 0, PX, 6), (0, 6, 6, PY),
        (606, 6, PX, PORTA[0]), (606, PORTA[1], PX, PY),
        (6, PY - 6, 606, PY),
    ]
    boxes = [caixa("parede", *w, T, WH, estilo="parede") for w in walls]
    # divisórias entre os boxes (3 cm), cortadas na mesma altura das paredes
    for x in xs[1:7]:
        boxes.append(caixa("divisória", x - 1.5, 6, x + 1.5, FUNDO, T, WH, estilo="parede"))
    for k in range(7):
        x0 = xs[k] + (1.5 if k else 0)
        x1 = xs[k + 1] - (1.5 if k < 6 else 0)
        cx = (xs[k] + xs[k + 1]) / 2
        boxes.append(caixa("porta do box", x0, FUNDO - 4, x1, FUNDO, T, WH, estilo="vidro"))
        if k in VASOS:   # vaso: caixa acoplada + bacia
            boxes.append(caixa("caixa acoplada", cx - 18, 6, cx + 18, 22, T, 76))
            boxes.append(caixa("vaso", cx - 16, 22, cx + 16, 68, T, 40))
        else:            # chuveiro: cano na parede, válvula solenoide no cano, braço e ducha; fechadura na porta
            boxes.append(caixa("cano", cx - 2, 6, cx + 2, 10, T, 110))
            boxes.append(caixa("válvula", cx - 6, 6, cx + 6, 16, T + 110, 14))
            boxes.append(caixa("cano", cx - 2, 6, cx + 2, 10, T + 124, 80))
            boxes.append(caixa("braço", cx - 2, 10, cx + 2, 16, T + 200, 4))
            boxes.append(caixa("ducha", cx - 9, 16, cx + 9, 34, T + 198, 4, estilo="redondo"))
            boxes.append(caixa("fechadura", x1 - 14, FUNDO - 4, x1 - 6, FUNDO, T + WH, 12, focal=True))

    p = [f'<g data-axo-plan data-origin="{OX} {OY}">', ax.plate(PX, PY, T)]
    # piso do chuveiro: marca plana em cada box de chuveiro
    for k in CHUVEIROS:
        a, b = xs[k] + 6, xs[k + 1] - 6
        pts = [ax.P(a, 12, T), ax.P(b, 12, T), ax.P(b, FUNDO - 10, T), ax.P(a, FUNDO - 10, T)]
        p.append(f'<path d="{ax.poly(pts)}" fill="{ink(0.07)}"/>')
    p.append(f'<g data-room data-name="Boxes de chuveiro" data-rect="6 6 {xs[4]:g} {FUNDO} 0"></g>')
    p.append(f'<g data-room data-name="Boxes de vaso" data-rect="{xs[4]:g} 6 606 {FUNDO} 0"></g>')
    p.append(f'<g data-room data-name="Corredor" data-rect="6 {FUNDO} 606 {PY - 6} 0"></g>')
    p += ax.boxes(boxes)
    DX, DY = 510, 186                 # detector de 12 cm no teto do corredor, entre os chuveiros e os vasos
    p += ax.ceiling(DX, DY, 6, T, TETO)
    p.append(ax.dim((0, PY + 22), (PX, PY + 22), (0, 6), "6 m"))
    p.append(ax.dim((PX + 22, 0), (PX + 22, PY), (6, 0), "2,4 m"))
    p += ax.tags([
        ("Válvula solenoide Zigbee", "com timer, 1 por chuveiro", ((xs[0] + xs[1]) / 2, 11, T + 117), (-114, 0), False),
        ("4 boxes de chuveiro", "1,2 × 0,85 m cada", ((xs[0] + xs[4]) / 2, 186, T), (0, 0), False),
        ("Fechadura (a definir)", "1 por box de chuveiro", (xs[4] - 11.5, FUNDO - 2, T + WH + 12), (0, 50), True),
        ("3 boxes de vaso", "sem fechadura controlada", ((xs[6] + xs[7]) / 2, 14, T + 76), (31, -62), False),
        ("Detector de fumaça", "no teto, a 2,6 m", (DX, DY, TETO - 3), (94, -15), False),
        ("Entrada", "porta do corredor", (609, sum(PORTA) / 2, T), (-70, 0), False),
    ])
    p.append("</g>")
    p += ax.note(732, "Medidas aproximadas. O teto não aparece: as paredes e as divisórias estão cortadas na altura da mesa.")
    page("planta-banheiro", "Maquete axonométrica · Quarto PX", "Banheiro comunitário: 6 × 2,4 m",
         "Maquete do banheiro comunitário, 6 m × 2,4 m, boxes de 1,2 m × 0,85 m: 4 boxes de chuveiro de um lado e 3 boxes de vaso "
         "do outro, em fileira ao longo de uma parede de 6 m, com corredor de 1,2 m. Cada box de chuveiro tem fechadura na porta, "
         "que libera a entrada do motorista, e válvula solenoide Zigbee com timer, que libera a água só durante o banho. "
         "A entrada fica numa parede de 2,4 m, sem controle de acesso, e um detector de fumaça fica no teto do corredor.",
         W, 756, p)


if __name__ == "__main__":
    visao_geral()
    fluxo_senha()
    rele_interruptores()
    planta()
    planta_banheiro()
    print("ok:", ", ".join(sorted(f.name for f in OUT.glob("*.html"))))
