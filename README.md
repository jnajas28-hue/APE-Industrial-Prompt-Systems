# APE Industrial Prompt Systems

Sistema APE (Automatic Prompt Engineer) para generar, evaluar y optimizar *prompts* industriales usando búsqueda en caja negra y métricas objetivas. Incluye datasets, motor de evaluación, optimización evolutiva y casos reales de negocio.

> No es arte.  
> Es ingeniería evolutiva aplicada al lenguaje.

---

## 🚀 ¿Qué hace este proyecto?

Este repositorio implementa un sistema completo de ingeniería automática de prompts (APE):

1. **Generación** — El sistema crea múltiples prompts candidatos a partir de ejemplos (input → output).
2. **Evaluación** — Cada prompt se prueba en tareas reales y se valora con métricas como Accuracy, F1 o Exact Match.
3. **Optimización** — El motor realiza una búsqueda en caja negra para encontrar el prompt con mejor rendimiento.

---

## 📁 Estructura prevista del proyecto

```text
APE-Industrial-Prompt-Systems/
│
├── datasets/        # Conjuntos input→output para evaluación
├── engine/          # Lógica de generación, evaluación y optimización
├── docs/            # Documentación técnica
└── examples/        # Casos de uso orientados a negocio
