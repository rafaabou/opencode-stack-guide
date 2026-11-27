from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).with_name('diagram.png')
S = 2
W, H = 2008, 1230
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
REG = FONT_DIR / 'DejaVuSans.ttf'
BOLD = FONT_DIR / 'DejaVuSans-Bold.ttf'

BG = '#0B1220'
CARD = '#111C2E'
LINE = '#334155'
TEXT = '#E6EDF3'
MUTED = '#A8B6C8'
CYAN = '#38BDF8'
GREEN = '#34D399'
PURPLE = '#C084FC'
ORANGE = '#FBBF24'
BLUE = '#60A5FA'
GRAY = '#CBD5E1'
RED = '#FB7185'


def f(path, size):
    return ImageFont.truetype(str(path), int(size * S))


def sc(v):
    return int(v * S)


def wrap(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ''
    for word in words:
        candidate = f'{current} {word}'.strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def box(draw, x, y, w, h, title, body, accent, title_size=24, body_size=17):
    radius = 14
    draw.rounded_rectangle(
        [sc(x), sc(y), sc(x + w), sc(y + h)],
        radius=sc(radius),
        fill=CARD,
        outline=LINE,
        width=sc(2),
    )
    draw.rounded_rectangle(
        [sc(x), sc(y), sc(x + 7), sc(y + h)],
        radius=sc(4),
        fill=accent,
    )
    tf = f(BOLD, title_size)
    bf = f(REG, body_size)
    draw.text((sc(x + 24), sc(y + 18)), title, font=tf, fill=accent)
    lines = wrap(draw, body, bf, sc(w - 48))
    line_h = int(body_size * 1.35)
    for i, line in enumerate(lines[:5]):
        draw.text((sc(x + 24), sc(y + 58 + i * line_h)), line, font=bf, fill=MUTED)


def arrow(draw, x1, y1, x2, y2, color=BLUE, width=3, head=10):
    draw.line([sc(x1), sc(y1), sc(x2), sc(y2)], fill=color, width=sc(width))
    if abs(y2 - y1) < abs(x2 - x1):
        sign = 1 if x2 > x1 else -1
        pts = [(x2, y2), (x2 - sign * head, y2 - head * 0.65), (x2 - sign * head, y2 + head * 0.65)]
    else:
        sign = 1 if y2 > y1 else -1
        pts = [(x2, y2), (x2 - head * 0.65, y2 - sign * head), (x2 + head * 0.65, y2 - sign * head)]
    draw.polygon([(sc(px), sc(py)) for px, py in pts], fill=color)


def main():
    img = Image.new('RGB', (W * S, H * S), BG)
    d = ImageDraw.Draw(img)

    title = 'OpenCode Stack — one project, every layer in its place'
    sub = 'Herdr holds the work; OpenCode hosts it; Persona and memory load the context.'
    d.text((sc(80), sc(48)), title, font=f(BOLD, 39), fill=TEXT)
    d.text((sc(80), sc(98)), sub, font=f(REG, 20), fill=MUTED)

    # Context strip: what is loaded before work starts.
    box(d, 80, 145, 380, 108, 'PERSONA', 'role · language · detail · conventions', PURPLE)
    box(d, 500, 145, 420, 108, 'ENGRAM', 'cross-session decisions, bugs, constraints', PURPLE)
    box(d, 960, 145, 420, 108, 'OPENWOLF', 'project anatomy, buglog, do-not-repeat rules', PURPLE)
    box(d, 1420, 145, 508, 108, '47 SKILLS + 6 COMMANDS', 'repeatable knowledge and prompts', GRAY)

    # Main flow, first row.
    box(d, 80, 315, 300, 175, 'HERDR', 'workspaces · worktrees · panes · isolation', CYAN)
    box(d, 430, 315, 330, 175, 'OPENCODE', 'host · tools · permissions · TUI', CYAN)
    box(d, 810, 315, 330, 175, 'OPENSPEC', 'what: proposal · delta spec · tasks', GREEN)
    box(d, 1190, 315, 330, 175, 'GRAPHIFY', 'where: code graph · affected nodes', GREEN)
    box(d, 1570, 315, 358, 175, 'AGENTS', 'who: orchestrator, explorer, fixer, oracle, designer, observer, council', ORANGE)

    for x1, x2 in [(380, 430), (760, 810), (1140, 1190), (1520, 1570)]:
        arrow(d, x1, 402, x2, 402, BLUE)

    # Second row, right-to-left snake.
    box(d, 1570, 565, 358, 175, 'PONYTAIL', 'how little: smallest complete diff plus tests', ORANGE)
    box(d, 1190, 565, 330, 175, 'VERIFY', 'tests · review · spec fidelity · security', ORANGE)
    box(d, 810, 565, 330, 175, 'REMEMBER', 'Engram · OpenWolf · graph refresh', PURPLE)
    box(d, 430, 565, 330, 175, 'SHIP', 'archive · commit · push · pull request', BLUE)
    box(d, 80, 565, 300, 175, 'NEXT SESSION', 'less re-learning, faster handoffs', GRAY)

    arrow(d, 1749, 490, 1749, 565, BLUE)
    for x1, x2 in [(1570, 1520), (1190, 1140), (810, 760), (430, 380)]:
        arrow(d, x1, 652, x2, 652, BLUE)

    # Connectors from context and surfaces into the main flow.
    arrow(d, 270, 253, 230, 315, PURPLE, width=2, head=8)
    arrow(d, 710, 253, 595, 315, PURPLE, width=2, head=8)
    arrow(d, 1170, 253, 1355, 315, PURPLE, width=2, head=8)
    arrow(d, 1674, 253, 1749, 315, PURPLE, width=2, head=8)

    # Bottom: extension surfaces and one real-project example.
    box(d, 80, 805, 450, 150, 'PLUGINS + MCP', 'ponytail · persona · slim · engram · herdr bridge', CYAN, 22, 16)
    box(d, 570, 805, 450, 150, 'AGENT LANES', 'disjoint write scopes · Herdr worktrees · one writer per file', ORANGE, 22, 16)
    box(
        d, 1060, 805, 868, 150,
        'REAL PROJECT EXAMPLE',
        'POST /api/login rate limit → spec → graph → fixer → tests → review → PR',
        GREEN, 22, 16,
    )
    arrow(d, 305, 805, 305, 740, BLUE, width=2, head=8)
    arrow(d, 1494, 805, 1494, 740, BLUE, width=2, head=8)

    footer = (
        'Owners: Herdr = where  ·  OpenSpec = what  ·  Graphify = where in code  ·  '
        'Slim = who  ·  Ponytail = how much  ·  Engram/OpenWolf = what we learned  ·  '
        'Persona = how we speak'
    )
    d.text((sc(80), sc(1015)), footer, font=f(REG, 18), fill=GRAY)
    d.text((sc(80), sc(1055)), 'The diff, the test, the review and the memory are the product.', font=f(BOLD, 17), fill=TEXT)

    small = img.resize((W, H), Image.Resampling.LANCZOS)
    small.save(OUT, optimize=True)
    print(f'wrote {OUT} ({W}x{H})')


if __name__ == '__main__':
    main()
