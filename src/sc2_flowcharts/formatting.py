import re


# Colors
TIME_COLOR = "firebrick"
SUPPLY_COLOR = "darkgoldenrod3"
SCOUT_COLOR = "green"
ATTACK_COLOR = "red"

# Formatting for HTML table cells
TABLE_CELL = '<TD border="0" align="left">{}</TD>'
COLOUR_STEP = '<FONT color="{}">{}</FONT>'
TABLE_FSTRING = '<<TABLE cellpadding="0" cellspacing="0" align="left" border="0" cellborder="0">{}</TABLE>>'



def parse_step(step: str):
    target, step_type, step = _parse_step(step)
    res = [_color_step(step_type, step)]
    if target:
        res.append(f"<B>{_parse_time_or_supply(target)}</B>")
    res_formatted = "\n".join(TABLE_CELL.format(s.strip()) for s in res)
    return f'<TR>{res_formatted}</TR>'
    

def _parse_step(step: str) -> tuple:
    """
    Parse string with formats:
        `12 Build pool`
        `12 Build pool`
        `1:45 Build pool`
        `1:45 (12) Build pool`
    """
    ts_or_supply = r"(?:\d+:\d+)|(?:\d+)"
    step_type = r"(?: ?[BAS] )"
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
    color = "black"
    step_type = (step_type or "").strip()
    if step_type == "S":
        color = SCOUT_COLOR
    elif step_type == "A":
        color = ATTACK_COLOR
    return COLOUR_STEP.format(color, step.strip())