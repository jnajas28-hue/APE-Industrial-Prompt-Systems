"""
metrics.py
Métricas básicas para evaluar el rendimiento de prompts sobre un dataset.

Estas métricas trabajan sobre pares (predicción, referencia).
La parte de generación de predicciones se implementa en evaluator.py.
"""

from typing import List


def exact_match(predictions: List[str], references: List[str]) -> float:
    """
    Calcula Exact Match: porcentaje de predicciones idénticas a la referencia.

    :param predictions: Lista de respuestas generadas.
    :param references: Lista de respuestas esperadas.
    :return: Valor entre 0.0 y 1.0
    """
    if not predictions or not references or len(predictions) != len(references):
        raise ValueError("Listas de predicciones y referencias inválidas.")

    total = len(predictions)
    aciertos = 0

    for p, r in zip(predictions, references):
        if p.strip() == r.strip():
            aciertos += 1

    return aciertos / total


def token_overlap(predictions: List[str], references: List[str]) -> float:
    """
    Métrica muy simple basada en solapamiento de tokens.
    NO es BLEU real, pero sirve como placeholder.

    :return: valor medio de solapamiento (0.0 a 1.0 aprox).
    """
    if not predictions or not references or len(predictions) != len(references):
        raise ValueError("Listas de predicciones y referencias inválidas.")

    scores = []

    for p, r in zip(predictions, references):
        p_tokens = set(p.lower().split())
        r_tokens = set(r.lower().split())

        if not p_tokens or not r_tokens:
            scores.append(0.0)
            continue

        inter = len(p_tokens & r_tokens)
        union = len(p_tokens | r_tokens)
        scores.append(inter / union)

    return sum(scores) / len(scores)
