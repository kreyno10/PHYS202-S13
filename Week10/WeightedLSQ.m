function [ m, b, sigmaM, sigmaB ] = WeightedLSQ(x, y, w)
%Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights, w.
    %Perform a weighted linear least squares regression. Return the resulting slope and intercept
    %parameters of the best fit line with their uncertainties.

    %If the weights are all equal to one, the uncertainties on the parameters are calculated using the
    %non-weighted least squares equations.
m = (sum(w)*sum(w.*x.*y) - sum(w.*x)*sum(w.*y))./(sum(w)*sum(w.*x.^2) - (sum(w.*x).^2));
b = ((sum(w.*x.^2)*sum(w.*y) - sum(w.*x)*sum(w.*x.*y))./(sum(w)*sum(w.*x.^2) - (sum(w.*x).^2)));

sigmaM = (sum(w)./(sum(w)*sum(w.*x.^2) - (sum(w.*x)^2))).^(1/2);
sigmaB = (sum(w.*x.^2)./(sum(w)*sum(w.*x.^2) - (sum(w.*x).^2))).^(1/2);

end

