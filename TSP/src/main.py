from heuristic import tsp_nearest_neighbor
from dynamic import tsp_held_karp
from utils import load_cost_matrix
import matplotlib.pyplot as plt
import random

def generate_random_coords(n, seed=42):
    random.seed(seed)
    return [(random.randint(0, 10), random.randint(0, 10)) for _ in range(n)]

def plot_routes(coords, nn_route, nn_cost, hk_route, hk_cost, title):
    plt.figure(figsize=(6,6))
    for i, (x, y) in enumerate(coords):
        plt.scatter(x, y, c="black")
        plt.text(x + 0.2, y + 0.2, str(i), fontsize=12)
    nn_x = [coords[i][0] for i in nn_route]
    nn_y = [coords[i][1] for i in nn_route]
    plt.plot(nn_x, nn_y, "b-", label=f"Nearest Neighbor (cost={nn_cost})")
    hk_x = [coords[i][0] for i in hk_route]
    hk_y = [coords[i][1] for i in hk_route]
    plt.plot(hk_x, hk_y, "r-", label=f"Held-Karp (cost={hk_cost})")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filenames = ["../data/matrix4.json", "../data/matrix5.json", "../data/matrix6.json"]


    for filename in filenames:
        try:
            cost_matrix = load_cost_matrix(filename)
            nn_route, nn_cost = tsp_nearest_neighbor(cost_matrix)
            hk_route, hk_cost = tsp_held_karp(cost_matrix)
            print(f"\n📁 {filename}")
            print("Nearest Neighbor:", nn_route, "Cost:", nn_cost)
            print("Held-Karp:", hk_route, "Cost:", hk_cost)
            coords = generate_random_coords(len(cost_matrix))
            plot_routes(coords, nn_route, nn_cost, hk_route, hk_cost, title=filename)
        except FileNotFoundError as e:
            print(f"❌ Lỗi: {e}")
