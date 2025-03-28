# Analyze stack traces and extract root causes

import re

def extraer_stacktrace(log_lines):
    stack_blocks = []
    current_stack = []
    in_trace = False

    for line in log_lines:
        if "Traceback (most recent call last):" in line:
            in_trace = True
            if current_stack:
                stack_blocks.append(current_stack)
                current_stack = []
            current_stack.append(line)
        elif in_trace:
            if line.strip() == "" or re.match(r'^\s*\w+Error[:]', line):
                current_stack.append(line)
                stack_blocks.append(current_stack)
                current_stack = []
                in_trace = False
            else:
                current_stack.append(line)

    if current_stack:
        stack_blocks.append(current_stack)

    return stack_blocks

def analizar_causa_raiz(stacktrace_block):
    if not stacktrace_block:
        return None

    ultima_linea = stacktrace_block[-1].strip()
    match = re.match(r'^(\w+Error): (.*)', ultima_linea)
    if match:
        tipo_error, descripcion = match.groups()
        return {
            "tipo_error": tipo_error,
            "descripcion": descripcion,
            "causa_raiz": ultima_linea
        }

    return {
        "tipo_error": "Desconocido",
        "descripcion": ultima_linea,
        "causa_raiz": ultima_linea
    }

