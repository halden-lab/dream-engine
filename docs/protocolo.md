# Protocolo de ensayo

1. Cargar un conjunto de patrones de referencia y guardar una copia.
2. Ejecutar entre 3 y 7 noches con la misma semilla.
3. Tras cada noche, perturbar la memoria con `ruido.perturbar` y `ruido.borrar`.
4. Medir la **persistencia**: proporción de patrones de referencia que aún tienen un superviviente con similitud ≥ 0.92.
5. Anotar el ensayo en `experimentos/ensayos.csv`.

Los ensayos se lanzan de madrugada, cuando la máquina del laboratorio no tiene otra carga. Los resultados de día no son comparables.

Un ensayo se considera estable si la persistencia se mantiene por encima de 0.7 durante tres noches seguidas.
