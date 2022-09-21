# Fault Detection and Isolation on a State Space Plant
A fault represents a deviation from the normal behavior of a system due to unexpected events, and the occurrence of faults must be detected as early as possible to prevent serious consequences. For this purpose, Fault Detection and Diagnosis techniques (FDD) are used for the detection of faults (fault detection) and the localization of detected faults (fault isolation). Most contributions in FDD rely on the analytical redundancy principle, which involves using model information to generate additional signals compared with the plant measurements . Output estimation is a powerful tool for building mathematical models of systems.

## Contents
- [Introduction](#introduction)
- [Check for Missing Data, Measurement Errors, and Outliers](#check-for-missing-data-measurement-errors-and-outliers)
- [Residual Analysis and Correlation](#residual-analysis-and-correlation)
- [Comparing and Validating the System Responses](#comparing-and-validating-the-system-responses)
- [Parity Relation Scheme](#parity-relation-scheme)
- [Different Fault Scenarios and Graphs for Residual R1, R2](#different-fault-scenarios-and-graphs-for-residual-r1-r2)
- [Selection of Thresholds](#selection-of-thresholds)
- [Residuals Sensitivity](#residuals-sensitivity)
- [Residual Generation using Structured Residuals](#residual-generation-using-structured-residuals)
- [Threshold Selection](#threshold-selection)

## Introduction
In this project, we simulate a given discrete state-space plant (single-input and two-outputs model) in Matlab and Simulink. Simulations are performed on the plant for 15 seconds with a sampling rate of 40 Hz (0.025 sec). We introduce a unit step impulse and white noise to simulate a real environment, as there will always be some noise, disturbances, and errors in sensor measurements.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Real%20Plant%20with%20Model%201%2C2.PNG" width="90%"></p>
Using the output estimation function "oe" in MATLAB, we obtain mathematical models from the real plant, resulting in two first-order mathematical models of our system. We move from these difference equations to discrete transfer functions. The "oe" function estimates transfer function Model 1 and Model 2 with an order of 1. The estimated models are stored as m1 and m2. Once we have our estimated mathematical model of the system and its parameters, we can use these models to predict the output and behavior of the system for new input signals.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/StepResponseIO.PNG" width="90%"></p>

## Check for Missing Data, Measurement Errors, and Outliers

In order to perform FDD effectively, it is essential to check for missing data, measurement errors, disturbances, and outliers in the measured data.

Missing data can lead to incorrect conclusions about the system's behavior. To account for its absence in the FDD algorithm, we use the "misdata" function in Matlab to reconstruct the input and output time-domain data sets by reasonable estimates.

Outliers are data points significantly different from the expected system behavior. Analyzing the data and identifying patterns/trends inconsistent with the expected behavior is crucial. This can be caused by factors like measurement errors, resulting in incorrect and noisy data. It's important to correct errors before performing FDD.

By examining the residual correlational structures (using the "resid" function in Matlab) and identifying anomalies and outliers, we can develop robust and accurate FDD algorithms that effectively identify faults and abnormal conditions in the system.

## Residual Analysis and Correlation

The main component of any FDD system is the residual generator, which produces residual signals grouped in a vector 'R' by processing the available measurements 'y' and the known values of control inputs 'u'.

Residual analysis is a vital step in developing and validating the models. Using the "resid" function in Matlab, we compute the 1-step-ahead prediction errors (residuals) for an identified model. We plot the AutoCorr (shows the correlation of residuals with themselves) and XCorr (shows the correlation of residuals with input and output data over time) to assess the quality of residual correlation structure and the adequacy of the models. The residuals must have a small magnitude, zero mean, and low autocorrelation, except at zero-time lag .
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Residuecorre.PNG" width="80%"></p>
These plots are powerful tools for diagnosing model fit and identifying potential areas for improvement. Upon examination, these plots do not indicate a mis-specified model, missing variables, or unaccounted disturbances. Additionally, the cross-correlation between residuals of Model 1 and Model 2 and the inputs lies within the 99% confidence band for all lags.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Modelwithnoise.PNG" width="90%"></p>

## Comparing and Validating the System Responses

To compare the simulated output from the two models with the actual output, we use the 'compare' function. The comparison plot indicates that both Model m1 and Model m2 are a good fit and practically identical to the real plant. Hence, simulations of our model are considered valid.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/SysResponsevalidation.PNG" width="60%"></p>

## Parity Relation Scheme

Model-based fault detection and isolation (FDI) using parity relations is a commonly used approach for detecting and isolating faults in dynamic systems. Parity relations are mathematical equations that relate the system inputs, outputs, and states to each other. In this approach, a mathematical model of the system is developed, and parity relations are derived based on the model. The basic idea is to use the redundancy in the system by comparing the outputs predicted by Model 1 and Model 2 with the actual outputs measured by the sensors. If there is a discrepancy between the predicted and measured outputs, it is an indication of a fault.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Real%20Plant%20with%20Model%201%2C2.PNG" width="90%"></p>
The role of the residual signals is to indicate the presence or absence of faults, and therefore the residual r must be equal (or close) to zero in the absence of faults and significantly different from zero after a fault occurs.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/FaultdiffMag.PNG" width="90%"></p>
Now, we apply different magnitudes of abrupt faults both at inputs and outputs and generate residuals to check the overall consistency of mathematical equations of the system with measurements.

### Selection of Thresholds

- Visualize the variations of residuals over time.
- Compute statistical measures in Matlab: Mean, Standard Deviation (std), maximum (max), and minimum (min) values of residuals. This helps us determine the behavior of the system.
- Based on statistical measures, we measure the noise level as the standard deviation of residuals and multiply by +3*(std) for upper threshold limit and -3*(std) for lower thresholds. Threshold_R1 = 3*std(R1) and Threshold_R2 = 3*std(R2).
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Thresholdselec.PNG" width="60%"></p>

### Residuals Sensitivity

Residuals are highly sensitive even at small magnitudes of input faults (Fu=0.3,1).
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Resensi.PNG" width="80%"></p>



## Residual Generation using Structured Residuals

Structured residuals involve identifying the faults of interest and designing the specific residuals to be sensitive to those specific faults. These residuals are designed to have specific properties that make them sensitive to specific types of faults and insensitive to others. The aim is to generate residuals that are highly sensitive to faults of interest while being robust to noise and disturbances.

Structured residuals are designed to be orthogonal to each other. This property allows each residual to detect a specific fault without interference from other faults.

Symmetry: Structured residuals are designed to be symmetric, meaning they are equally sensitive to faults in either direction. This property helps to detect faults that produce symmetrical effects in the system.
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Structured%20Residuals.PNG" width="90%"></p>
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Residdifffau.PNG" width="90%"></p>
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Residdifffau2.PNG" width="90%"></p>
<p align="center"><img src="https://github.com/Rohit-Gupta2/Advanced-Controls/blob/Master/Fault%20Detection%20and%20Isolation/Figures/Residdifffau3.PNG" width="90%"></p>

### Threshold Selection

Thresholds are wider than usual due to high noise in the system. If we choose standard deviation, we have lower limits of R1, R2, R3. It is suggested to add a low-pass filter to the system to reduce noise, which might make fault detection easier for the thresholds. It is also suggested to use different fault detection methods for task 3, such as adaptive thresholds or statistical methods like the interquartile range (IQR).

The simulation is completed without any faults being present in the system, despite having faults at the output.

