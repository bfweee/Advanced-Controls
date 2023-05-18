import numpy as np
from sim.MPCSim import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]  # Setting the figure size for visualization.
options['OBSTACLES'] = False  # Disabling obstacles in the simulation.

# Define the Model Predictive Control (MPC) class.
class ModelPredictiveControl:
    def __init__(self):
        # MPC Control parameters
        self.horizon = 30  # Prediction horizon ( how many steps into the future to plan)
        self.dt = 0.2      # Time step duration for each planning step.

        # Reference or set points the controller will aim to achieve.
        self.reference1 = [10, 10, 0]        # First reference: x, y, and heading angle [x, y, psi]
        self.reference2 = [10, 2,3.14/2]    # Reference for state [x, y, psi]

    # This function models the vehicle's dynamics and updates its state.
    def plant_model(self, prev_state, dt, pedal, steering):
        # Predict the next state of the vehicle using a bicycle model.
        # Extracting the previous state variables.
        x_t = prev_state[0]  # x-coordinate.
        y_t = prev_state[1]  # y-coordinate.
        psi_t = prev_state[2]  # Heading angle (yaw).
        v_t = prev_state[3]  # Velocity.

        # Extracting control inputs.
        beta = steering  # Steering angle.
        a_t = pedal  # Acceleration.
        
        # Computing the next state. Update velocity considering acceleration and a simple damping term
        v_t_1 = v_t + a_t * dt - v_t/25.0

        # Compute state derivatives
        x_dot = v_t * np.cos(psi_t)  # x-coordinate change rate.
        y_dot = v_t * np.sin(psi_t)  # y-coordinate change rate.
        psi_dot = v_t * np.tan(beta)/2.5  # Yaw rate.

        # Update state variables
        x_t += x_dot * dt  # Updating x-coordinate.
        y_t += y_dot * dt  # Updating y-coordinate.
        psi_t += psi_dot*dt  # Updating heading angle.
        return [x_t, y_t, psi_t, v_t_1]  # Returning the updated state.
    
    # This function computes the cost associated with a given control input sequence.
    def cost_function(self, u, *args):
        # Cost function to be minimized during control optimization.
        state = args[0]  # Current state of the vehicle.
        ref = args[1]    # Reference state or set point.
        cost = 0.0  # Initialize the cost.
        for k in range(0, self.horizon):
            # Update the state using the plant model with control inputs.  Simulate the vehicle's dynamics using the control inputs.
            state = self.plant_model(state, self.dt, u[k*2], u[k*2+1])
            
            # Linear Position Costs: Penalize deviation from the reference position. (minimize the difference from reference).
            #cost += abs(ref[0] - state[0]) # x-coordinate error.
            #cost += abs(ref[1] - state[1]) # y-coordinate error

            # Squared Position Costs:
            cost += abs(ref[0] - state[0])**2  # x-coordinate error.
            cost += abs(ref[1] - state[1])**2  # y-coordinate error

            # Angle Cost: Penalize deviation from the reference heading angle.
            cost += abs(ref[2] - state[2])**2

            # Acceleration Cost: Penalize rapid or large changes in acceleration.
            #cost += (state[3] - v_start)**2*100  # Weighted by a factor of 100.

            # Steering Input cost (minimize abrupt changes in steering).
            #cost += u[k * 2 + 1]**2*self.dt
        return cost
# Run the simulation using the specified options and MPC controller.
sim_run(options, ModelPredictiveControl)
