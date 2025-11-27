"""
optimizer.py
Orquestador del ciclo APE: generar → evaluar → seleccionar → iterar.

Este optimizador es sencillo (búsqueda tipo "mejor de N" + iteraciones).
Más adelante se puede sustituir por algoritmos evolutivos más sofisticados.
"""

from typing import List, Dict, Any, Callable, Optional

from .generator import PromptGenerator
from .evaluator import PromptEvaluator


class APEOptimizer:
    """
    Optimiza prompts mediante búsqueda en caja negra.

    Flujo:
    1. Genera prompts candidatos
    2. Evalúa cada uno
    3. Selecciona el mejor
    4. (Opcional) Genera nuevas variantes a partir del mejor
    """

    def __init__(
        self,
        generator: Optional[PromptGenerator] = None,
        evaluator: Optional[PromptEvaluator] = None,
        n_candidates: int = 5,
    ) -> None:
        self.generator = generator or PromptGenerator()
        self.evaluator = evaluator or PromptEvaluator()
        self.n_candidates = n_candidates

    def optimize(
        self,
        examples: List[Dict[str, Any]],
        dataset_eval: List[Dict[str, Any]],
        n_iterations: int = 3,
        logger: Optional[Callable[[str], None]] = None,
    ) -> Dict[str, Any]:
        """
        Ejecuta el ciclo de optimización durante `n_iterations`.

        :param examples: ejemplos (input/output) para construir prompts.
        :param dataset_eval: dataset sobre el que evaluar rendimiento.
        :param n_iterations: número de iteraciones de búsqueda.
        :param logger: función opcional para loguear (print, logger, etc.).
        :return: dict con el mejor prompt y su score.
        """
        log = logger or (lambda msg: None)

        best_prompt: Optional[str] = None
        best_score: float = -1.0

        for it in range(n_iterations):
            log(f"[APE] Iteración {it+1}/{n_iterations}")

            candidates = self.generator.generate_candidates(
                examples=examples,
                n=self.n_candidates,
            )

            for idx, prompt in enumerate(candidates):
                score = self.evaluator.evaluate(prompt, dataset_eval)
                log(f"  - Candidato {idx+1}/{len(candidates)} → score={score:.4f}")

                if score > best_score:
                    best_score = score
                    best_prompt = prompt

            # En una versión más avanzada se podrían mutar los mejores prompts aquí

        return {
            "best_prompt": best_prompt,
            "best_score": best_score,
        }
