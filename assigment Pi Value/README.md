# Assignment: Estimating Pi using Monte Carlo Simulation

**🚀 [Live Demo](https://anoneurx.github.io/intro-to-data-science/assigment%20Pi%20Value/)**

## Project Overview
This project demonstrates how to approximate the value of **Pi ($\pi$)** using a statistical method known as the **Monte Carlo Simulation**. 

The application is designed with a **professional academic theme** suitable for classroom presentations, featuring a deep navy blue interface and real-time visualization.

## The Formula
The area of a circle is $A = \pi r^2$.
The area of a square with side $2r$ is $A = (2r)^2 = 4r^2$.

The ratio between them is:
$$\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi r^2}{4 r^2} = \frac{\pi}{4}$$

Therefore, we can calculate Pi as:
$$\pi \approx 4 \times \frac{\text{Dots Inside Circle}}{\text{Total Dots}}$$

## How the Code Works (For Presentation)
1. **HTML Layout**: A simple, clean interface with a white background and professional black text.
2. **The Canvas**: Represents a square area. We draw a circle inside this square.
3. **Random Sampling**: The JavaScript generates random coordinates $(x, y)$.
4. **Distance Check**: For every point, we check if it is within the circle using the distance formula:
   - If $(x - center)^2 + (y - center)^2 \leq radius^2$, the point is **inside**.
5. **Iteration**: As we add more points, the estimation becomes more accurate.

## How to Run
1. Open the `index.html` file in any web browser.
2. Click **"Start / Stop"** to begin the simulation.
3. Watch the value of Pi update in real-time as the number of dots increases.

## Conclusion
This assignment illustrates the **Law of Large Numbers**. With more data points (dots), our statistical estimate gets closer and closer to the actual value of $\pi \approx 3.14159$.
