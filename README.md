# Quantum Conway's Game of Life

A quantum-inspired, pygame-powered take on Conway’s Game of Life. This simulation incorporates concepts like **superposition**, **probabilistic collapse**, and **non-local entanglement**, visualized in real time using glowing gradients and entanglement outlines.

![Quantum Life Screenshot](quantumgameoflife.png)

## ✨ Features

- 🧬 **Quantum Superposition**: Cells that are surrounded by exactly 2 neighbors accumulate “uncertainty” over time, simulating superposition. This is rendered with a smooth blue blending effect.
- 🎲 **Probabilistic Collapse**: Once a cell's uncertainty reaches a threshold, it has a 50% chance of flipping its state. This models the stochastic nature of quantum measurement collapse.
- 🔗 **Entanglement**: Pairs of randomly selected cells are non-locally linked. If one changes, the other is forced to match—no matter the distance between them.
- 🎨 **Quantum Visualization**:
  - **Alive cells** are white.
  - **Superposition** adds a glowing blue overlay as uncertainty increases.
  - **Entangled cells** are outlined in **magenta (purple)** to show their linked quantum connection, even when they are “off.”
- ⚫ **Binary Aesthetic**: Maintains the black/white pixel grid clarity of classic Conway's Life, now with quantum logic layered beneath.

## 🧠 Conceptual Notes

This simulation is not a literal quantum system but mirrors key principles:

- **Superposition** is modeled with a numeric range (0 to 1) and a gradual visual glow.
- **Collapse** occurs based on a threshold and a random outcome, as in quantum measurements.
- **Entanglement** is implemented via enforced state mirroring between linked cells.
- **Non-locality** is realized through state changes that ignore spatial proximity.

The flickering “static” pixels you might observe are the result of **unstable collapses**—quantum outcomes that appear momentarily before vanishing due to lack of environmental support, similar to quantum decoherence.

## 🚀 Requirements

- Python 3.7+
- `pygame`
- `numpy`

Install dependencies:

```bash
pip install pygame numpy
