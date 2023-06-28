# Obstacle Avoidance using Model Predictive Controller

Obstacle avoidance is a critical aspect of autonomous vehicle control. This project showcases a robust obstacle avoidance system implemented with a Model Predictive Controller (MPC). The MPC enables efficient navigation while ensuring the vehicle adheres to dynamic constraints and avoids obstacles. The MPC controller predicts and computes control inputs that minimize a cost function while satisfying vehicle dynamics and obstacle avoidance constraints.
## Table of Contents
<picture> <img align="right" src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/MPC_ObstacleAvoidance/MPC_obstacleAv_Sim.gif" alt="Simulator" width="400" width = 280px></picture>
<br><br>
- [Overview](#overview)
- [MPC Controller](#mpc-controller)
    - [Prediction Horizon and Time Step](#Prediction-Horizon-and-Time-Step)
    - [Plant Model](#Plant-Model)
    - [Vehicle State Update](#Vehicle-State-Update)
    - [Cost Function](#Cost-Function)
    - [Obstacle Avoidance](#Obstacle-Avoidance)
- [Visualization](#Visualization)
- [Usage](#usage)
- [Running the Simulation](#running-the-simulation)
## Overview
This project simulates obstacle avoidance using a Model Predictive Controller (MPC) implemented in Python. The MPC predicts the vehicle's future states, including position and orientation, and calculates control inputs (acceleration and steering) to achieve precise maneuvering. Key project highlights include:
- Real-world MPC application: Demonstrates how MPC can be applied to control problems, such as obstacle avoidance.
- High-fidelity vehicle dynamics: Utilizes a bicycle model that accounts for damping effects on velocity for accurate simulation.
- Balanced cost function: Carefully designed cost function considers multiple control objectives, including precise positioning, orientation, and smooth control inputs.
- Complex control scenarios: Illustrates how predictive control handles intricate scenarios like obstacle avoidance, requiring precise and adaptive maneuvering.

## MPC Controller

The MPC controller is defined in the `ModelPredictiveControl` class and includes the following key components:

### Prediction Horizon and Time Step
- The heart of this project is the MPC controller, encapsulated within the ModelPredictiveControl class. It incorporates several Functions:
Prediction Horizon: The MPC predicts the vehicle's future states over a specified prediction horizon. It uses a prediction horizon of 30 steps into the future (`self.horizon`) to plan the vehicle's trajectory. 

- Time Step (dt): The controller divides the prediction horizon into discrete time steps, each with a duration of dt which is set to 0.2 seconds (`self.dt`).

**Reference Points:** Two reference points, reference1 and reference2, define the desired final state of the vehicle. They include position (x, y) and orientation (psi) information.
### Plant Model

- The `plant_model` function represents the vehicle's dynamics using a bicycle model. It predicts the next state of the vehicle based on control inputs (acceleration and steering). Key aspects of the model include:
- State variables: x, y, psi (yaw angle), and velocity (v).
  - `x_t`: x-coordinate of the vehicle's position.
  - `y_t`: y-coordinate of the vehicle's position.
  - `psi_t`: Heading angle (yaw) of the vehicle.
  - `v_t`: Velocity of the vehicle.
- **Control inputs:** Acceleration (a_t) and steering angle (beta).
- **Damping effect:** The model incorporates a damping term to simulate velocity damping.

### Vehicle Dynamics

- The vehicle dynamics are modeled using the `plant_model` method.
- The method computes the rates of change for state variables such as position (`x`, `y`), orientation (`psi`), and velocity (`v`).
- Control inputs, including steering angle (`beta`) and acceleration (`a`), influence the state variables.
- A simple friction model is applied to simulate the vehicle's behavior.
### Cost Function
- The MPC controller minimizes a cost function to determine optimal control inputs, as defined by the `cost_function` method.
- Cost Function: The `cost_function` calculates the cost associated with a given sequence of control inputs. It penalizes deviations from reference positions, orientation errors, and sudden changes in acceleration and steering.
- The cost function includes the following components:
  - **Position Costs**: Penalizes deviations from reference positions (x and y). You can choose between linear or squared position costs.
  - **Orientation Cost**: Penalizes deviations from the reference heading angle, addressing orientation errors (yaw angle psi).
  - **Acceleration Cost**: Penalizes rapid or large changes in acceleration.
  - **Steering Input Cost**: Penalize rapid or large changes in acceleration. Aims to minimize abrupt steering changes.
  - **Obstacle Cost**:Minimize vehicle proximity to obstacles Encourages the controller to steer the vehicle away from obstacles, considering vehicle proximity.

### Obstacle Avoidance
- The obstacle avoidance cost is calculated based on the distance between the vehicle and an obstacle (`self.x_obs`, `self.y_obs`).
- The cost increases as the vehicle approaches the obstacle.
- The cost function encourages the controller to steer the vehicle away from obstacles.
## Visualization
- Matplotlib library is used to visualize the car parking scenarios. The visualization includes:
    - Real-Time Visualization: The script dynamically updates and displays the vehicle's movement and parking progress in real-time.
    - Trajectory Tracking: The visualization shows how well the MPC controller tracks the desired reference points.
    - Control Effort: Visual representation of the control inputs (acceleration and steering) applied by the MPC.
## Usage

To use this MPC-based obstacle avoidance system, follow these steps:

1. Set the simulator options in the `options` dictionary at the beginning of the script. You can specify the figure size for visualization and enable/disable obstacles:

   ```python
   options = {}
   options['FIG_SIZE'] = [8, 8]   # Figure size for visualization.
   options['OBSTACLES'] = True   # Flag indicating whether obstacles are present.
   ```

2. Customize the MPC controller by modifying its parameters, such as the prediction horizon, time step, and reference trajectory (`self.reference1` and `self.reference2`).

3. Implement the plant model in the `plant_model` method to define the vehicle's dynamics.

4. Define the cost function in the `cost_function` method to specify the controller's objectives.


## Running the Simulation

Run the script to execute the simulation with the specified options and MPC controller. The simulation will display the vehicle's trajectory and obstacle avoidance behavior in real-time.

The MPC controller successfully guides the vehicle to track the reference trajectory while avoiding obstacles. You can observe the vehicle's dynamic behavior and its ability to adjust its path to avoid collisions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Enjoy exploring the world of obstacle avoidance with Model Predictive Control!