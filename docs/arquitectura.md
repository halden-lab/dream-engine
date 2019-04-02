# Arquitectura

El motor tiene cuatro etapas. Cada una es una función pura sobre una lista de patrones, salvo el propio `Motor`, que guarda el estado entre noches.

```
 vigilia                    sueño                         vigilia
┌─────────┐   ┌─────────┐   ┌──────────┐   ┌───────────┐   ┌──────────┐
│recordar │ → │ repasar │ → │ fusionar │ → │ persistir │ → │ despierto│
└─────────┘   └─────────┘   └──────────┘   └───────────┘   └──────────┘
```

## Patrón

Un vector de valores reales, un peso entre 0 y 1 y una edad en ciclos. La **energía** de un patrón es la norma de sus valores multiplicada por su peso.

## Repaso

En cada ciclo todos los patrones envejecen y pierden peso (`decaimiento`). Uno de ellos, elegido al azar, se refuerza. Es la versión más simple de la reactivación que se observa en el hipocampo durante el sueño de ondas lentas.

## Fusión

Dos patrones cuya similitud coseno supera `parecido` se consideran el mismo recuerdo. El superviviente hereda la mitad del peso del absorbido y la mayor de las dos edades.

## Persistencia

Se descarta todo patrón con energía menor que `minimo`. Es la única etapa que destruye información.

## Despertar

El sistema está despierto cuando el peso medio de la memoria supera el umbral. Desde la 0.2 el umbral tiene histéresis para que el estado no parpadee cerca del límite.
