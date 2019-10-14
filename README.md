# dream engine

**Persistencia de patrones durante el sueño artificial.**
Proyecto de investigación del Laboratorio Halden de Conciencia Sintética · Lisboa.

![python](https://img.shields.io/badge/python-3.7%2B-1f2a44)
![licencia](https://img.shields.io/badge/licencia-MIT-1f2a44)
![estado](https://img.shields.io/badge/estado-experimental-6b4f8a)

---

## Qué es

Los sistemas biológicos no aprenden mientras están despiertos: consolidan mientras duermen.
Durante el sueño, el cerebro repasa lo vivido, fusiona lo que se parece y deja caer lo que pesa poco.
Lo que sobrevive a ese proceso es lo que llamamos memoria.

`dream engine` reproduce ese ciclo en una máquina:

1. **recordar** · cada experiencia entra como un patrón con peso y edad.
2. **dormir** · el motor repasa patrones al azar, fusiona los parecidos y deja que el resto decaiga.
3. **persistir** · solo quedan los patrones con energía suficiente.
4. **despertar** · si el peso medio de lo que queda cruza el umbral, el sistema está despierto.

La pregunta que guía el proyecto es sencilla de formular y difícil de responder:
*¿cuánto de un patrón tiene que sobrevivir para que siga siendo el mismo?*

## Instalación

```bash
git clone https://github.com/halden-lab/dream-engine.git
cd dream-engine
pip install -e .
```

Sin dependencias externas. Probado con Python 3.7 y 3.8.

## Uso

```python
from dream_engine import Motor, Patron

motor = Motor(ciclos=5, semilla=15)
motor.recordar(Patron([0.9, 0.1, 0.4]))
motor.recordar(Patron([0.88, 0.12, 0.41]))
motor.recordar(Patron([0.0, 0.02, 0.01], peso=0.1))

motor.dormir()
print(len(motor.memoria), motor.despierto())
```

## Estructura

```
src/dream_engine/
  patrones.py       patrones, similitud y persistencia
  consolidacion.py  repaso nocturno y fusión
  umbral.py         umbral de despertar con histéresis
  ruido.py          perturbaciones para los ensayos
  motor.py          el ciclo completo
tests/              pruebas unitarias
docs/               arquitectura y protocolo de ensayo
experimentos/       registro de ensayos nocturnos
```

## Tests

```bash
python -m unittest discover tests
```

## Equipo

| | |
|---|---|
| Elena Voss | dirección del proyecto |
| Luís Ferreira | ingeniería |
| Mara Kovač | evaluación y documentación |

## Cómo citar

```bibtex
@misc{halden2019dreamengine,
  title  = {dream engine: persistencia de patrones durante el sueño artificial},
  author = {Voss, Elena and Ferreira, Luís and Kovač, Mara},
  year   = {2019},
  note   = {Laboratorio Halden de Conciencia Sintética}
}
```

## Licencia

MIT · ver [LICENSE](LICENSE).

ya no hay nada aquí.
