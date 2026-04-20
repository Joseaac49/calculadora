# 🧪 QA Automation - Calculadora en Python

Proyecto de automatización de pruebas utilizando **Pytest**, enfocado en validar operaciones matemáticas básicas y manejo de errores.

---

## 📌 Descripción

Este proyecto simula una calculadora simple y aplica testing automatizado siguiendo buenas prácticas de QA.

Se validan:

- Operaciones básicas
- Casos positivos y negativos
- Manejo de errores
- Tests parametrizados

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Pytest
- Pytest-html

---

## 🧮 Funcionalidades

- ➕ Suma
- ➖ Resta
- ✖️ Multiplicación
- ➗ División

---

## 🧪 Casos de prueba cubiertos

- Valores positivos
- Valores negativos
- Cero
- Números grandes
- Números flotantes
- División por cero (manejo de excepción)

---

## 📁 Estructura del proyecto


calculadora/
│── operaciones.py

test/
│── test_calculadora.py
│── conftest.py

pytest.ini


---

## ▶️ Cómo ejecutar los tests

```bash
pytest


pytest --html=reporte.html --self-contained-html

Luego abrir: 

reporte.html

🎯 Objetivo

Este proyecto fue desarrollado como práctica de QA Automation, con el objetivo de:

Aprender Pytest
Implementar buenas prácticas de testing
Simular escenarios reales de testing funcional

🚀 Autor

Jose Aguilar
QA Automation Trainee