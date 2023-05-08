# Autonomous Car Simulator 1D Kalman Filter

This is a Python project that simulates the behavior of a Autonomous car using 1D Kalman filter by tracking its position and velocity.  The simulator generates real and estimated data, displays the results through animations, and provides visualizations of the car's movement, velocity estimates, and position estimate errors. 

<p align="center">
  <strong>1D Kalman filtering Constant Speed set to True and False </strong>
  <br>
  <img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Autonomous%20Car%201DKF/1DKF_Car.gif" alt="Simulator">
</p>

## Table of Contents

- [How It Works](#How-It-Works)
- [KalmanFilter Class](#kalmanfilter-class)
- [Simulator Components](#Simulator-Components)
- [Usage](#usage)
- [Running the Simulation](#Running-the-Simulation)


## How It Works

The script defines a `KalmanFilter` class that encapsulates the Kalman filter logic. It includes methods for prediction and measurement updates. The simulation uses a physics model to generate noisy position data, and the Kalman filter is used to estimate the object's position and velocity from this noisy data.

The script uses `matplotlib` to create an animation that visually represents the object's movement and the Kalman filter's estimates.

## KalmanFilter Class

The `KalmanFilter` class defines a Kalman filter with the following parameters:

- Initial state `x`
- Uncertainty matrix `P`
- State transition matrix `F`
- Measurement function `H`
- Measurement uncertainty `R`

The class provides methods for prediction and measurement update:

- `predict(t)`: Predicts the new state based on the state transition matrix.
- `measure_and_update(measurements, t)`: Updates the state estimate based on measurements.

## Simulator Components

The script includes the following components:

1. **KalmanFilter Class**: Defines the Kalman filter class with methods for prediction and measurement updates. This class handles state estimation and tracking.

2. **Simulation Loop**: Defines a physics simulation function to simulate car movement. Generates real data for velocity and time. Simulates the car's movement over time, adds noise to measurements, and performs Kalman filtering.

3. **Visualization**: The script uses `matplotlib` to create real-time visualizations of the car's movement, velocity estimates, and position estimate errors. The visualization includes a car icon, velocity estimate plot, and position estimate error plot.

4. **Performance Measurement**: The script measures and prints the computation time required for the simulation.

## Usage

To run the simulator, execute the script in a Python environment. The simulator provides options to control the simulation, such as constant speed and figure size. You can modify these options in the `options` dictionary at the beginning of the script.

```python
# Define options for the simulator
options = {}
options['FIG_SIZE'] = [8, 8]          # Figure size for visualization.
options['CONSTANT_SPEED'] = True      # Constant speed flag.
```

You can set `CONSTANT_SPEED` to `True` or `False` to simulate constant or variable object speed.


## Running the Simulation

Run the script, and a real-time animation will appear, showing the car's movement and estimation. You can customize the simulation by modifying the options and physics simulation functions as needed.
- You can save the animation as a GIF by uncommenting the relevant code at the end of the script.

Enjoy simulating the car's behavior by changing speed and other parameters!

