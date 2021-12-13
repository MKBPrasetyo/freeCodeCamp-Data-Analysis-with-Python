import numpy as np

def calculate(list):
  if len(list) != 9:
    return "List must contain nine numbers."

  else:
    arr = np.array(list)
    mat = arr.reshape(3,3)
    mean1 = mat.mean(axis = 0).tolist()
    mean2 = mat.mean(axis = 1).tolist()
    fltmean = mat.mean()
    mean = [mean1, mean2, fltmean]
    var1 = mat.var(axis = 0).tolist()
    var2 = mat.var(axis = 1).tolist()
    fltvar = mat.var()
    var = [var1, var2, fltvar]
    stdev1 = mat.std(axis = 0).tolist()
    stdev2 = mat.std(axis = 1).tolist()
    fltstdev = mat.std()
    stdev = [stdev1, stdev2, fltstdev]
    max1 = mat.max(axis = 0).tolist()
    max2 = mat.max(axis = 1).tolist()
    fltmax = mat.max()
    max = [max1, max2, fltmax]
    min1 = mat.min(axis = 0).tolist()
    min2 = mat.min(axis = 1).tolist()
    fltmin = mat.min()
    min = [min1, min2, fltmin]
    sum1 = mat.sum(axis = 0).tolist()
    sum2 = mat.sum(axis = 1).tolist()
    fltsum = mat.sum()
    sum = [sum1, sum2, fltsum]
    calculations = {
    'mean' : mean,
    'variance' : var,
    'standard deviation' : stdev,
    'max' : max,
    'min' : min,
    'sum' : sum}
    return calculations