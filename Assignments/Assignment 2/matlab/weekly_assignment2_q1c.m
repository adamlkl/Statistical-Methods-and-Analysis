nsim = 1000000; % number of simulations
roll = 3;       % number of rolls
count = 0;      % frequency of getting 2
N = 6;          % max dice value 

% simulate 1000000 calculations of frequency 
for n1=1:1:nsim
    for n2=1:1:roll
       i = randi(6);
       if i == 2
           count = count + 1;
           break
       end
    end
end 

% calculate probability 
prob = (count/nsim)*100;

res_format = 'Probability = %.4f%%\n';
res = sprintf(res_format,prob);

% print result
disp(res);
    