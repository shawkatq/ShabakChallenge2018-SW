
from datetime import datetime
from datetime import timedelta
import csv
import operator
from multiprocessing import Process,freeze_support

# the known suspects uids
susp = ['2449'
        ,'6796'
        ,'9237'
        ,'4024'
        ,'3538'
        ,'3608'
        ,'7239'
        ,'435'
        ,'5206'
        ,'2211']

moreSusp = []

urlDict = {}
urlDictIndex = 0

usrDict = {}
usrDict2 = {}

# split the log file into two files, log1 for the known suspects, log2 for the others, and replace the urls with ids to make the files smaller.
def sort_split_replace():
    urlDictIndex = 0
    with open('log1no.csv', mode='w') as log1:
        log1_writer = csv.writer(log1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('log2no.csv', mode='w') as log2:
            log2_writer = csv.writer(log2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open('log.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    line_count+=1
                    if line_count % 1000000 == 0:
                        print(line_count)
                    if line_count != 1:
                        if len(row)>4:
                            row[3] = ",".join(row[3:])
                            del row[4:]
                        # convert url to number 
                        if row[3] in urlDict:
                            row[3] = urlDict[row[3]]
                        else:
                            urlDictIndex+=1
                            urlDict[row[3]] = urlDictIndex
                            row[3] = urlDictIndex
                        

                        # process date
                        d = datetime.strptime(row[2], "%m/%d/%Y %H:%M")
                        row.append(d.day)
                        row.append(d.hour)
                        row.append(d.minute)

                        # delete 
                        del row[2:4]

                        # write the row in the right file
                        if row[0] in susp:
                            log1_writer.writerow(row)
                        else:
                            log2_writer.writerow(row)
                        
                print(line_count)
    log1.close()
    log2.close()
    csv_file.close()

            
# build a victor of the number of activites on each day for each user. and search for the uniqe activities pattern.
def checkDays():
    with open('log2no.csv') as log2:
        log2_reader = csv.reader(log2, delimiter=',')
        for row in log2_reader:
            # if user found
            if row[0] in usrDict2:
                usrDict2[row[0]][int(row[2])-1] += 1
            else:
                days = []
                for d in range(0,31):
                    days.append(0)
                usrDict2[row[0]] = days
                usrDict2[row[0]][int(row[2])-1] = 1
    log2.close()

    for usr in usrDict2:
        days = 0
        for d in range(0,31):
            if usrDict2[usr][d] > 100:
                days += 1
                if(days > 2):
                    # print(usr)
                    moreSusp.append(usr)
                    break


# find the most used ips for the new suspects
userIps2 = {}
usersMaxIp2 = {}
def searchForMustUsedIp():
    with open('log2no.csv') as log2:
        log2_reader = csv.reader(log2, delimiter=',')
        for row in log2_reader:
            # if user found
            if row[0] in userIps2:
                if row[1] in userIps2[row[0]]:
                    userIps2[row[0]][row[1]] += 1
                else:
                    userIps2[row[0]][row[1]] = 1
            else:
                userIps2[row[0]] = {}
                userIps2[row[0]][row[1]] = 1
    log2.close()
    #  print max used ip for each user
    
    for u in userIps2:
        maxIpCnt = 0
        maxIp = ''
        for ip in userIps2[u]:
            if maxIpCnt < userIps2[u][ip]:
                maxIpCnt = userIps2[u][ip]
                maxIp = ip
        usersMaxIp2[u] = maxIp
        if u in (moreSusp):
            print(u + ' ' + maxIp)


sort_split_replace()
checkDays()
searchForMustUsedIp()