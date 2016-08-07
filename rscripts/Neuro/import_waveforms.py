#!/usr/bin/python
# DataView Traces to Waveform Vis.

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import json

def import_waveform(filename, nr_trace=None, toplot=False, 
                        savetxt=False, tojson=False, 
                        outname='waveform.txt', dtype=np.float32):
    def iter_loadtxt(filename, delimiter='\t', 
                    skiprows=6, dtype=dtype):
        def iter_func():
            with open(filename, 'r') as infile:
                for _ in range(skiprows):
                    next(infile)
                for line in infile:
                    line = line.rstrip().split(delimiter)
                    for item in line:
                        yield dtype(item)
            iter_loadtxt.rowlength = len(line)
        data = np.fromiter(iter_func(), dtype=dtype)
        data = data.reshape((-1, iter_loadtxt.rowlength))
        return data
    wv = iter_loadtxt(filename, delimiter='\t', skiprows=6)
    if nr_trace is None: nr_trace = range(0, wv.shape[1])
    if toplot is True:
        plt.plot(wv[:, nr_trace])
        plt.show()
    if savetxt is True:
        np.savetxt(outname, wv[:, nr_trace])
    if tojson is True:
        with open(outname, 'wb') as off:
            json.dump(wv[:, nr_trace], off)
    return wv[:, nr_trace]

def load_waveform(filename, trace):
    def iter_loadtxt(filename, delimiter='\t', skiprows=6, dtype=float):
        # http://stackoverflow.com/questions/8956832/python-out-of-memory-on-large-csv-file-numpy
        def iter_func():
            with open(filename, 'r') as infile:
                for _ in range(skiprows):
                    next(infile)
                for line in infile:
                    line = line.rstrip().split(delimiter)
                    for item in line:
                        yield dtype(item)
            iter_loadtxt.rowlength = len(line)
        data = np.fromiter(iter_func(), dtype=dtype)
        data = data.reshape((-1, iter_loadtxt.rowlength))
        return data
    return iter_loadtxt(filename)[:, trace]

def iter_loadtxt(filename, delimiter='\t', skiprows=6, dtype=np.float64):
    # http://stackoverflow.com/questions/8956832/python-out-of-memory-on-large-csv-file-numpy
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)
    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data

def gen_from_iter(filename, delimiter='\t', skiprows=0, dtype=float):
    with open(filename, 'r') as infile:
        for _ in range(skiprows):
            next(infile)
        for line in infile:
            line = line.rstrip().split(delimiter)
            for item in line:
                # print(dtype(item))
                yield dtype(item)

def waveform_compress(filename, trace, n=1000):
    reduced = list()
    wv = load_waveform(filename, trace)
    s = int(len(wv)/n)
    for i in range(int(n)):
        slice_ = wv[i*s:(i+1)*s]
        reduced.append(np.mean(slice_))
    return np.array(reduced, dtype=np.float32)
