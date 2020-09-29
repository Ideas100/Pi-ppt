import os
import sys
import shutil

options = ['--init', '--help']

def create_directory(path):
    try:
        os.makedirs(path)
    except OSError:
        print('mkdir failed, check whether directory exists')
        sys.exit()

def copy_files(source, destination, path):
    dir_, file_ = os.path.split(__file__)
    src = os.path.join(dir_,'../data', source)
    des = os.path.join(path, destination)
    shutil.copyfile(src, des)

    
def pippt_init(slide_name):
    path = os.getcwd() + '/' + slide_name
    create_directory(path + '/images')
    create_directory(path + '/code')
    copy_files('image.dat', 'image.png', path + '/images')
    copy_files('code.dat', 'code.c', path + '/code')
    copy_files('sample.dat', slide_name + '.py', path)
    
def pippt_help():
    print('Usage: pi-ppt [OPTIONS] <slide_name>')
    print('')
    print('  pi-ppt: A simple presentation module')
    print('')
    print('Options:')
    print('  --init  Creates a sample format for the pi-ppt')
    print('  --help  Short description on pi-ppt module')

def pippt_usage():
    print('Error: Missing arguments for pi-ppt')
    print('')
    print('Try "pi-ppt --help" for help')
    
    
# main function
def main():
    if len(sys.argv) < 2:
        pippt_usage()
        sys.exit()

    if sys.argv[1] == options[0] and len(sys.argv) == 3:
        pippt_init(sys.argv[2])
    elif sys.argv[1] == options[1]:
        pippt_help()
    else:
        pippt_usage()
        
if __name__=='__main__':
    main()
