
import random
import pickle
import glob


def write_file_list(file,list):
    wf = open(file,"w")	
    pickle.dump(list, wf)
    wf.close()
 
    """
    create list signal/background events files
    based on the population of files in 'data' directories 
    """
    
mct_s = glob.glob('data/single_electron/mct*')
mct_d = glob.glob('data/double_beta/mct*')

mct_s = glob.glob('data/nexus/Background/*lis_ev*')
mct_d = glob.glob('data/nexus/zeronubb/*lis_ev*')
		
filelist = mct_s + mct_d
random.shuffle(filelist)


write_file_list('nexus_single_electron_files',mct_s)
write_file_list('nexus_double_beta_files',mct_d)
write_file_list('nexus_randomized_files',filelist)


	
		