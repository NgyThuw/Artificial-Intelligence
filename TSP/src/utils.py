import json
import os

def load_cost_matrix(filename):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    full_path = os.path.join(base_dir, filename)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Không tìm thấy file: {full_path}")
    with open(full_path, "r") as f:
        data = json.load(f)
    return data["cost_matrix"]
