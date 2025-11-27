"""
evaluator.py
Evalúa el rendimiento de un prompt sobre un dataset dado.

Este módulo define la interfaz de evaluación.
La integración real con un LLM (GPT, Claude, etc.) se añadirá después.
"""

from typing import List, Dict, Any, Callable

from .metrics import exact_match, token_overlap


class PromptEvaluator:
    """
    Evaluador de prompts.

    Toma:
    - un prompt
    - un dataset (lista de pares input/output)
    - una función de métrica

    Y devuelve una puntuación numérica.
    """

    def __init__(
        self,
        metric_fn: Callable[[List[str], List[str]], float] = exact_match,
    ) -> None:
        self.metric_fn = metric_fn

    def _run_model(self, prompt: str, inputs: List[str]) -> List[str]:
        """
        Punto de integración con el modelo de lenguaje.

        Ahora mismo es un stub. Más adelante:
        - llamada a API (OpenAI, Anthropic, etc.)
        - control de temperatura, max_tokens, etc.

        :param prompt: Prompt a evaluar.
        :param inputs: Lista de entradas del dataset.
        :return: Lista de predicciones generadas por el modelo.
        """
        # TODO: implementar integración real con LLM.
        # De momento, devolvemos respuestas vacías del mismo tamaño.
        return ["" for _ in inputs]

    def evaluate(self, prompt: str, dataset: List[Dict[str, Any]]) -> float:
        """
        Evalúa un único prompt sobre un dataset.

        :param prompt: Prompt candidato.
        :param dataset: Lista de dicts con campos "input" y "output".
        :return: puntuación según la métrica configurada.
        """
        if not dataset:
            raise ValueError("El dataset no puede estar vacío.")

        inputs = [item.get("input", "") for item in dataset]
        refs = [item.get("output", "") for item in dataset]

        preds = self._run_model(prompt, inputs)
        score = self.metric_fn(preds, refs)
        return score


def evaluate_with_both_metrics(prompt: str, dataset: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Ejemplo de evaluación combinada con dos métricas:
    - exact_match
    - token_overlap
    """
    evaluator_em = PromptEvaluator(metric_fn=exact_match)
    evaluator_to = PromptEvaluator(metric_fn=token_overlap)

    inputs = [item.get("input", "") for item in dataset]
    refs = [item.get("output", "") for item in dataset]

    preds = evaluator_em._run_model(prompt, inputs)

    return {
        "exact_match": exact_match(preds, refs),
        "token_overlap": token_overlap(preds, refs),
    }
