#!/usr/bin/env python3
"""This script plots a simple 2D plot.

Run: python plot2D_line.py
Optional: python3 plot2D.py -f sample_data.csv -x "Xlabel" -y "Ylabel" -t "Title" -l "Data" -s thefig.png -py "loglog"
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_csv_data(file_path):
	df = pd.read_csv(file_path)
	datacolumns = df.columns
	x = df[df.columns.values[0]].to_numpy()    # or df.iloc[:,0].to_numpy()
	y = df[df.columns.values[1]].to_numpy()    # or df.iloc[:,1].to_numpy()
	return x, y

def plot_line(file_path, title="Title goes here", xlabel="X Axis Label", ylabel="Y Axis Label", legend="Legend",save=None, plot_type="line", hold_on=False):
	
	x, y = read_csv_data(file_path)
	fig, ax = plt.subplots()
	if plot_type == "line":
		ax.plot(x, y, marker="o")
	elif plot_type == "scatter":
		ax.scatter(x, y)
	elif plot_type == "bar":
		ax.bar(x, y)
	elif plot_type == "logx":
		ax.semilogx(x, y)
	elif plot_type == "logy":
		ax.semilogy(x, y)
	elif plot_type == "loglog":
		ax.loglog(x, y)
	ax.set_title(title)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.legend(legend, loc="best")
	ax.grid(True)
	if hold_on == False:
		plt.show()
		if save:
			fig.savefig(save, dpi=150)
			print(f"Saved plot to {save}")
		else:
			plt.show()
	else:
		fig.show()


def plot2d_simple():
	parser = argparse.ArgumentParser(description="Simple 2D line plot")
	parser.add_argument("--file", "-f", help="Path to the CSV file")
	parser.add_argument("--xlabel","-x", help="Label for X axis")
	parser.add_argument("--ylabel", "-y", help="Label for Y axis")
	parser.add_argument("--title", "-t", help="Title for the plot")
	parser.add_argument("--legend", "-l", help="Legend for the plot")
	parser.add_argument("--save", "-s", help="Path to save the plot image (PNG/JPG).")
	parser.add_argument("--type", "-pt", help="Type of the plot. Options: line, scatter, bar. Default is line.", default="line")
	args = parser.parse_args()
	"""
	if filename==None:
		plot_line(args.file, title=args.title, xlabel=args.xlabel, ylabel=args.ylabel, legend=args.legend, save=args.save, plot_type=args.type,hold_on=hold_on)
	else:
		plot_line(filename, title=args.title, xlabel=args.xlabel, ylabel=args.ylabel, legend=args.legend, save=args.save, plot_type=args.type,hold_on=hold_on)
	"""
	plot_line(args.file, title=args.title, xlabel=args.xlabel, ylabel=args.ylabel, legend=args.legend, save=args.save, plot_type=args.type)


if __name__ == "__main__":
	plot2d_simple()
