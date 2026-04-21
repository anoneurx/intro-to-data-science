# Monte Carlo Pi Estimation - Data Science Assignment

## 1. Abstract
This project implements a **Monte Carlo Simulation** to estimate the value of the mathematical constant **Pi ($\pi$)**. The simulation leverages random sampling and the geometric relationship between a circle and its bounding square to derive an approximation of $\pi$.

## 2. Mathematical Foundation
The simulation is based on the formula for the area of a circle:
$$A_{circle} = \pi r^2$$

By inscribing a circle within a square of side length $2r$, we can compare their areas:
- **Area of Square** = $(2r)^2 = 4r^2$
- **Area of Circle** = $\pi r^2$

The ratio of these areas is:
$$\frac{Area_{circle}}{Area_{square}} = \frac{\pi r^2}{4r^2} = \frac{\pi}{4}$$

By generating $N$ random points in the square and counting the number of points $M$ that fall inside the circle, we can estimate $\pi$ using:
$$\pi \approx 4 \times \left(\frac{M}{N}\right)$$

## 3. Implementation Details
The project consists of two primary components:
1. **Interactive Visualization (`index.html`)**: A web-based dashboard using HTML5 Canvas to visualize the "point-throwing" process in real-time.
2. **Analysis Script (`monte_carlo_pi.py`)**: A Python-based implementation for large-scale data testing and error analysis.

## 4. Key Findings
- **Sample Size Correlation**: As the number of iterations ($N$) increases, the error margin decreases, demonstrating the **Law of Large Numbers**.
- **Efficiency**: Statistical estimation provides an alternative to analytical calculation, useful in complex system modeling.

## 5. Usage
1. Open `index.html` to visualize the simulation.
2. Use the "Start" and "Stop" controls to observe the convergence of $\pi$.
3. Run `python3 monte_carlo_pi.py` to see the numerical error reduction over different sample sizes.
