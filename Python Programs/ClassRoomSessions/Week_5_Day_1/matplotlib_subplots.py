import matplotlib.pyplot as pl

labels=['Passed', 'Failed', 'Skipped']
executionCount=[45,10,5]
# Passed	45
# Failed	10
# Skipped	5

Weeks=[1,2,3,4,5,6]
Defects=[5,8,6,10,7,4]

# pl.subplot(0,1,)
# pl.hist(Weeks, bins=5)
# pl.show()

fig, axes = pl.subplots(2,1)
axes[0].plot(labels, executionCount)
axes[1].plot(Weeks, Defects)
pl.show()

