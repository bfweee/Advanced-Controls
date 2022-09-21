
clear all
sim Task3_Structured_residuals.slx 

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

% %  Check for Missing data and Outliers
check_misdata_M1    =   misdata(z1,m1)
check_misdata_M2    =   misdata(z2,m2)

% figure
yline(7.6360, '--k', 'Threshold = 7.6360');
 yline(-7.6360, '--k', 'Threshold = -7.6360');
 
% noise_levelRout15 = std(Rout1)
% threshold_upper = 3*noise_level;
% threshold_lower = -3*noise_level;
% noise_levelf0r1 = std(R1)
% threshold_upperR10 = 3*noise_levelf0r1 ;
% threshold_lowerR10 = -3*noise_levelf0r1 ;
% figure(6)
% plot(tout,Rout1)
% grid on 
% legend('show')
% xlabel('Time (s)')
% ylabel('Residual R2')
% title('Noise 0.01, Step Response of Residual R1,R2,R3 ')

% hold on
% figure(1)
% yline(7.6360, '--k', 'Threshold = 7.6360');
% yline(-7.6360, '--k', 'Threshold = -7.6360');
% figure(2)
% yline(5.1681, '--k', 'Threshold = 5.1681');
% yline(-5.1681, '--k', 'Threshold = -5.1681');
% figure(3)
% yline(4.1840, '--k', 'Threshold = 4.1840');
% yline(-4.1840, '--k', 'Threshold = -4.1840');
% figure(4)
% yline(7.6360, '--k', 'Threshold = 7.6360');
% yline(-7.6360, '--k', 'Threshold = -7.6360');
% yline(5.1681, '--k', 'Threshold = 5.1681');
% yline(-5.1681, '--k', 'Threshold = -5.1681');
% yline(4.1840, '--k', 'Threshold = 4.1840');
% yline(-4.1840, '--k', 'Threshold = -4.1840');
% hold off
%noise_levelf0r2 = std(R2)
% threshold_upperR20 = 3*noise_levelf0r2 ;
% threshold_lowerR20 = -3*noise_levelf0r2 ;
figure(1)
hold on
plot(tout,R1)
grid on 
legend('show')
xlabel('Time (s)')
ylabel('Residual R1')
title('Residual R1 at Output Faults 0,5 and 11 , Step-time = 3')
hold off
figure(2)
hold on
plot(tout,R2)
grid on 
legend('show')
xlabel('Time (s)')
ylabel('Residual R2')
title('Residual R2 at Output Faults 0,5 and 11 , Step-time = 3')
hold off
figure(3)
grid on 
hold on
plot(tout,R3)
legend('show')
xlabel('Time (s)')
ylabel('Residual R3')
title('Residual R3 at Output Faults 0,5 and 11, Step-time = 3')
hold off
figure(4)
hold on
grid on
plot(tout,Rout1)
legend('show')
xlabel('Time (s)')
ylabel('Residuals R1,R2,R3')
title('Residuals R1,R2,R3 at Output Faults 0,5 and 11 , Step-time = 3')
hold off
grid on 
% legend('show')
% xlabel('Time (s)')
% ylabel('Residual R2')
% title('Noise free Step Response of Residual R1,R2,R3 ')

% plot(tout,R1)
% hold off
% grid on
% legend('show')
% title('R1 with Fy1 (Noise), Step-time = 3')
% % % 
% 
% 
% figure(2)
% hold on
% plot(tout,R2)
% hold off
% grid on
% legend('show')
% title('R2 with Fy2 (Noise), Step-time = 3')
% 
% 
% % figure(2)
% % hold on
% % plot(tout,R2) 
% % % figure(2)
% 
% % plot(tout,R2)
% % hold off
% % grid on
% % legend('show')
% % title('R2 with Fu (Noise free), Step-time = 3')
% % title('R2 with Fy2 (Noise free) ,Steptime=3')

% % % Set thresholds for residual validation
% % alpha = 0.05;
% % threshold_upper1 = mean_residuals1 + norminv(1-alpha/2)*std_residuals1;
% % threshold_lower1 = mean_residuals1 - norminv(1-alpha/2)*std_residuals1;
% % threshold_upper2 = mean_residuals2 + norminv(1-alpha/2)*std_residuals2;
% % threshold_lower2 = mean_residuals2 - norminv(1-alpha/2)*std_residuals2;
% % 
% % % Perform residual validation and detect faults
% % fault_detected1 = false(size(residuals1, 1), 1);
% % fault_detected2 = false(size(residuals2, 1), 1);
% % for i = 1:size(residuals1, 1)
% %     if residuals1(i) > threshold_upper1 || residuals1(i) < threshold_lower1
% %         fault_detected1(i) = true;
% %     end
% %     if residuals2(i) > threshold_upper2 || residuals2(i) < threshold_lower2
% %         fault_detected2(i) = true;
% %     end
% % end
% % 
% % % Plot residuals and faults with magnitudes of 1, 5, and 8
% % figure
% % 
% % 
% % % Plot residuals and faults with magnitudes of 1, 5, and 8
% % figure;
% % subplot(2,1,1);
% % plot(residuals1);
% % hold on;
% % plot(find(fault_detected1), residuals1(fault_detected1), 'ro', 'MarkerSize', 1);
% % plot([1 size(residuals1, 1)], [threshold_upper1 threshold_upper1], 'r--');
% % plot([1 size(residuals1, 1)], [threshold_lower1 threshold_lower1], 'r--');
% % ylim([-8 8]);
% % title('Residuals and Faults for Model 1');
% % ylabel('Residuals');
% % xlabel('Sample Number');
% % legend('Residuals', 'Detected Faults', 'Thresholds
% % fault_indices = [100, 200, 300]; % Indices of simulated faults
% % % Plot residuals for both models
% % figure
% % plot(resid1)
% % hold on
% % plot(resid2)
% % legend('Model 1', 'Model 2')
