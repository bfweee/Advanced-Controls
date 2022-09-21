clear all
close all
sim Task1_With_Noise.slx 


% Model-1
z1      =   iddata(Yout(:,1),Uout,0.025); 
% Validation input-output data, specified as an iddata object. Data can
% have multiple input-output channels. Data is time-domain.
order   =   [1 1 1];
m1      =   oe(z1,order)   % Discrete-time Output error (transfer function) model
% Model-2
z2      =   iddata(Yout(:,2),Uout,0.025);
order   =   [1 1 1];
m2      =   oe(z2,order)  % Discrete-time Output error (transfer function) model
% Check for Missing data and Outliers
Missing_data_M1    =   misdata(z1,m1)
Missing_data_M2    =   misdata(z2,m2)
% Model checking and Validation
zm=merge(z1,z2)
zn=merge(Missing_data_M1,Missing_data_M2)
zm.exp = {'Model 1';'Model 2'}
zn.exp = {'Missing_data_M1';'Missing_data_M2'}
figure(1)
plot(zm,'b-')
grid on
legend('show')
hold on
plot(zn,'r--')
hold off
grid on
legend('show')

m2.OutputName = {'y2'}
z2.OutputName={'y2'}
figure(2)
compare(z1,m1)      % Validation of model 1 with the real plant
grid on
legend('show')
figure(3)
compare(z2,m2)      % Validation of model 2 with the real plant
grid on
legend('show')
figure(4)
resid(z1,m1)        % resid plots the autocorrelation of the residuals and the cross-correlation of the residuals with the input signals.
grid on
legend('show')
figure(5)
resid(z2,m2) 
% The cross-correlation between residuals of m2 and the inputs lie in the 99% confidence band for all lags.
grid on
legend('show')

Threshold_R1_fy1_0 = 3*std(R1)
Threshold_R2_fy1_0 = 3*std(R2)
yline(5.9626, '--c', 'Threshold = 5.9626');
yline(-5.9626, '--c', 'Threshold = -5.9626');
