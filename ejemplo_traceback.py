import traceback
try:
    raise Exception('This is the error message.')

except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the Traceback info was written in error_log.txt')
