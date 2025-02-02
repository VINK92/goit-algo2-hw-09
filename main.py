import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        neighbor = [max(min(x + random.uniform(-0.1, 0.1), b[1]), b[0]) for x, b in zip(current_solution, bounds)]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value
        
        if abs(neighbor_value - current_value) < epsilon:
            break
    
    return current_solution, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)
    
    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)
        
        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value
        
        if abs(candidate_value - best_value) < epsilon:
            break
    
    return best_solution, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break
        
        neighbor = [max(min(x + random.uniform(-0.5, 0.5), b[1]), b[0]) for x, b in zip(current_solution, bounds)]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value or random.random() < math.exp((current_value - neighbor_value) / temp):
            current_solution, current_value = neighbor, neighbor_value
    
    return current_solution, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]
    
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)
    
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)
    
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
