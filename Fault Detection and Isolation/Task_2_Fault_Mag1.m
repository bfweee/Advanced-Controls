
sim Task2_Fault_Mag1.slx 


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


Threshold_R1_fy1_0 = 3*std(R1)
Threshold_R2_fy1_0 = 3*std(R2)
Threshold_R1_fy1_3 = 3*std(R1)
Threshold_R2_fy1_3 = 3*std(R2)
Threshold_R1_fy1_5 = 3*std(R1)
Threshold_R2_fy1_5 = 3*std(R2)

% % Check for Missing data and Outliers
% check_misdata_M1    =   misdata(z1,m1)
% check_misdata_M2    =   misdata(z2,m2)


% % Model checking and Validation
% zm=merge(z1,z2)
% zn=merge(check_misdata_M1,check_misdata_M2)
% zm.exp = {'Model 1';'Model 2'}
% zn.exp = {'check_misdata_M1';'check_misdata_M2'}
% figure(1)
% plot(zm,'b-')
% grid on
% legend('show')
% hold on
% plot(zn,'r--')
% hold off
% grid on
% legend('show')
% 
% m2.OutputName = {'y2'}
% z2.OutputName={'y2'}
% figure(2)
% compare(z1,m1)      % Validation of model 1 with the real plant
% grid on
% legend('show')
% figure(3)
% compare(z2,m2)      % Validation of model 2 with the real plant
% grid on
% legend('show')
