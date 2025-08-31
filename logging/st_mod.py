
def main():
    print(f'First module name is {__name__}')

if __name__ == 'st_mod':
    main()

'''
if __name__ == '__main__':
    main()
'''
# Checks if we are running the python file from the same file itself which case its true and __name__ = __main__,
# or if the file is being run from a different module in which case its not true
# Used because sometimes we wanna run some code only when its imported or when its not
