from useful_methods import rpn_calc, get_input


if __name__ == '__main__':
    rpn = '3 4 2 * 1 5 - 2 3 ^ ^ / +'
    print( 'For RPN expression: %r\n' % rpn )
    rp = rpn_calc(get_input(rpn))
    maxcolwidths = [max(len(y) for y in x) for x in zip(*rp)]
    row = rp[0]
    print( ' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
    for row in rp[1:]:
        print( ' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
 
    print('\n The final output value is: %r' % rp[-1][2])
