# HangMan
# Hangman 1.0 — Documentación del proyecto

**Autor:** Santiago Lazo Villarraga  
**Correo:** s.lazo@utp.edu.co

---

## 1. Descripción del juego

Hangman 1.0 es una implementación del clásico juego del ahorcado, en el que el jugador debe adivinar una palabra oculta ingresando letras individuales. El jugador dispone de **6 vidas** para descubrir la palabra antes de perder la partida.

## 2. Reglas del juego

### 2.1. Inicio de la partida

- El juego seleccionará una palabra aleatoria del archivo `palabras.txt`.
- Cada letra de la palabra se representará inicialmente mediante un guion bajo (`_`).
- El jugador comenzará con **6 vidas disponibles**.

### 2.2. Ingreso de letras

- El jugador solo podrá ingresar una letra por interacción.
- Únicamente se aceptarán letras del alfabeto inglés, comprendidas entre `A` y `Z`.
- No se permitirán números, símbolos, espacios, la letra `Ñ` del alfabeto español ni entradas vacías.
- Las letras ingresadas no podrán repetirse.

### 2.3. Aciertos y errores

- **Acierto:** si la letra pertenece a la palabra oculta, se revelarán todas sus apariciones.
- **Error:** si la letra no pertenece a la palabra, el jugador perderá una vida.
- **Letra repetida:** se mostrará una advertencia y no se descontarán vidas.
- **Entrada inválida:** se solicitará nuevamente una letra válida sin descontar vidas.

### 2.4. Condiciones de victoria y derrota

| Resultado | Condición | Acción |
|---|---|---|
| Victoria | Se adivinan todas las letras de la palabra. | Mostrar un mensaje de felicitación. |
| Derrota | El contador de vidas llega a cero. | Revelar la palabra oculta y mostrar un mensaje de derrota. |

### 2.5. Finalización de la partida

Al finalizar cada partida, se mostrará un menú con las siguientes opciones:

1. **Jugar de nuevo:** iniciar una nueva partida con otra palabra y restablecer las 6 vidas.
2. **Salir:** finalizar la ejecución del juego.

> [!IMPORTANT]
> Las entradas inválidas y las letras repetidas no deben descontar vidas. Solo se pierde una vida cuando se ingresa una letra válida que no pertenece a la palabra oculta.

---

## 3. Estructura del proyecto

El proyecto se llamará `hangman_1_0` y estará organizado en tres archivos:

```text
hangman_1_0/
├── juego.py
├── palabras.txt
└── monigote.txt
```

| Archivo | Responsabilidad |
|---|---|
| `juego.py` | Contiene la lógica principal, las validaciones, el control de vidas y el menú. |
| `palabras.txt` | Almacena las palabras disponibles para seleccionar aleatoriamente. |
| `monigote.txt` | Contiene las representaciones del ahorcado correspondientes a cada cantidad de vidas. |

---

## 4. Lista de tareas (Task List)

### 4.1. Configuración inicial

- [x] Nombrar el proyecto `hangman_1_0`.
- [x] Definir los tres archivos principales: `juego.py`, `palabras.txt` y `monigote.txt`.

### 4.2. Gestión de palabras

- [X] Leer las palabras almacenadas en `palabras.txt`.
- [X] Seleccionar una palabra aleatoria al iniciar cada partida.
- [ ] Representar cada letra de la palabra mediante un guion bajo (`_`).
- [ ] Actualizar la palabra visible cuando el jugador acierte una letra.

### 4.3. Validación de entradas

- [X] Permitir únicamente una letra por interacción.
- [X] Rechazar entradas que contengan más de una letra.
- [X] Validar que la entrada pertenezca al rango `A-Z`.
- [X] Detectar letras repetidas y mostrar el mensaje correspondiente.
- [ ] Evitar que las entradas inválidas descuenten vidas.

### 4.4. Control de vidas y representación gráfica en consola

- [ ] Establecer un total de 6 vidas por partida.
- [ ] Descontar una vida cuando se ingrese una letra válida que no esté en la palabra.
- [ ] Mostrar las vidas restantes después de cada intento válido.
- [X] Cargar los monigotes desde el archivo `monigote.txt`.
- [ ] Mostrar el monigote correspondiente a las vidas restantes.

### 4.5. Condiciones de finalización

- [ ] Detectar cuándo el jugador ha adivinado la palabra completa.
- [ ] Mostrar un mensaje de victoria cuando corresponda.
- [ ] Detectar cuándo el contador de vidas llega a cero.
- [ ] Mostrar un mensaje de derrota y revelar la palabra oculta.
- [ ] Mostrar el menú de opciones al finalizar cada partida.
- [ ] Implementar la opción de jugar nuevamente.
- [ ] Implementar la opción de salir del juego.
- [ ] Restablecer correctamente el estado de la partida al reiniciar.

---

## 5. Criterios de aceptación

El proyecto se considerará funcional cuando cumpla las siguientes condiciones:

- [X] Las palabras se seleccionan aleatoriamente desde el archivo correspondiente.
- [ ] Las entradas se validan correctamente.
- [ ] Las letras acertadas se revelan en todas sus posiciones.
- [ ] Las vidas se descuentan únicamente por errores válidos.
- [ ] El monigote coincide con el número de vidas restantes.
- [ ] La victoria y la derrota se detectan correctamente.
- [ ] El menú permite reiniciar o cerrar el juego sin errores.

---

## 6. Decisiones tomadas

### 6.1. Libreria os

Al intentar cargar los archivos con el `whit`...`open` me generaba errores ya que no encontraba
la direccion de los archivos por esa razon opte por usar la libreria os

### 6.2. Libreria random
Con ayuda de esta libreria se escoge una palabra aleatoria de la lista que consera las palabras del archivo `palabras.txt`
