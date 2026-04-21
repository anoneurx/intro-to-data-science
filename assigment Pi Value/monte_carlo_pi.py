import random
import math

def estimate_pi(num_points):
    """
    Estimates Pi by generating random points in a square 
    and checking if they fall inside a circle.
    """
    inside_circle = 0
    
    for _ in range(num_points):
        # Generate random x and y coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point is inside the unit circle (x^2 + y^2 <= 1)
        if (x**2 + y**2) <= 1:
            inside_circle += 1
            
    # Calculate Pi using the ratio: (inside / total) = Pi / 4
    return 4 * (inside_circle / num_points)

# Main execution
if __name__ == "__main__":
    # Test with different numbers of dots
    test_counts = [1000, 10000, 100000]
    
    print("Monte Carlo Pi Simulation Results:")
    print("-" * 40)
    
    for count in test_counts:
        calculated_pi = estimate_pi(count)
        error = abs(calculated_pi - math.pi)
        
        print(f"Dots: {count:<8} | Pi Estimate: {calculated_pi:<10.5f} | Error: {error:.5f}")
