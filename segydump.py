import struct
import sys

import segyio

# Program to dump segy headers


def dump_binhead(data):
    ### binary header
    fields = [
        "Job ID Number",
        "Line Number",
        "Reel Number",
        "Traces Per Ensemble",
        "Aux Traces Per Ensemble",
        "Sample Interval",
        "Sample Interval in Field",
        "Samples Per trace",
        "Samples per trace in field",
        "Data Format Code",
        "Ensemble Fold",
        "Trace Sorting Code",
        "Vertical Sum Code",
        "Sweep Start Freq",
        "Sweep Stop Freq",
        "Sweep Length",
        "Sweep Type",
        "Trace Num of Sweep Channel",
        "Sweep Trace Taper Len Start",
        "Sweep Trace Taper Len End",
        "Taper Type",
        "Correlated Data",
        "Binary Gain Recovered",
        "Amplitude Recovery Method",
        "Measurement System",
        "Impluse Signal Polarity",
        "Vibratory Polarity Code",
        "Ext Traces Per Ensemble",
        "Ext Aux Traces Per Ensemble",
        "Ext Samples Per Trace",
        "Ext Sample Interval",
        "Ext Field Sample Interval",
        "Ext Field Samples Per Trace",
        "Ext Ensemble Fold",
        "Integer Constant",
        "SEG-Y Fmt Rev Maj",
        "SEG-Y Fmt Rev Min",
        "Fixed Len Trace Flag",
        "Num Ext Text Hdrs",
        "Num Add Trace Hdrs",
        "Time Basis Code",
        "Num Traces in File",
        "Byte Offset of First Trace",
        "Number of Data Trailer Stanzas",
    ]
    fmt0 = ">IIIHHHHHHHHHHHHHHHHHHHHHHHHIIIddIII" + 200 * "x" + "BBHHIHQQI" + 68 * "x"

    hdr = struct.unpack(fmt0, data)
    for i in range(len(hdr)):
        print(fields[i] + " = " + str(hdr[i]))


def main():
    with open("./s_01294501_segy.sgy", "rb") as f:
        print("MINE---------------")
        data = f.read()
        data = data[3200:3600]
        dump_binhead(data)
    print()
    print()
    with open("./line10pro.sgy", "rb") as f:
        print("WORKNG--------------")
        data = f.read()
        data = data[3200:3600]
        dump_binhead(data)


main()
