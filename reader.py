def read_file( fname ):
    f = open( fname, 'r' )
    text = f.read()
    f.close()
    return text
def get_csv_list( fname ):
    text = read_file( fname )
    lines = text.split('\n')
    line_list = []
    for line in lines:
        line_list.append( line.split(',') )
    return line_list

if __name__ == '__main__':
    text = read_file( 'conspiracywords.csv' )
    lines = get_csv_list('conspiracywords.csv' )
    
    print text
    print '\n'
    print lines
    print '\n'
    print words
    print '\n'
