% initialise P(L) array 
PL = [0.05,0.1,0.05,0.05;
      0.05,0.1,0.05,0.05;
      0.05,0.05,0.1,0.05;
      0.05,0.05,0.1,0.05];
  
%initialise P(O|L) array   
POL = [0.75,0.95,0.75,0.05;
       0.05,0.75,0.95,0.75;
       0.01,0.05,0.75,0.95;
       0.01,0.01,0.05,0.75];
   
% size of array
N = 4;

% initialise P(L|O) array to store solutions 
PLO = zeros(N,N);

% check final probability, must be 1
sum = 0;

% calculate P(L|O) for each cell
for n1=1:1:N
    for n2=1:1:N
        PO = calculatePO(PL,POL,N,n1,n2);
        PLO(n1,n2)=(PL(n1,n2)*POL(n1,n2))/PO;
        sum = sum + PLO(n1,n2);
    end
end 

% print result
disp(PLO);
disp(sum);

% calculate P(O)
function PO = calculatePO(PL, POL, N, n1, n2)
PO = 0;
for c1=1:1:N
    for c2=1:1:N
        if c1 ~= n1 || c2 ~= n2
            PO = PO + (PL(c1,c2)*POL(c1,c2));
        end
    end
end
PO = PO + (PL(n1,n2)*POL(n1,n2));
end