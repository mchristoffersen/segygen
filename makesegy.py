# Python 3.7.0

# Program to generate segy files

import numpy as np
import matplotlib.pyplot as plt
import struct

### Function defs

def build_binhead(spt, ntrace):
    ### Build binary header
    ### Important fields have comment that starts with #!!!
    binhead = b''
    # Job identification number
    binhead += struct.pack(">I",1)
    # Line number
    binhead += struct.pack(">I",1)
    # Reel number
    binhead += struct.pack(">I",1)
    # Traces per ensemble
    binhead += struct.pack(">H",1)
    # Auxiliary traces per ensemble
    binhead += struct.pack(">H",0)
    # Sample interval - ignored (later one is used)
    binhead += struct.pack(">H",375)
    # Field recording sample interval
    binhead += struct.pack(">H",375)
    #!!! Samples per trace
    binhead += struct.pack(">H",spt)
    # Field recording samples per trace
    binhead += struct.pack(">H",spt)
    #!!! Data format code - see format doc 
    binhead += struct.pack(">H",5)
    # Ensemble fold
    binhead += struct.pack(">H",1)
    #!!!? (Maybe important?) Trace sorting code - see format doc
    binhead += struct.pack(">H",4)
    #!!!? Vertical sum code (What is this?)
    binhead += struct.pack(">H",1)
    # Sweep freq start
    binhead += struct.pack(">H",0)
    # Sweep freq end
    binhead += struct.pack(">H",0)
    # Sweep length
    binhead += struct.pack(">H",0)
    # Sweep type
    binhead += struct.pack(">H",0)
    # Trace number of sweep channel
    binhead += struct.pack(">H",0)
    # Sweep trace taper length at start
    binhead += struct.pack(">H",0)
    # Sweep trace taper length at end
    binhead += struct.pack(">H",0)
    # Taper type
    binhead += struct.pack(">H",0)
    # Correlated data traces, 2 is yes
    binhead += struct.pack(">H",2)
    # Binary gain recovered, 2 is no
    binhead += struct.pack(">H",1)
    # Amplitude recovery method, 1 is none
    binhead += struct.pack(">H",4)
    # Measurement system, 1 is meters
    binhead += struct.pack(">H",1)
    # Implulse signal polarity
    binhead += struct.pack(">H",1)
    # Vibratory polarity code
    binhead += struct.pack(">H",0)
    # Extended number of traces per ensemble
    binhead += struct.pack(">I",0)
    # Extended number of auxiliary traces per ensemble
    binhead += struct.pack(">I",0)
    # Extended samples per trace
    binhead += struct.pack(">I",0)
    #!!! Extended sample interval
    binhead += struct.pack(">d",37.5)
    # Extended field recording sample interval
    binhead += struct.pack(">d",0)
    # Extended field recording samples per trace
    binhead += struct.pack(">I",0)
    # Extended ensemble fold
    binhead += struct.pack(">I",0)
    # An integer constant - see format doc
    binhead += struct.pack(">I",16909060)
    # 200 unassigned bytes
    for i in range(25):
        binhead += struct.pack("Q",0)
    #!!! Major SEG-Y format revision number
    binhead += struct.pack(">B",2)
    #!!! Minor SEG-Y format revision number
    binhead += struct.pack(">B",0)
    #!!! Fixed length trace flag, 1 is yes - see format doc
    binhead += struct.pack(">H",1)
    # Number of extended text file headers
    binhead += struct.pack(">H",0)
    # Number of additional trace headers
    binhead += struct.pack(">I",0)
    # Time basis code, 4 is UTC
    binhead += struct.pack(">H",4)
    #!!! Number of traces in file
    binhead += struct.pack(">Q",ntrace)
    # Byte offset of first trace
    binhead += struct.pack(">Q",0)
    # Number of data trailer stanza records
    binhead += struct.pack(">I",0)
    # 68 unassigned bytes
    for i in range(17):
        binhead += struct.pack(">I",0)

    return binhead

def build_trchead(i):
    # i - trace number
    trchead = b''
    # Trace sequence number within line
    trchead += struct.pack(">I",0)
    # Trace sequence number within file - starts at 1
    trchead += struct.pack(">I",i)
    # Original field record number
    trchead += struct.pack(">I",0)
    # Trace number in original field record
    trchead += struct.pack(">I",0)
    # Energy source point number
    trchead += struct.pack(">I",0)
    # Ensemble number
    trchead += struct.pack(">I",0)
    # Trace number within ensemble
    trchead += struct.pack(">I",0)
    # Trace ID code, 1 is time domain
    trchead += struct.pack(">H",1)
    # Number of vertically summed traces
    trchead += struct.pack(">H",0)
    # Number of horizontally stacked traces (stacking??)
    trchead += struct.pack(">H",0)
    # Data use, 1 is production
    trchead += struct.pack(">H",1)
    # Distance from center of source point to center of rx group
    trchead += struct.pack(">I",0)
    # Elevation of rx group
    trchead += struct.pack(">I",0)
    # Surface elevation at source location
    trchead += struct.pack(">I",0)
    # Source depth below surface
    trchead += struct.pack(">I",0)
    # Seismic datum elevation at rx group
    trchead += struct.pack(">I",0)
    # Seismic datum elevation at source
    trchead += struct.pack(">I",0)
    # Water column height at source location
    trchead += struct.pack(">I",0)
    # Water column height at rx group location
    trchead += struct.pack(">I",0)
    # Scalar to be applied to last seven fields for real val - see format doc
    trchead += struct.pack(">H",1)
    # Scalar to be applied to four following fields for real val - see format doc
    trchead += struct.pack(">H",1)
    # Source X coord
    trchead += struct.pack(">I",0)
    # Source Y coord
    trchead += struct.pack(">I",0)
    # rx group X coord
    trchead += struct.pack(">I",0)
    # rx group Y coord
    trchead += struct.pack(">I",0)
    # Coordinate units, 3 is decimal degrees
    trchead += struct.pack(">H",3)
    # Weathering velocity
    trchead += struct.pack(">H",0)
    # Subweathering velocity
    trchead += struct.pack(">H",0)
    # Uphole time at source in ms
    trchead += struct.pack(">H",0)
    # Uphole time at group in ms
    trchead += struct.pack(">H",0)
    # Source static correction in ms
    trchead += struct.pack(">H",0)
    # Group static correction in ms
    trchead += struct.pack(">H",0)
    # Total static correction applied in ms
    trchead += struct.pack(">H",0)
    # Lag time A
    trchead += struct.pack(">H",0)
    # Lag time B
    trchead += struct.pack(">H",0)
    #  Delay recording time
    trchead += struct.pack(">H",0)
    # Mute time start in ms
    trchead += struct.pack(">H",0)
    # Mute time stop in ms
    trchead += struct.pack(">H",0)
    # Samples in this trace
    trchead += struct.pack(">H",0)
    # Sample interval for this trace
    trchead += struct.pack(">H",0)
    # Gain type of field instruments
    trchead += struct.pack(">H",0)
    # Instrument gain constant
    trchead += struct.pack(">H",0)
    # Instrument early or initial gain
    trchead += struct.pack(">H",0)
    # Correlated, 2 is yes
    trchead += struct.pack(">H",2)
    # Sweep freq start Hz
    trchead += struct.pack(">H",0)
    # Sweep freq end Hz
    trchead += struct.pack(">H",0)
    # Sweep length ms
    trchead += struct.pack(">H",0)
    # Sweep type, 1 is linear
    trchead += struct.pack(">H",1)
    # Sweep trace taper length start ms
    trchead += struct.pack(">H",0)
    # Sweep trace taper length end ms
    trchead += struct.pack(">H",0)
    # Taper type
    trchead += struct.pack(">H",0)
    # Alias filter freq Hz
    trchead += struct.pack(">H",0)
    # Alias filter slope
    trchead += struct.pack(">H",0)
    # Notch filter freq Hz
    trchead += struct.pack(">H",0)
    # Notch filter flope
    trchead += struct.pack(">H",0)
    # Low-cut freq Hz
    trchead += struct.pack(">H",0)
    # Hi-cut freq Hz
    trchead += struct.pack(">H",0)
    # Low-cut slope
    trchead += struct.pack(">H",0)
    # Hi-cut slope
    trchead += struct.pack(">H",0)
    # Year data recorded
    trchead += struct.pack(">H",0)
    # Day of year data recorded
    trchead += struct.pack(">H",0)
    # Hour of day
    trchead += struct.pack(">H",0)
    # Minute of hour
    trchead += struct.pack(">H",0)
    # Second of minute
    trchead += struct.pack(">H",0)
    # Time basis code
    trchead += struct.pack(">H",0)
    # Trace weighting factor
    trchead += struct.pack(">H",0)
    # Geophone group number of roll switch position one
    trchead += struct.pack(">H",0)
    # Geophone group number of trace number one within original field record
    trchead += struct.pack(">H",0)
    # Geophone group number of last trace within original field record
    trchead += struct.pack(">H",0)
    # Gap size
    trchead += struct.pack(">H",0)
    # Over travel assoc with taper at beginning of line
    trchead += struct.pack(">H",0)
    # X coordinate of ensemble position of this trace
    trchead += struct.pack(">I",0)
    # Y coordinate of ensemble position of this trace
    trchead += struct.pack(">I",0)
    # Line number (inline  number)
    trchead += struct.pack(">I",1)
    # Ensemble number (crossline number)
    trchead += struct.pack(">I",i)
    # Shotpoint number
    trchead += struct.pack(">I",0)
    # Scalar to be applied to shotpoint number
    trchead += struct.pack(">H",0)
    # Trace units, 0 is unknown
    trchead += struct.pack(">H",0)
    # Transduction constant
    trchead += struct.pack(">I",0)
    trchead += struct.pack(">H",0)
    # Transduction units
    trchead += struct.pack(">H",0)
    # Device/Trace identifier 
    trchead += struct.pack(">H",0)
    # Scalar to be applied to uphole, static, and group corrections 
    trchead += struct.pack(">H",0)
    # Source type/orientation
    trchead += struct.pack(">H",0)
    # Source energy direction wrt orientation
    trchead += struct.pack(">H",0)
    trchead += struct.pack(">H",0)
    trchead += struct.pack(">H",0)
    # Source measurement
    trchead += struct.pack(">I",0)
    trchead += struct.pack(">H",0)
    # Source measurement unit
    trchead += struct.pack(">H",0)
    # Zero
    trchead += struct.pack(">Q",0)

    return trchead

def main():
    # Assumptions
    spt = 3600 #samples per trace

    data_path = "./s_01294501_rgram.img"
    nav_path = "./s_01294501_geom.tab"
    out_path = "./s_01294501_segy.sgy"

    # Load data
    data = np.fromfile(data_path, dtype="float32")
    if(len(data)/spt != len(data)//spt):
        print("Does trace length = {} samples??".format(spt))
        sys.exit()
    ntrace = len(data)//spt
    data = np.reshape(data, (spt, ntrace))
    data = np.transpose(data).copy(order='C') # This makes the traces C-contiguous

    # Load nav
    # nav stuff here

    # Build Segy 2.0 format file
    # https://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev2_0-mar2017.pdf
    with open(out_path,'wb') as f:
        ### Write 3200 byte text header - maybe add actual text??
        txthead = b''
        for i in range(400):
            txthead += struct.pack("Q",0)

        f.write(txthead)

        ### Write 400 byte binary header
        f.write(build_binhead(spt, ntrace))

        ### Write data traces
        for i in range(ntrace):
            f.write(build_trchead(i+1))
            trace = data[i,:]
            trcbin = b''
            for i in range(len(trace)):
                trcbin += struct.pack('>f',trace[i])
            f.write(trcbin)
main()