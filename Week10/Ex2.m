experiment = importdata('radioactivedecay.dat.txt') 
t = experiment.data(:,1); 
N = experiment.data(:,2); 
figure(42)
plot(t,N,'b:')
%%
hold on
%function to fit 
fun = @(t, N) 50*exp(-t);
%Find a starting point for the parameters. 
guess = fun(t); 
plot(t,guess,'r:');
%%
% fit the data 
fittedmodel = fit(t',N',fun,'StartPoint'); 
% plot the result 
plot(fittedmodel,'r-');
hold off

