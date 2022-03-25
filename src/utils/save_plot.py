import pandas as pd
import matplotlib.pyplot as plt
import time
import os

def get_unique_plotname(plot_name):
    unique_plotname = time.strftime(f"%Y%m%d_%H%M%S_{plot_name}")
    return unique_plotname

def save_plot(df, plot_name, plot_dir):
    df.plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    
    
    unique_plotname = get_unique_plotname(plot_name)
    path_to_join = os.path.join(plot_dir, plot_name)
    
    plt.savefig(path_to_join)
    plt.show()
    
    
