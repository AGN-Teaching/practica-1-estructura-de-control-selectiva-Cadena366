[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rMafNWiN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18553515)
# Práctica 1. Estructura de control selectiva


# Presentación del problema  
En esta práctica, se me pide desarrollar un programa en Python que permita determinar las apuestas ganadoras en un juego de ruleta.
La ruleta contiene 38 espacios numerados del 0 al 36, más el "00".  

Las apuestas consideradas incluyen:  
- Apuestas a un número específico  
- Apuestas al color (rojo o negro)  
- Apuestas a números pares o impares  
- Apuestas por rango (1-18 o 19-36)  

El objetivo es que el programa reciba un número de entrada y muestre todas las apuestas ganadoras.

# Diseño del algoritmo  
Para resolver el problema, el algoritmo sigue estos pasos:  
1. Solicitar al usuario un número entre 0 y 36 o "00".  
2. Verificar si el número es "0" o "00" (ya que no cuentan para otras apuestas).  
3. Determinar si el número es rojo o negro. Se usa una lista con los números rojos y, si el número no está en ella, se asume negro. 
4. Verificar si el número es par o impar.  
5. Determinar si pertenece al rango 1-18 o 19-36.  
6. Mostrar las apuestas ganadoras correspondientes.  

# Implementación en Python  
En la implementación se utilizó input() para recibir la entrada del usuario y print() para mostrar los resultados. Se emplearon 
estructuras condicionales if, elif y else para verificar cada una de las condiciones de la ruleta. Se usaron listas para almacenar 
los números rojos, evitando estructuras más complejas. También se aplicó el operador % para determinar si un número es par o impar. 
De esta manera, el programa sigue una estructura lógica que facilita la verificación de las apuestas ganadoras.


