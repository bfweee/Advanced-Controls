
clear all
close all
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

% % % Check for Missing data and Outliers
% % check_misdata_M1    =   misdata(z1,m1)
% % check_misdata_M2    =   misdata(z2,m2)
% % 
% noise_level = std(R1)
% 
% noise_level =
% 
%     2.3149
% 
% threshold_upper = 3*noise_level;
% threshold_lower = -3*noise_level;
noise_levelf0r1 = std(R1)
threshold_upperR10 = 3*noise_levelf0r1 ;
threshold_lowerR10 = -3*noise_levelf0r1 ;
figure(1)
hold on

yline(5.9626, '--c', 'Threshold = 5.9626');
yline(-5.9626, '--c', 'Threshold = -5.9626');

noise_levelf0r2 = std(R2)
threshold_upperR20 = 3*noise_levelf0r2 ;
threshold_lowerR20 = -3*noise_levelf0r2 ;
figure(2)
hold on
yline(6.1943, '--c', 'Threshold = 6.1943');
yline(-6.1943, '--c', 'Threshold = -6.1943');

noise_levelf5r1 = std(R1)
threshold_upperR15 = 3*noise_levelf5r1 ;
threshold_lowerR23 = -3*noise_levelf5r1 ;
figure(1)
hold on

yline(8.4312, '--k', 'Threshold = 8.4312');
yline(-8.4312, '--k', 'Threshold = -8.4312');

noise_levelf5r2 = std(R2)
threshold_upperR25 = 3*noise_levelf5r2 ;
threshold_lowerR23 = -3*noise_levelf5r2 ;
figure(2)
hold on
yline(8.2714, '--k', 'Threshold = 8.2714');
yline(-8.2714, '--k', 'Threshold = -8.2714');
noise_levelf3r2 = std(R2)
threshold_upperR23 = 3*noise_levelf3r2 ;
threshold_lowerR23 = -3*noise_levelf3r2 ;
figure(2)
hold on

yline(6.9104, '--r', 'Threshold = 6.9104');
yline(-6.9104, '--r', 'Threshold = -6.9104');
