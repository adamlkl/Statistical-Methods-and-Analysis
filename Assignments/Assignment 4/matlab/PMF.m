c = [0.125,0.375,0.375,0.125];
x = [-3,-1,-1,-1,1,1,1,3];  
nbins=4;
hist(x,nbins,'Normalization','cdf');
cdf = cumsum(c);
disp(cdf);

