# adjust default output
pylab.rcParams['figure.figsize'] = (14,6)

# ticker with required step
import matplotlib.ticker
locator = matplotlib.ticker.MultipleLocator(base=1.0)

# plot example
fig, axes = plt.subplots(nrows=8, ncols=1, figsize=(16, 4*len(corr_coeff)), sharey=True)
axes[0].set_title('Correlation coefficients for ecolamp, samples_quantity=15', fontsize=20)
pylab.title('Some name')
for c in corr_coeff:
    ax1 = axes[counter]
    ax1.plot(c, label='some label')
    ax1.set_xlim(0, len(c))
    ax1.set_xlabel('time')
    ax1.set_ylabel('correlation')
    ax1.legend(loc='lowwer right')
    # handle the grid
    ax1.grid(True)
    ax1.xaxis.set_major_locator(locator)

# render same plot many times
from IPython import display
a = random.randn(2, 200)

for i in range(3):
    a += 100
    pylab.scatter(*a)
    display.display(pylab.gcf())
    display.clear_output(wait=True)
    time.sleep(1.0)

# add suptitle
fig.suptitle(filename + ': ' + readme, x=0.52, y=0.93)

# enable legend for all axes
_ = [axe.legend(loc='upper right') for axe in axes]

# save image
fig.savefig('path to save')

# plot vertical line
ax.axvline(x, color='k', linestyle='--')

# plot russian text
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font',**font)
# or try this
rc('font',**{'family':'serif'})
rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')
