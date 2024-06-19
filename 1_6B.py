import csv, logging, datetime


lst  = ['1.csv','2.csv','3.csv','4.csv','5.csv']

timestring = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
logfile = '1_6B' + timestring + '.log'
logging.basicConfig(filename=logfile, level=logging.INFO,format='%(asctime)s_%(levelname)s: %(message)s')
logging.info('Копирование файла успешно завершено')
logging.error('Файл не обнаружен')
new_file = timestring + "new_file.csv"
for i in lst:
    try:
        with open(i, 'r') as fl:
            reader = csv.reader(fl)
            row = list(reader)
            with open(new_file, 'a') as nf:
                csv.writer(nf).writerows(row)
            logging.info(i)

    except FileNotFoundError:
        print('Файл ', i, 'не найден.')
        logging.error(i)

