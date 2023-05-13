import numpy as np
from sim.MPCSim import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]  # Set the figure size for visualization.
options['OBSTACLES'] = True   # Flag indicating whether obstacles are present.

class ModelPredictiveControl:
    def __init__(self):
        # Model predictive control parameters.
        self.horizon = 10  # Prediction horizon.
        self.dt = 0.2  # Time step for the simulation.

        # Reference or set point the controller will achieve.
        self.reference1 = [10, 0.1, 0]  # Reference state [x, y, psi].
        self.reference2 = None  # Optional secondary reference.

        # Coordinates of an obstacle Position in the simulation.
        self.x_obs = 5
        self.y_obs = 0

    # Model of the vehicle dynamics.
    def plant_model(self, prev_state, dt, pedal, steering):
        x_t = prev_state[0]
        y_t = prev_state[1]
        psi_t = prev_state[2]
        v_t = prev_state[3]

        beta = steering  # Steering angle.
        a_t = pedal     # Acceleration.
        
        # Compute the rates of change for various state variables.
        x_dot = v_t*np.cos(psi_t)
        y_dot = v_t*np.sin(psi_t)
        psi_dot = v_t*np.tan(beta)/2.5
        v_dot = a_t

        # Update state variables based on dynamics.
        x_t += x_dot*dt
        y_t += y_dot*dt
        psi_t += psi_dot*dt
        v_t += v_dot*dt - v_t/25.0   # Simple friction model.

        return [x_t, y_t, psi_t, v_t]

    # Cost function to be minimized by the MPC controller.
    def cost_function(self, u, *args):
        state = args[0]  # Current state of the vehicle.
        ref = args[1]    # Reference state to track.
        cost = 0.0

        # Iterate over the prediction horizon.
        for k in range(0, self.horizon):
            state = self.plant_model(state, self.dt, u[k*2], u[k*2+1])

            # Add position and angle error to the cost.
            # Tracking costs for position and orientation.
            cost += (ref[0] - state[0])**2
            cost += (ref[1] - state[1])**2
            cost += (ref[2] - state[2])**2

            # Add obstacle avoidance cost based on current position.
            # Obstacle avoidance cost based on distance to the obstacle.
            cost += self.obstacle_cost(state[0], state[1])
        return cost

    # Cost function for obstacle avoidance.
    def obstacle_cost(self, x, y):
        # Calculate the distance between the vehicle and the obstacle.
        # Calculate the cost based on the distance to the obstacle.
        distance = (x - self.x_obs)**2 + (y - self.y_obs)**2
        distance = np.sqrt(distance)
        if (distance > 2):
            return 15
        else:
            return 1/distance*25

# Run the simulation with the specified options and MPC controller.
sim_run(options, ModelPredictiveControl)
