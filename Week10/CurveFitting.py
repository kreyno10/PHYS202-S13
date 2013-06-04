import numpy as np
def LinearLeastSquaresFit(x,y):
    """take i arrays representing (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slope and intercept
    parameters of te best fit line with their uncertainties."""
    
    xav =np.zeros(len(x), float)
    xav = sum(x)/len(x) #average x value
    yav =np.zeros(len(y), float)
    yav = sum(y)/len(y)#average y value
    xav2 = np.zeros(len(x), float)
    xav2 = sum(x**2)/len(x) #average x^2 value
    xy = np.zeros(len(x), float)
    xy = sum(x * y)/len(x) #average value of xy

    m = (xy - xav*yav) / (xav2 - xav**2) # slope
    b = (xav2*yav - xav*xy)/ (xav2 - xav**2) #intercept
    
    d = np.zeros(len(x), float)
    for n in range(len(x)):
        d[n] = y[n] - (m*x[n] + b) #vertical deviation
        
    x2 = np.zeros(len(d), float)
    for n in range(len(x)): 
        x2[n] = sum(d[n]**2)#sum of squares of vertical deviations
    
    x2av = np.zeros(len(d), float)
    x2av = sum(x2)/len(x) #average sum of squares of vertical deviation
    
    sigmaM = sqrt(1/float(len(x) -2) * x2av/(xav2 - xav**2))#uncertainty in slope
    sigmaB = sqrt(1/float(len(x) -2) * x2av*xav2/(xav2 - xav**2))#uncertainty in intercept
    
    return "slope=", m, "intercept=", b, "slope error=", sigmaM, "intercept error=", sigmaB


def WeightedLinearLeastSquaresFit(x,y,w):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights, w.
    Perform a weighted linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties.

    If the weights are all equal to one, the uncertainties on the parameters are calculated using the
    non-weighted least squares equations."""
    
    sumw = np.zeros(len(w), float)
    sumw = sum(w)
    sumwx = np.zeros(len(w), float)
    sumwx = sum(w*x)
    sumwy = np.zeros(len(w), float)
    sumwy = sum(w*y)
    sumwx2 = np.zeros(len(w), float)
    sumwx2 = sum(w*(x**2))
    sumwxy = np.zeros(len(w), float)
    sumwxy = sum(w*x*y)
    
    m = (sum(w)*sum(w*x*y) - sum(w*x)*sum(w*y))/(sum(w)*sum(w*x**2) - (sum(w*x))**2)#slope with weighting
    b = (sumwx2*sumwy - sumwx*sumwxy)/(sumw*sumwx2 - sumwx**2)#intercept with weighting 
    
    sigmaM = sqrt(sumw/(sumw*sumwx2 - sumwx**2))
    sigmaB = sqrt(sumwx2/(sumw*sumwx2 - sumwx**2))
    
    if sum(w)/len(w) == 1: #weights are all equal to one, uncertainties are unweighted
        xav = np.zeros(len(x), float)
        xav = sum(x)/len(x) #average x value
        xav2 = np.zeros(len(x), float)
        xav2 = sum(x**2)/len(x) #average x^2 value

        d = np.zeros(len(x), float)
        for n in range(len(x)):
            d[n] = y[n] - (m*x[n] + b) #vertical deviation
        
        x2 = np.zeros(len(d), float)
        for n in range(len(x)): 
            x2[n] = sum(d[n]**2)#sum of squares of vertical deviations
    
        x2av = np.zeros(len(d), float)
        x2av = sum(x2)/len(x) #average sum of squares of vertical deviation
    
        sigmaM = sqrt(1/float(len(x) -2) * x2av/(xav2 - xav**2))#uncertainty in slope
        sigmaB = sqrt(1/float(len(x) -2) * x2av*xav2/(xav2 - xav**2))#uncertainty in intercept
    
    
    return "m=",m, "m err=", sigmaM, "b=",b, "b err=", sigmaB
