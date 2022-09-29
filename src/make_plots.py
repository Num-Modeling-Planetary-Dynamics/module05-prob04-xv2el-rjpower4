from datasets import ElementDataset, data_directory
import matplotlib.pyplot as plt
import numpy as np

def plot_dataset(ds: ElementDataset):
    fig, axs = plt.subplots(2, sharex=True)
    fig.set_size_inches(10, 8)
    fig.suptitle(ds.name, fontsize=20)

    for ax in axs:
        ax.grid()
        ax.tick_params(left=True, right=True)
        ax.tick_params(labelleft=True, labelright=True)
    
    axs[0].plot(ds.data.t / 365.0 / 100.0, ds.data.a)
    axs[0].set_ylabel("Semi-Major Axis [AU]", fontsize=18)
    axs[0].tick_params('both', labelsize=18)

    axs[1].plot(ds.data.t / 365.0 / 100.0, np.rad2deg(ds.data.inclination))
    axs[1].set_ylabel("Inclination [deg]", fontsize=18)
    axs[1].set_xlabel("Time [Century]", fontsize=18)
    axs[1].tick_params('both', labelsize=18)

    return (fig, axs)

# ----------------------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------------------
def main():
    datasets = ElementDataset.load_all(data_directory())
    return datasets

if __name__ == "__main__":
    datasets = main()
    for ds in datasets:
        f, a = plot_dataset(ds)
        f.savefig(ds.output_path(), dpi=300)