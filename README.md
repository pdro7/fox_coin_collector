# Fox Coin Collector 🦊💰

Un juego simple desarrollado en Python usando pygame donde controlas a un zorro que debe recoger monedas antes de que se acabe el tiempo.

## Características

- **Zorro controlable**: Muévete con las flechas o WASD
- **Monedas animadas**: Con efectos visuales de brillo y pulsación
- **Timer de 60 segundos**: Recoge todas las monedas que puedas
- **Sistema de puntuación**: Cada moneda suma un punto
- **Estados del juego**: Menú inicial, juego y pantalla final
- **Efectos visuales**: Animaciones, sombras y efectos de color

## Controles

- **Flechas** o **WASD**: Mover al zorro
- **ESPACIO**: Comenzar juego (desde el menú)
- **R**: Reiniciar juego (después de terminar)
- **ESC**: Salir del juego

## Instalación y Ejecución

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd fox_coin_collector
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el juego:
```bash
python3 main.py
```

## Estructura del Proyecto

```
fox_coin_collector/
├── main.py                 # Punto de entrada del juego
├── game/
│   ├── __init__.py
│   ├── player.py           # Clase del zorro
│   ├── coin.py             # Clase de las monedas
│   ├── timer.py            # Manejo del tiempo
│   └── ui.py               # Interfaz de usuario
├── assets/
│   └── images/             # Sprites (futuro)
├── requirements.txt        # Dependencias
└── README.md              # Este archivo
```

## Objetivo del Juego

¡Ayuda al zorro a recoger el mayor número de monedas posible en 60 segundos! Cada vez que tocas una moneda, tu puntuación aumenta y aparece una nueva moneda en una posición aleatoria.

## Desarrollo

Este juego fue desarrollado siguiendo un enfoque incremental:
1. Configuración inicial y ventana básica
2. Implementación del jugador con movimiento
3. Creación del sistema de monedas
4. Sistema de colisiones
5. Timer y puntuación
6. Estados del juego
7. Mejoras visuales y efectos

## Tecnologías Utilizadas

- **Python 3.9+**
- **Pygame 2.6+**

---

🎮 ¡Diviértete jugando y trata de conseguir la puntuación más alta!