# Car Parking Using Model Predictive Controller 
Parking a vehicle in a confined space, such as a parking lot, is a common task for autonomous vehicles. This project demonstrates how a Model Predictive Controller (MPC) can be employed to control a car's movements during parking. The MPC is used to control the vehicle's acceleration and steering inputs to park it accurately in a reference parking space.

## Contents

- [Overview](#overview)
- [MPC Controller](#mpc-controller)
    - [Prediction Horizon and Time Step](#Prediction-Horizon-and-Time-Step)
    - [Plant Model](#Plant-Model)
    - [Vehicle State Update](#Vehicle-State-Update)
    - [Cost Function](#Cost-Function)
- [Visualization](#Visualization)
- [Running the Simulation](#running-the-simulation)

<p align="center">
  <strong>Car Parking Model Predictive Control</strong>
  <br>
  <img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/MPC_CarParking/MPC_CP_Sim.gif" alt="Simulator">
</p>

## Overview
This project simulates an Autonomous car parking scenario using a Model Predictive Controller (MPC) implemented in Python.
The MPC predicts the vehicle's future states, such as position and orientation, and calculates control inputs (acceleration and steering) to achieve precise parking.
- This script provides a comprehensive example of how MPC can be applied to real-world control problems, such as autonomous parking.
- The vehicle dynamics are simulated with high fidelity using the bicycle model, including damping effects on velocity.
- The cost function is carefully designed to balance various control objectives, including accurate positioning, orientation, and smooth control inputs.
- The script demonstrates how a predictive control approach can handle complex control scenarios, such as parking, where precise maneuvering is required.

## MPC Controller

The MPC controller is defined in the `ModelPredictiveControl` class and includes the following key components:

### Prediction Horizon and Time Step
- The heart of this project is the MPC controller, encapsulated within the ModelPredictiveControl class. It incorporates several technical elements:
Prediction Horizon: The MPC predicts the vehicle's future states over a specified prediction horizon. It uses a prediction horizon of 30 steps into the future (`self.horizon`) to plan the vehicle's trajectory. 

- Time Step (dt): The controller divides the prediction horizon into discrete time steps, each with a duration of dt which is set to 0.2 seconds (`self.dt`).

**Reference Points:** Two reference points, reference1 and reference2, define the desired final state of the vehicle. They include position (x, y) and orientation (psi) information.

### Plant Model
- The plant_model function represents the dynamics of the vehicle using a bicycle model. It computes the next state of the vehicle based on control inputs (acceleration and steering). Key aspects of the model include:
- State variables: x, y, psi (yaw angle), and velocity (v).
  - `x_t`: x-coordinate of the vehicle's position.
  - `y_t`: y-coordinate of the vehicle's position.
  - `psi_t`: Heading angle (yaw) of the vehicle.
  - `v_t`: Velocity of the vehicle.
- **Control inputs:** Acceleration (a_t) and steering angle (beta).
- **Damping effect:** The model includes a damping term to simulate velocity damping.

### Vehicle State Update
- The plant model predicts the next state of the vehicle using the control inputs and updates the state variables accordingly.
- The model also simulates the vehicle's velocity, considering acceleration and a simple damping term.

### Cost Function
- Cost Function: The `cost_function` computes the cost associated with a given control input sequence. It penalizes deviations from the reference points, orientation errors, and rapid changes in acceleration and steering.
- The MPC controller minimizes a cost function to find optimal control inputs.
- The cost function includes the following components:
  - **Position Costs**: Penalize deviations from reference positions (x and y). We can choose between Linear or squared Position Cost.
  - **Orientation Cost**: Penalize deviations from the reference heading angle, orientation errors (yaw angle psi).
  - **Acceleration Cost**: Penalize rapid or large changes in acceleration.
  - **Steering Input Cost**: Minimize abrupt changes in steering.
## Visualization
- Matplotlib library is used to visualize the car parking scenarios. The visualization includes:
    - Real-Time Visualization: The script dynamically updates and displays the vehicle's movement and parking progress in real-time.
    - Trajectory Tracking: The visualization shows how well the MPC controller tracks the desired reference points.
    - Control Effort: Visual representation of the control inputs (acceleration and steering) applied by the MPC.
## Running the Simulation

Once you have configured the options, run the script. The simulation will generate a visualization of the car parking scenario, and you can observe how the MPC controller guides the vehicle to its parking destination.

This project serves as an educational resource for understanding the technical intricacies of Model Predictive Control, vehicle dynamics modeling, and control optimization.
Explore, experiment, and gain insights into advanced autonomous vehicle control with Model Predictive Control!
Feel free to reach out for further technical details or exploration of specific aspects of the project.