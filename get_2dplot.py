import matplotlib.pyplot as plt
import numpy as np


def read_data_from_file(filename, delimiter=None):
    """
    Read numeric data from a text file.
    Expects two columns (x and y) per line, separated by whitespace or a delimiter.
    Lines starting with '#' are treated as comments and skipped.

    Parameters:
        filename (str): Path to the text file.
        delimiter (str): Column delimiter (default: any whitespace).

    Returns:
        x, y (np.ndarray, np.ndarray): Parsed data arrays.
    """
    x_vals, y_vals = [], []

    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(delimiter)
                if len(parts) < 2:
                    print(f"Warning: skipping malformed line {line_num}: {line}")
                    continue
                try:
                    x_vals.append(float(parts[0]))
                    y_vals.append(float(parts[1]))
                except ValueError:
                    print(f"Warning: skipping non-numeric line {line_num}: {line}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")

    if not x_vals:
        raise ValueError("No valid data found in file.")

    return np.array(x_vals), np.array(y_vals)


def ask_plot_type():
    """
    Prompt the user to choose a plot type.

    Returns:
        str: One of 'line', 'loglog', or 'bar'.
    """
    valid_types = {'line': 'line', 'l': 'line',
                    'loglog': 'loglog', 'log': 'loglog',
                    'bar': 'bar', 'b': 'bar'}

    while True:
        """
        choice = input(
            "Choose a plot type:\n"
            "  [1] Line plot\n"
            "  [2] Log-Log plot\n"
            "  [3] Bar plot\n"
            "Enter choice (name or number): "
        ).strip().lower()
        """
        choice = input(
            "Choose a plot type:\n"
            "  [1] Expt with hollow circles\n"
            "  [2] Line plot\n"
            "  [3] Log-Log plot\n"
            "  [4] Bar plot\n"
            "Enter choice (name or number): "
        ).strip().lower()

        # Allow numeric shortcuts too
        #num_map = {'1': 'line', '2': 'loglog', '3': 'bar'}
        num_map = {'1': 'expt', '2': 'line', '3': 'loglog', '4': 'bar'}
        if choice in num_map:
            return num_map[choice]
        if choice in valid_types:
            return valid_types[choice]

        print("Invalid choice. Please enter 'line', 'loglog', 'bar', or 1/2/3.\n")

def plot_data_multiple_i(x,y, plot_type,themarker,ax):

    if plot_type == 'expt':
        ax.plot(x, y, themarker, markerfacecolor='none', markersize=6, linestyle='None')

    elif plot_type == 'line':
        ax.plot(x, y, themarker, linestyle='-', color='steelblue')

    elif plot_type == 'loglog':
        ax.loglog(x, y, themarker, linestyle='-', color='darkorange')

    elif plot_type == 'bar':
        ax.bar(x, y, color='seagreen', width=(x.max() - x.min()) / max(len(x), 1) * 0.8 if len(x) > 1 else 0.8)

    else:
        raise ValueError(f"Unknown plot type: {plot_type}")

    return ax
    

def plot_data(x, y, plot_type, xlabel="X", ylabel="Y", title=None, legend=None, filename=None):
    """
    Plot data according to the specified plot type.

    Parameters:
        x, y (array-like): Data to plot.
        plot_type (str): 'line', 'loglog', or 'bar'.
        xlabel, ylabel (str): Axis labels.
        title (str): Optional plot title.
    """
    plt.figure(figsize=(8, 5))

    if plot_type == 'expt':
        plt.plot(x, y, 'ok', markerfacecolor='none', markersize=6, linestyle='None')
        plt.title(title or "Experiment Plot")

    elif plot_type == 'line':
        plt.plot(x, y, marker='o', linestyle='-', color='steelblue')
        plt.title(title or "Line Plot")

    elif plot_type == 'loglog':
        # loglog requires positive values
        mask = (x > 0) & (y > 0)
        if not np.all(mask):
            print("Warning: non-positive values excluded from log-log plot.")
        plt.loglog(x[mask], y[mask], marker='o', linestyle='-', color='darkorange')
        plt.title(title or "Log-Log Plot")

    elif plot_type == 'bar':
        plt.bar(x, y, color='seagreen', width=(x.max() - x.min()) / max(len(x), 1) * 0.8 if len(x) > 1 else 0.8)
        plt.title(title or "Bar Plot")

    else:
        raise ValueError(f"Unknown plot type: {plot_type}")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend([legend])

    #plt.xlabel(getxlabel())
    #plt.ylabel(getylabel())
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    #if filename is None:
    #    filename = getfilename()
    plt.savefig(filename+'.png', dpi=150)

def getfilename():
    choice = input(
            "Provide name of the plot to be saved as png file:"
        ).strip().lower()
    return choice

def getxlabel():
    choice = input(
            "Provide the X-axis label:"
        ).strip().lower()
    return choice

def getylabel():
    choice = input(
            "Provide the Y-axis label:"
        ).strip().lower()
    return choice

def howmanydatapoints():
    choice = input(
            "Choose data to be selected from one file or multiple files [1] for one data files [2] for multiple files:"
        ).strip().lower()
    return choice

def standaloneplots():
    thenum = howmanydatapoints()
    if thenum == '1':
        filename = input("Enter path to data file: ").strip()
        x, y = read_data_from_file(filename)
        plot_type = ask_plot_type()
        plot_data(x, y, plot_type, xlabel="X", ylabel="Y")
    
    if thenum == '2':
        num_files = int(input("Enter number of data files: ").strip())
        all_x, all_y = [], []
        plot_type = ask_plot_type()
        for i in range(num_files):
            filename = input(f"Enter path to data file {i+1}: ").strip()
            x, y = read_data_from_file(filename)
            plot_data(x, y, plot_type, xlabel="X", ylabel="Y")
            #all_x.append(x)
            #all_y.append(y)
        
        # Concatenate all data
        #x_combined = np.concatenate(all_x)
        #y_combined = np.concatenate(all_y)
        
        #plot_type = ask_plot_type()
        #plot_data(x_combined, y_combined, plot_type, xlabel="X", ylabel="Y")
def onlyexpt():
    # Plot single experiment from a data file
    #filename = input("Enter path to data file: ").strip()
    filename = "data.txt"  # Example filename
    x, y = read_data_from_file(filename)
    plot_type = ask_plot_type()
    plot_data(x, y, plot_type, xlabel="X", ylabel="Y", title="Experiments from data",legend="Experiment", filename = 'expt_plot')

def multiple_expt():
    # Plot multiple experiments from data files.

    # This is the list of files to be plotted.
    filenamev = ["data.txt", "data2.txt"]  # Example filenames
    filename = 'multiple_expt_plot' # Output filename for the combined plot

    # ===========================================================================
    plot_type = ask_plot_type()
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4))

    markers = ['ok', 'or', 'ob', 'og', 'om', 'oc']  # Different markers for each dataset
    for filename, marker in zip(filenamev, markers):
        x, y = read_data_from_file(filename)
        ax=plot_data_multiple_i(x, y, plot_type, marker, ax)

    plt.title("Multiple Experiments from data")
    plt.show()
    plt.legend(["Data 1", "Data 2"])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig(filename+'.png', dpi=150)

if __name__ == "__main__":
    #onlyexpt()
    multiple_expt()
