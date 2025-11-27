"""
generator.py
Módulo responsable de generar prompts candidatos a partir de ejemplos (input → output).

Este módulo NO llama todavía a ningún LLM.
Define la interfaz y una implementación mínima para empezar a trabajar.
"""

from typing import List, Dict, Any, Optional


class PromptGenerator:
    """
    Generador de prompts candidatos a partir de ejemplos anotados.

    Ejemplo de `examples`:
    [
        {"input": "texto de entrada", "output": "respuesta esperada"},
        ...
    ]
    """

    def __init__(self, base_instruction: Optional[str] = None) -> None:
        """
        :param base_instruction: Instrucción base sobre la que se generarán variantes.
        """
        self.base_instruction = base_instruction or (
            "Eres un modelo de lenguaje que debe imitar los ejemplos dados "
            "y producir respuestas consistentes, sin inventar datos."
        )

    def generate_candidates(
        self,
        examples: List[Dict[str, Any]],
        n: int = 5,
    ) -> List[str]:
        """
        Genera `n` prompts candidatos a partir de la instrucción base y los ejemplos.

        De momento genera variantes simples (placeholders) para ilustrar la estructura.
        Más adelante, aquí se conectará un LLM para proponer prompts nuevos.

        :param examples: Lista de pares input/output.
        :param n: Número de prompts candidatos a generar.
        :return: Lista de prompts candidatos (strings).
        """
        if not examples:
            raise ValueError("Se requieren ejemplos (input/output) para generar prompts.")

        candidates: List[str] = []

        # Plantilla muy básica para ilustrar la estructura
        template = (
            "{instruction}\n\n"
            "Tienes estos ejemplos de comportamiento deseado:\n"
            "{examples_block}\n\n"
            "Sigue el mismo patrón para cualquier nueva entrada."
        )

        examples_lines = []
        for ex in examples[:3]:  # no saturar el prompt inicial
            inp = ex.get("input", "").strip()
            out = ex.get("output", "").strip()
            examples_lines.append(f"Entrada: {inp}\nSalida esperada: {out}\n")

        examples_block = "\n".join(examples_lines)

        for i in range(n):
            variant_instruction = f"{self.base_instruction} (Variante {i+1})"
            prompt = template.format(
                instruction=variant_instruction,
                examples_block=examples_block,
            )
            candidates.append(prompt)

        return candidates
