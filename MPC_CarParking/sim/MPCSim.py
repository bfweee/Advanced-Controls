# Importing necessary libraries.
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation  # Animation support for Matplotlib.
import matplotlib.gridspec as gridspec  # Grid specification for subplots.
import matplotlib.patches as mpatches  # Drawing patches (shapes) in plots.
from scipy.optimize import minimize  # Optimization function from SciPy.
import time  # Time measurement and delay functions.

# Function for running the simulation with provided options and MPC (Model Predictive Control) class.
def sim_run(options, MPC):
    start = time.process_time()  # Measure the starting time of the simulation.

    # Simulator Options
    FIG_SIZE = options['FIG_SIZE']  # Figure size for the simulation window [Width, Height].
    OBSTACLES = options['OBSTACLES']  # Flag to enable/disable obstacles in the simulation.

    mpc = MPC()  # Create an instance of the Model Predictive Control class.

    num_inputs = 2  # Number of control inputs (throttle and steering).
    u = np.zeros(mpc.horizon * num_inputs)  # Initialize control input sequence.
    bounds = []  # Bounds for control inputs.

    # Set bounds for inputs for bounded optimization.
    for i in range(mpc.horizon):
        bounds += [[-1, 1]]      # Throttle input bounds.
        bounds += [[-0.8, 0.8]]  # Steering input bounds.
    # Define reference states for the controller.
    ref_1 = mpc.reference1  # First reference state to track.
    ref_2 = mpc.reference2  # Second reference state to track.
    ref = ref_1  # Initialize the reference to the first reference state.
    # Initialize state and control history arrays for simulation.
    state_i = np.array([[0, 0, 0, 0]])  # Initialize the state history with the initial state.
    u_i = np.array([[0, 0]])  # Initialize the control input history.
    sim_total = 250  # Total number of simulation steps.
    predict_info = [state_i]  # List to store predicted state trajectories.

    # Simulation loop.
    for i in range(1, sim_total + 1):
        # Remove the oldest control inputs and append the most recent one for optimization. (for continuity).
        u = np.delete(u, 0)
        u = np.delete(u, 0)
        u = np.append(u, u[-2])
        u = np.append(u, u[-2])
        start_time = time.time()  # Measure the starting time for the current step.

        # Non-linear optimization to find optimal control inputs.
        u_solution = minimize(mpc.cost_function, u, (state_i[-1], ref),
                              method='SLSQP',
                              bounds=bounds,
                              tol=1e-5)
        print('Step ' + str(i) + ' of ' + str(sim_total) + '   Time ' + str(round(time.time() - start_time, 5)))
        
        # Update control inputs and predict the next state.
        u = u_solution.x  # Update control inputs based on optimization result.
        # Simulate the vehicle dynamics with the updated control inputs.
        y = mpc.plant_model(state_i[-1], mpc.dt, u[0], u[1])

        # Switch the reference to the second reference state after a certain step.
        if (i > 75 and ref_2 is not None):
            # If we're past a certain point and have a second reference, switch to it.
            ref = ref_2

        predicted_state = np.array([y])  # Initialize the predicted state trajectory with the current state.

        # Predict future states based on the optimal control inputs.
        for j in range(1, mpc.horizon):
            predicted = mpc.plant_model(predicted_state[-1], mpc.dt, u[2 * j], u[2 * j + 1])
            predicted_state = np.append(predicted_state, np.array([predicted]), axis=0)
         # Store simulation history.
        predict_info += [predicted_state]  # Store the predicted state trajectory.
        state_i = np.append(state_i, np.array([y]), axis=0)  # Append the current state to the state history.
        u_i = np.append(u_i, np.array([(u[0], u[1])]), axis=0)  # Append the current control inputs to the history.

    # SIMULATOR DISPLAY
    fig = plt.figure(figsize=(FIG_SIZE[0], FIG_SIZE[1]))
    gs = gridspec.GridSpec(8, 8)  # Grid specification for subplot arrangement.

    # Elevator plot settings.
    ax = fig.add_subplot(gs[:8, :8])

    plt.xlim(-3, 17)  # Set x-axis limits for the plot.
    ax.set_ylim([-3, 17])  # Set y-axis limits for the plot.
    plt.xticks(np.arange(0, 11, step=2))  # Set x-axis tick locations.
    plt.yticks(np.arange(0, 11, step=2))  # Set y-axis tick locations.
    plt.title('Model Predictive Control for Autonomous Car Control')  # Set the plot title.

    # Time display.
    time_text = ax.text(6, 0.5, '', fontsize=15)  # Text for displaying simulation time.

    # Main plot info.
    car_width = 1.0  # Width of the car for visualization.
    patch_car = mpatches.Rectangle((0, 0), car_width, 2.5, fc='b', fill=True)  # Car visualization.
    patch_goal = mpatches.Rectangle((0, 0), car_width, 2.5, fc='b',
                                    ls='dashdot', fill=False)  # Goal visualization.

    ax.add_patch(patch_car)  # Add car visualization to the plot.
    ax.add_patch(patch_goal)  # Add goal visualization to the plot.
    predict, = ax.plot([], [], 'r--', linewidth=1)  # Line for displaying predicted trajectory.

    # Car steering and throttle position visualization.
    telem = [3, 14]  # Position for steering wheel and control input visualizations.
    patch_wheel = mpatches.Circle((telem[0] - 3, telem[1]), 2.2)  # Steering wheel visualization.
    ax.add_patch(patch_wheel)  # Add steering wheel to the plot.
    wheel_1, = ax.plot([], [], 'k', linewidth=3)  # Lines representing the steering wheel.
    wheel_2, = ax.plot([], [], 'k', linewidth=3)
    wheel_3, = ax.plot([], [], 'k', linewidth=3)
    throttle_outline, = ax.plot([telem[0], telem[0]], [telem[1] - 2, telem[1] + 2],
                                'b', linewidth=20, alpha=0.4)  # Throttle visualization.
    throttle, = ax.plot([], [], 'k', linewidth=20)  # Throttle position indicator.
    brake_outline, = ax.plot([telem[0] + 3, telem[0] + 3], [telem[1] - 2, telem[1] + 2],
                            'b', linewidth=20, alpha=0.2)  # Brake visualization.
    brake, = ax.plot([], [], 'k', linewidth=20)  # Brake position indicator.
    throttle_text = ax.text(telem[0], telem[1] - 3, 'Forward', fontsize=15,
                            horizontalalignment='center')  # Text indicating throttle direction.
    brake_text = ax.text(telem[0] + 3, telem[1] - 3, 'Reverse', fontsize=15,
                        horizontalalignment='center')  # Text indicating brake direction.

    # Obstacles (if enabled).
    if OBSTACLES:
        patch_obs = mpatches.Circle((mpc.x_obs, mpc.y_obs), 0.5,fc='red')  # Visualization of an obstacle.
        ax.add_patch(patch_obs)  # Add obstacle to the plot.

    # Function to shift the car visualization from the center of the car to the rear left corner.
    def car_patch_pos(x, y, psi):
        x_new = x - np.sin(psi) * (car_width / 2)
        y_new = y + np.cos(psi) * (car_width / 2)
        return [x_new, y_new]

    # Function to update the steering wheel visualization.
    def steering_wheel(wheel_angle):
        wheel_1.set_data([telem[0] - 3, telem[0] - 3 + np.cos(wheel_angle) * 2],
                         [telem[1], telem[1] + np.sin(wheel_angle) * 2])
        wheel_2.set_data([telem[0] - 3, telem[0] - 3 - np.cos(wheel_angle) * 2],
                         [telem[1], telem[1] - np.sin(wheel_angle) * 2])
        wheel_3.set_data([telem[0] - 3, telem[0] - 3 + np.sin(wheel_angle) * 2],
                         [telem[1], telem[1] - np.cos(wheel_angle) * 2])

    # Function to update the plot for each time frame.
    def update_plot(num):
        # Update car position and orientation.
        patch_car.set_xy(car_patch_pos(state_i[num, 0], state_i[num, 1], state_i[num, 2]))
        patch_car.angle = np.rad2deg(state_i[num, 2]) - 90
        
        # Update car wheels (steering).
        np.rad2deg(state_i[num, 2])
        # Update steering wheel and control input indicators.
        steering_wheel(u_i[num, 1] * 2)
        # Update throttle and brake positions.
        throttle.set_data([telem[0], telem[0]],
                          [telem[1] - 2, telem[1] - 2 + max(0, u_i[num, 0] / 5 * 4)])
        brake.set_data([telem[0] + 3, telem[0] + 3],
                       [telem[1] - 2, telem[1] - 2 + max(0, -u_i[num, 0] / 5 * 4)])

        # Update the goal position.
        if (num <= 75 or ref_2 is None):
            patch_goal.set_xy(car_patch_pos(ref_1[0], ref_1[1], ref_1[2]))
            patch_goal.angle = np.rad2deg(ref_1[2]) - 90
        else:
            patch_goal.set_xy(car_patch_pos(ref_2[0], ref_2[1], ref_2[2]))
            patch_goal.angle = np.rad2deg(ref_2[2]) - 90
        # Update the predicted trajectory.
        predict.set_data(predict_info[num][:, 0], predict_info[num][:, 1])
        return patch_car, time_text

    print("Compute Time: ", round(time.process_time() - start, 3), "seconds.")

    # Animation setup.
    car_ani = animation.FuncAnimation(fig, update_plot, frames=range(1, len(state_i)), interval=100, repeat=True, blit=False)
    # Uncomment the following line to save the animation as an MP4 file.
    # car_ani.save('mpc-video.mp4')
    # Saving Animation
    #f = r"D:/animation.gif"
    #writergif = animation.PillowWriter(fps=8)
    #car_ani.save(f, writer=writergif)
    plt.show()  # Show the simulation plot.
