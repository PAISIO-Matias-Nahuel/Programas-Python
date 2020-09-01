import logging
logging.basicConfig(filename =r'D:\programas_python\error_log',
                    level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


logging.debug('start of program')

def factorial(n):
    logging.debug('start of factorial(%s)')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i ,total))

    logging.debug('return value is %s' % (total))
    return total
print(factorial(5))

logging.debug('end of program')
