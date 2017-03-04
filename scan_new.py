"""
scan double beta and single electron events

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
import argparse
import os
import pickle


def scan_inp():
    """
    parse input pvalues
    """
    
#    parse input arguments for analysis 

    parser = argparse.ArgumentParser()
    parser.add_argument("-file_type", type=str, help="file type: signal/background/mixed",
                        default='signal',dest='f_type')
    parser.add_argument("-scan_type", type=str, help="scan type: blind/true",
                        default='blind',dest='scan_type')
    parser.add_argument("-star", type=int, help="first event",
                        default=0,dest='first_ev')
    parser.add_argument("-class_file", type=str, help="classfication file",
                        default='class.res',dest='class_file')
    
    ar = parser.parse_args()
    
    print '---------------------------------------------------------------------'
    print '  files to analyze               ',ar.f_type
    print '  scan type                      ',ar.scan_type
    print '  First event                    ',ar.first_ev
    if ar.scan_type == 'blind':
        print '  Classification file            ',ar.class_file
    print '---------------------------------------------------------------------'
    
    return ar.f_type, ar.scan_type, ar.first_ev, ar.class_file



#
# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

f_type, scan_type, first_ev, class_file = scan_inp()

filelist ={
      'signal': 'double_beta_files',
      'background': 'single_electron_files',
      'mixed': 'randomized_files'
       }

nlist = pickle.load( open('nexus_'+filelist[f_type], "rb" ) )

debug = True
evt = 0

if scan_type == 'blind':
    classified_files = open(class_file,"a")
    
for file in nlist[first_ev:]:

    if scan_type != 'blind':
        print '   Scanning file ', file

    table = np.loadtxt(file);
 
    x = table[:,1];
    y = table[:,2];
    z = table[:,3];
    E = table[:,4];
    print "Found {0} voxels".format(len(x));

    fig = plt.figure(figsize=(20,10))

    ax3 = fig.add_subplot(111, projection='3d');

    psize = 5000*E 
    s3 = ax3.scatter(x,y,z,s=psize)

    if scan_type != 'blind':
        ax3.plot([x[0]],[y[0]],[z[0]],'o',color='blue',markersize=5);
        ax3.plot([x[-1]],[y[-1]],[z[-1]],'s',color='blue',markersize=5);

    ax3.set_xlabel("x (mm)");
    ax3.set_ylabel("y (mm)");
    ax3.set_zlabel("z (mm)");

    lb_x = ax3.get_xticklabels();
    lb_y = ax3.get_yticklabels();
    lb_z = ax3.get_zticklabels();
    for lb in (lb_x + lb_y + lb_z):
         lb.set_fontsize(8);
    plt.show();
#==============================================================================
#  
#     classif = input("  classify 0(single el) - 10(double el)\n")
#     print classif
#     cl = "   {0} \n".format(classif)
#     fout = file + cl
#     classified_files.write(fout)
# 
# 
#==============================================================================



