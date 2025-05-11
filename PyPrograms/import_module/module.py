
def find_index(args,object):
    '''
    function to find the index of an object in a list
    '''
    ret_value = 0
    for index,args in enumerate(args):
        if args is object:
            ret_value=1
            print(index)
    if(ret_value==0):
        print('Object not found!')

