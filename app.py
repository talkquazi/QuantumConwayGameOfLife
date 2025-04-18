import numpy as np
import pygame
import sys

# Quantum-corrected Conway's Game of Life using pygame
class QuantumLife:
    def __init__(self, size, cell_size=10, prob_alive=0.2):
        self.size = size
        self.cell_size = cell_size
        self.grid = np.random.choice([0, 1], size*size, p=[1-prob_alive, prob_alive]).reshape(size, size)
        self.superposition = np.zeros((size, size))
        self.entangled_pairs = {}  # Dict to store entangled cell pairs

        pygame.init()
        self.screen = pygame.display.set_mode((size * cell_size, size * cell_size))
        pygame.display.set_caption("Quantum Conway's Game of Life")

        # Color settings for visualization
        self.alive_color = (255, 255, 255)  # White for alive cells
        self.dead_color = (0, 0, 0)         # Black for dead cells
        self.superposition_color = (0, 150, 255)  # Blue for superposition

        # Initialize some entangled pairs
        self.entangle_cells()

    def entangle_cells(self):
        num_pairs = (self.size * self.size) // 50
        for _ in range(num_pairs):
            x1, y1 = np.random.randint(0, self.size, 2)
            x2, y2 = np.random.randint(0, self.size, 2)
            self.entangled_pairs[(x1, y1)] = (x2, y2)
            self.entangled_pairs[(x2, y2)] = (x1, y1)

    def step(self):
        new_grid = np.copy(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                total = (
                    self.grid[i, (j-1)%self.size] + self.grid[i, (j+1)%self.size] +
                    self.grid[(i-1)%self.size, j] + self.grid[(i+1)%self.size, j] +
                    self.grid[(i-1)%self.size, (j-1)%self.size] + self.grid[(i-1)%self.size, (j+1)%self.size] +
                    self.grid[(i+1)%self.size, (j-1)%self.size] + self.grid[(i+1)%self.size, (j+1)%self.size]
                )

                # Quantum superposition rule
                if total == 2:
                    self.superposition[i, j] = min(1.0, self.superposition[i, j] + 0.25)
                else:
                    self.superposition[i, j] = 0

                # Probabilistic collapse
                if self.superposition[i, j] >= 1.0:
                    if np.random.rand() < 0.5:
                        new_grid[i, j] = 1 - self.grid[i, j]
                    self.superposition[i, j] = 0
                else:
                    if self.grid[i, j] == 1 and (total < 2 or total > 3):
                        new_grid[i, j] = 0
                    elif self.grid[i, j] == 0 and total == 3:
                        new_grid[i, j] = 1

        # Improved entanglement: collect all changes before applying them
        entanglement_changes = {}
        for (x1, y1), (x2, y2) in self.entangled_pairs.items():
            if self.grid[x1, y1] != new_grid[x1, y1]:
                entanglement_changes[(x2, y2)] = new_grid[x1, y1]
        
        # Apply entanglement changes after all regular updates
        for (x, y), state in entanglement_changes.items():
            new_grid[x, y] = state

        self.grid = new_grid

    def draw_grid(self):
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                
                # Visualization logic including superposition
                if self.grid[x, y]:
                    # Alive cells
                    if self.superposition[x, y] > 0:
                        # Blend between alive color and superposition color
                        blend_factor = self.superposition[x, y]
                        color = self.blend_colors(self.alive_color, self.superposition_color, blend_factor)
                        pygame.draw.rect(self.screen, color, rect)
                    else:
                        pygame.draw.rect(self.screen, self.alive_color, rect)
                else:
                    # Dead cells
                    if self.superposition[x, y] > 0:
                        # Blend between dead color and superposition color
                        blend_factor = self.superposition[x, y]
                        color = self.blend_colors(self.dead_color, self.superposition_color, blend_factor)
                        pygame.draw.rect(self.screen, color, rect)
                    else:
                        pygame.draw.rect(self.screen, self.dead_color, rect)
                
                # Visualize entangled cells with a border
                if (x, y) in self.entangled_pairs:
                    pygame.draw.rect(self.screen, (255, 0, 255), rect, 1)  # Magenta border for entangled cells

    def blend_colors(self, color1, color2, blend_factor):
        """Blend two colors based on a factor (0.0 to 1.0)"""
        r = int(color1[0] * (1 - blend_factor) + color2[0] * blend_factor)
        g = int(color1[1] * (1 - blend_factor) + color2[1] * blend_factor)
        b = int(color1[2] * (1 - blend_factor) + color2[2] * blend_factor)
        return (r, g, b)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.step()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(10)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    qlife = QuantumLife(size=60, cell_size=10, prob_alive=0.2)
    qlife.run()