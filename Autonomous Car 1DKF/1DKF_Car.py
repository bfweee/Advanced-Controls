# Import necessary libraries
import numpy as np               
import matplotlib.pyplot as plt  
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec  
import time                       # Import the time module for time-related operations
# Define options for the simulator
options = {}                       # Create an empty dictionary called 'options'
options['FIG_SIZE'] = [8,8]        # Set the value of 'FIG_SIZE' in the 'options' dictionary to [8, 8]
options['CONSTANT_SPEED'] = True  # Set the value of 'CONSTANT_SPEED' in the 'options' dictionary to False

# Define a class named 'KalmanFilter'
class KalmanFilter:
    def __init__(self):
        # Initialize instance variables
        self.v = 0                       # Initialize 'v' to 0, representing velocity
        self.prev_time = 0               # Initialize 'prev_time' to 0 for tracking time
        # Initial State
        self.x = np.matrix([[0.],       # Create a 2x1 matrix 'x' representing the initial state
                            [0.]])
        # Uncertainty Matrix
        self.P = np.matrix([[1000., 0.],  # Create a 2x2 matrix 'P' representing uncertainty
                            [0., 1000.]])
        # Next State Function
        self.F = np.matrix([[1., 0.0],   # Create a 2x2 matrix 'F' representing the next state function
                            [0., 1.]])
        # Measurement Function
        self.H = np.matrix([[1., 0.]])   # Create a 1x2 matrix 'H' representing the measurement function
        # Measurement Uncertainty
        self.R = np.matrix([[0.01]])     # Create a 1x1 matrix 'R' representing measurement uncertainty
        # Identity Matrix
        self.I = np.matrix([[1., 0.],    # Create a 2x2 identity matrix 'I'
                            [0., 1.]])
    
    def predict(self, t):
        # Calculate the time difference (dt) between the current time (t) and the previous time (prev_time)
        dt = t - self.prev_time
        # Update the state transition matrix F with the time difference (dt)
        self.F[0, 1] = dt
        # Predict the new state (x) based on the state transition matrix (F)
        self.x = self.F * self.x
        # Predict the new covariance matrix (P) based on the state transition matrix (F)
        self.P = self.F * self.P * np.transpose(self.F)
        # Return the predicted x[0,0] value (typically representing position)
        return self.x[0, 0]
    def measure_and_update(self, measurements, t):
        # Calculate the time difference 'dt' between the current time 't' and the previous time 'prev_time'.
        dt = t - self.prev_time
        # Update the state transition matrix 'F' to incorporate 'dt'.
        self.F[0, 1] = dt
        # Create a measurement matrix 'Z' from the provided measurements.
        Z = np.matrix(measurements)
        # Calculate the measurement residual (y) by subtracting the expected measurement (H * x) from the actual measurement (Z)
        y = np.transpose(Z) - (self.H * self.x)
        # Calculate the measurement covariance (S) based on the measurement matrix (H), the covariance matrix (P), and the measurement noise covariance (R)
        S = self.H * self.P * np.transpose(self.H) + self.R
        # Calculate the Kalman Gain (K) using the covariance matrices
        K = self.P * np.transpose(self.H) * np.linalg.inv(S)
        # Update the state estimate (x) using the Kalman Gain (K) and the measurement residual (y)
        self.x = self.x + (K * y)
        # Update the covariance matrix (P) based on the Kalman Gain (K)
        self.P = (self.I - (K * self.H)) * self.P
        # Add a small value to the diagonal of the covariance matrix (P) for numerical stability
        #self.P[0, 0] += 0.1
        #self.P[1, 1] += 0.1
        # Update the velocity (v) and previous time (prev_time) based on the new state estimate (x) and current time (t)
        self.v = self.x[1, 0]
        self.prev_time = t

def sim_run(options, KalmanFilter):
    # Measure the start time for performance evaluation
    start = time.perf_counter()
    
    # Extract simulator options
    FIG_SIZE = options['FIG_SIZE']  # Figure size for visualization.
    CONSTANT_SPEED = options['CONSTANT_SPEED']  # Constant speed flag.

    # Initialize the Kalman Filter
    kalman_filter = KalmanFilter()

    # Physics simulation function
    def physics(t0, dt, state):
        if len(state) == 0:
            x0 = 0
        else:
            x0 = state[-1]

        if not CONSTANT_SPEED:
            if t0 > 60:
                x1 = 3 * dt + x0
                return x1
            if t0 > 40:
                x1 = 2 * dt + x0
                return x1
            if t0 > 20:
                x1 = 0.5 * dt + x0
                return x1
        x1 = 3 * dt + x0
        return x1
    
    # Define real data for velocity (y) and corresponding time (x)
    if CONSTANT_SPEED:
        v_real_data_y = [3, 3]
        v_real_data_x = [0, 100]
    else:
        v_real_data_y = [3, 3, 0.5, 0.5, 2, 2, 3, 3]
        v_real_data_x = [0, 19.99, 20, 39.99, 40, 59.99, 60, 100]

    state = []
    est_data_t = []
    v_est_data = []
    x_est_data = []
    t = np.linspace(0.0, 100, 1001)
    dt = 0.1
    
    # Simulation Loop
    for t0 in t:
        state += [physics(t0, dt, state)]
        if t0 % 1.0 == 0.0:
            est_data_t += [t0]
            # Measure car location with added noise
            state_with_noise = state[-1] + (np.random.rand(1)[0] - 0.5) * 0.3
            if t0 == 0.0:
                x_est_data += [0]
                v_est_data += [0]
                continue
            x_est_data += [kalman_filter.predict(t0) - state[-1]]
            kalman_filter.measure_and_update(state_with_noise, t0)
            v_est_data += [kalman_filter.v]

    # SIMULATOR DISPLAY SETUP
    # Create the main figure and gridspec
    fig = plt.figure(figsize=(FIG_SIZE[0], FIG_SIZE[1]))
    gs = gridspec.GridSpec(14, 8)

    # Elevator plot settings.
    ax = fig.add_subplot(gs[:, :3])
    plt.xlim(0, 8)
    ax.set_ylim([0, 31])
    plt.xticks([])

    plt.title('1D Kalman Filtering Const Speed = True')

    # Time display.
    time_text = ax.text(6, 0.5, '', fontsize=15, color='red')
    Info2 = ax.text(10, 7, '', fontsize=12)

    # Main plot info.
    car_l, car_r = ax.plot([], [], 'b-', [], [], 'b-')
    car_t, car_b = ax.plot([], [], 'b-', [], [], 'b-')

    # V Estimate plot.
    ax2 = fig.add_subplot(gs[0:4, 4:])
    v_est, = ax2.plot([], [], '-b')
    v_real, = ax2.plot(v_real_data_x, v_real_data_y, 'k--')
    plt.title('V Estimate')
    plt.xticks([])
    ax2.set_ylim([0, 4])
    ax2.set_yticks([0, 2, 4])

    # X Estimate plot.
    ax3 = fig.add_subplot(gs[5:9, 4:])
    x_est, = ax3.plot([], [], '-b')
    plt.title('X Estimate Error')
    plt.xticks([])
    ax3.set_ylim(-4, 4)
    ax3.set_yticks([-4, 0, 4])

    # Function to update plots for each frame
    def update_plot(num):
        t_loc = int(t[num])
        if state[num] > 18:
            ax.set_ylim([0 + state[num] - 18, 31 + state[num] - 18])
            time_text.set_position([6, state[num] - 18 + 0.5])
            Info2.set_position([10, state[num] - 18 + 7])

        # Car.
        car_l.set_data([3, 3], [state[num], state[num] + 6.8])
        car_r.set_data([5, 5], [state[num], state[num] + 6.8])
        car_t.set_data([3, 5], [state[num] + 6.8, state[num] + 6.8])
        car_b.set_data([3, 5], [state[num], state[num]])

        if int(t[num]) < 20:
            ax2.set_xlim([0, est_data_t[t_loc + 1]])
            ax3.set_xlim([0, est_data_t[t_loc + 1]])
        else:
            ax2.set_xlim([est_data_t[t_loc - 20], est_data_t[t_loc + 1]])
            ax3.set_xlim([est_data_t[t_loc - 20], est_data_t[t_loc + 1]])

        v_est.set_data(est_data_t[:t_loc], v_est_data[:t_loc])
        x_est.set_data(est_data_t[:t_loc], x_est_data[:t_loc])

        # Timer
        time_text.set_text(str(100 - t[num]))
        Info2.set_text(str('Constant Speed = True'))

        return car_l, car_r, car_t, car_b, time_text, Info2

    # Print the computation time
    print("Compute Time: ", round(time.perf_counter() - start, 3), "seconds.")
    # Animation settings
    car_ani = animation.FuncAnimation(fig, update_plot, frames=range(1, len(t)), interval=100, repeat=False, blit=False)
    # Show the animation
    plt.show()
    # Saving Animation
    #f = r"D:/animation.gif"
    #writergif = animation.PillowWriter(fps=8)
    #ar_ani.save(f, writer=writergif)

# Call the sim_run function with options and KalmanFilter
sim_run(options, KalmanFilter)