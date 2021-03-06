import numpy as np

# Let's do some plotting
from matplotlib import pyplot as pl

def plot(test, input, f, predicted, sigma):

  fig = pl.figure()
  pl.plot(test, f(test), 'r:', label=u'$f(x) = x\,\sin(x)$')
  pl.plot(input, f(input), 'r.', markersize=10, label=u'Observations')
  pl.plot(test, predicted, 'b-', label=u'Prediction')
  pl.fill(np.concatenate([test, test[::-1]]),
        np.concatenate([predicted - 1.9600 * sigma,
                       (predicted + 1.9600 * sigma)[::-1]]),
        alpha=.5, fc='b', ec='None', label='95% confidence interval')
  pl.xlabel('$x$')
  pl.ylabel('$f(x)$')
  pl.ylim(-10, 20)
  pl.legend(loc='upper left')
  pl.show()



def gpTest():
  # Plot the function, the prediction and the 95% confidence interval based on
  # the MSE
  x = np.atleast_2d(np.linspace(0, 10, 100)).T
  print x.shape

  def f(x):
      """The function to predict."""
      return x * np.sin(x)

  X = np.array([[1.], [3.], [5.], [6.], [7.], [8.]])
  # X = np.array([1., 3., 5., 6., 7., 8.])

  print X
  # Observations
  y = f(X).ravel()

  gaussianP = gptheano.GaussianProcess(covFunction=gptheano.ARDSquareExponential(1), noise=0.1)
  gaussianP.fit(X, y)
  res =  gaussianP.predict(np.array([0.0]))
  # res =  gaussianP.predict(0.0)
  print "predict"
  print res
  
   # my predict still does not work with mutiple instances but doing that is not hard
  y_pred, sigma = gaussianP.predictAll(x)
  plot(x, X, f, y_pred, sigma)

  # THIS WILL CHANGE THE HYPERPARAMETERS
  print "optimizing"
  res = gaussianP.optimizehyperparams()
  print "returned hyperparams", res

  XNew = np.array([[0.], [2.], [4.], [9.]])
  yNew = f(XNew).ravel()
  gaussianP.fit(XNew, yNew)
  res =  gaussianP.predict(np.array([0.0]))
  print "predict 0.0 after optimization", res


def main():
  gpTest()

if __name__ == '__main__':
  main()
