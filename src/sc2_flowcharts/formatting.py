import re
from catppuccin import PALETTE

flavor = PALETTE.frappe

# Colors
TEXT_COLOR = flavor.colors.text.hex
TIME_COLOR = flavor.colors.yellow.hex
SUPPLY_COLOR = flavor.colors.pink.hex
SCOUT_COLOR = flavor.colors.green.hex
ATTACK_COLOR = flavor.colors.red.hex
REACTION_COLOR = flavor.colors.blue.hex
EDGE_COLOR = flavor.colors.overlay2.hex
RED = flavor.colors.red.hex
GREEN = flavor.colors.green.hex

# Formatting for HTML table cells
TABLE_CELL = '<TD border="0" align="left">{}</TD>'
TITLE_CELL = '<TD border="0" align="center"><B>{}</B></TD>'
COLOUR_STEP = '<FONT color="{}">{}</FONT>'
TABLE_FSTRING = '<<TABLE cellpadding="0" cellspacing="0" align="left" border="0" cellborder="0">{}</TABLE>>'

GRAPH_ATTR = dict(style="filled,rounded", fillcolor=flavor.colors.base.hex, bgcolor=flavor.colors.base.hex, fontcolor=flavor.colors.text.hex)
NODE_ATTR = dict(shape="box", style="rounded,filled", fontcolor=flavor.colors.text.hex, fillcolor=flavor.colors.crust.hex, color=flavor.colors.crust.hex, fontname="Sans Serif", fontsize="16")
EDGE_ATTR = dict(color=EDGE_COLOR, fontcolor=TEXT_COLOR, penwidth="2", fontname="Sans Serif", fontsize="16")


def parse_step(step: str):
    target, step_type, step = _parse_step(step)
    res = [_color_step(step_type, step)]
    if target:
        res.append(f"<B>{_parse_time_or_supply(target)}</B>")
    res_formatted = "\n".join(TABLE_CELL.format(s.strip()) for s in res)
    return f'<TR>{res_formatted}</TR>'

def format_title(title: str):
    """
    Format a title for the table.
    """
    title_cell = TITLE_CELL.format(title.strip())
    return f'<TR>{title_cell}</TR>'
    

def _parse_step(step: str) -> tuple:
    """
    Parse string with formats:
        `12 Build pool`
        `12 Build pool`
        `1:45 Build pool`
        `1:45 (12) Build pool`
    """
    ts_or_supply = r"(?:\d+:\d+)|(?:\d+)"
    step_type = r"(?: ?[BAST] )"
    reg = f"({ts_or_supply})?\s*?({step_type})?\s*?(.+)"
    match = re.match(reg, step)
    return match.groups()

def _parse_time_or_supply(group: str):
    if ":" in group:
        color = TIME_COLOR
    else:
        color = SUPPLY_COLOR
    return COLOUR_STEP.format(color, group.strip())

def _color_step(step_type: str|None, step: str):
    color = TEXT_COLOR
    step = (step or "").strip()
    step_type = (step_type or "").strip()
    if step_type == "S":
        color = SCOUT_COLOR
    elif step_type == "A":
        color = ATTACK_COLOR
    elif step_type == "T":
        step = f"\t{step}"
    return COLOUR_STEP.format(color, step.strip())