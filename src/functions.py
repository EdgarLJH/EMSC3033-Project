""" Functions needed to run notebook:

  - random_points()
  - get_cdf()
  - get_std()
  - ks2()
  - plot_cdf()
  - plot_hist_d()
  - plot_violin_p()

"""

from .dependencies import *

def documentation():
  
    markdown_documentation = """   
The notebook takes location data and calculates its closest approach to a user-defined lithospheric depth. Data locations are shown on different LAB maps 
and the distances are plotted as cumulative distribution functions. Finally, two-sample Kolmogorov-Smirnov tests are conducted to test the significance of
these distances. 
"""

    return markdown_documentation
  
  

def random_points(deposit_data, n):
    '''
    Generate n number of CDFs of random points, each the same size as the deposit data.
    '''   
    arrrandom = np.empty((0, 2))
    arronshore = np.empty((0, 2))
    arroffshore = np.empty((0, 2))
    
    while len(arronshore) < len(deposit_data) * n:
        lons = random.uniform(-180, 180)
        lats = random.uniform(-90, 90)
        arrrandom = np.append(arrrandom, np.array([[lons, lats]]), axis = 0)
        
        # If loop to determine onshore and offshore coordinates
        if globe.is_land(lats, lons) == True: 
            arronshore = np.append(arronshore, np.array([[lons, lats]]), axis = 0)
        else:
            arroffshore = np.append(arroffshore, np.array([[lons, lats]]), axis = 0)
    return arrrandom, arronshore, arroffshore
    
  

def get_cdf(data):
    '''
    Calculate cumulative distribution function (CDF) and probability density function (PDF) for a set of data.
    '''
    count, bins_count = np.histogram(data, bins = np.arange(0, max(data), 10))
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    return cdf, pdf, bins_count

  

def get_std(data):
    '''
    Calculate standard deviation for a set of data. 
    '''
    sort_dist = np.sort(data)
    bins = np.arange(0, max(sort_dist), 10)
    digit = np.digitize(sort_dist, bins)
    
    std_random = np.empty((0))
    
    for i in range(1, len(bins) + 1):
        std_random = np.append(std_random, np.std(sort_dist[np.where(digit == i)[0]])) 
    
    return std_random

    
    
def ks2(data1, data2, n):
    '''
    2-sample Kolmogorov-Smirnov test comparing data1 to multiple data2 CDFs. 
    data1: Data CDF
    data2: n number of CDFs of random locations
    '''
    d = np.empty((0))
    p = np.empty((0))
    lower = 0
    upper = int(len(data2) / n)
    for i in range(n):
        d_ks = stats.ks_2samp(data1, data2[lower:upper])[0]
        p_ks = stats.ks_2samp(data1, data2[lower:upper])[1]
        d = np.append(d, d_ks)
        p = np.append(p, p_ks)
        lower += int(len(data2) / n)
        upper += int(len(data2) / n)
    return np.array([d, p])

    
    
def plot_cdf(data_deposit, data_random, std_random, ax, title, z):
    '''
    Plot CDF of geodesic distances.
    '''
    ax.axvline(x = z, color = "black", linestyle = "-.") # Show contour line
    ax.plot(data_deposit[2][0:-1], 100 * data_deposit[0], color = "C1", 
            label = "Raw number of data points")
    ax.plot(data_random[2][0: -1], 100 * data_random[0], color = "black", 
            label = "Random continental locations (mean)")
    ax.plot(data_random[2][0: -1], 100 * data_random[0] + std_random[0:-1], color = "gray",
              label = "Random continental locations (standard dev.)")
    ax.plot(data_random[2][0: -1], 100 * data_random[0] - std_random[0:-1], color = "gray")
    ax.fill_between(data_random[2][0: -1], 
                    100 * data_random[0] + std_random[0:-1], 
                    100 * data_random[0] - std_random[0:-1], 
                    color='silver', alpha=0.5)
    ax.set_xlabel("Distance from " + str(z) + " LAB contour (km)", labelpad = 10)
    ax.set_ylabel("Cumulative Frequency (%)")
    ax.legend(loc = 'lower right', prop={'size': 8})
    ax.set_xlim([0, 1400])
    ax.set_ylim([0, 100])
    ax.set_title(title)
    
    return ax
    
    
def plot_hist_d(data, ax):
    '''
    Plot histogram of D-values.
    '''
    ax.hist(data, bins = np.arange(round(min(data), 2) - 0.01, round(max(data), 2) + 0.01, 0.01), 
            color = "black", edgecolor = "white", linewidth = 1.2)
    ax.annotate(str(round(np.mean(data), 2)) + u"\u00B1" + str(round(np.std(data), 2)), 
                xy=(.96, .94), xycoords='axes fraction', ha='right', va='top', fontsize = 8, weight = 'bold')
    ax.set_xlabel('D-value', labelpad = 10)
    ax.set_ylabel('Count')
    
    return ax


def plot_violin_p(data, ax):
    '''
    Produce violin plot of p-values.
    '''
    ax.violinplot(data, vert = False)
    plt.gca().invert_xaxis()
    ax.set_xlabel('p-value', labelpad = 10)
