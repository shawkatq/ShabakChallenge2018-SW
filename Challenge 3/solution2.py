
from datetime import datetime
from datetime import timedelta
import csv
from multiprocessing import Process,freeze_support

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

urlDict = {}
urlDictIndex = 0

usrDict = {}
usrDict2 = {}


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
                            #  row.append(urlDict[row[3]])
                            row[3] = urlDict[row[3]]
                        else:
                            urlDictIndex+=1
                            urlDict[row[3]] = urlDictIndex
                            # row.append(urlDictIndex)
                            row[3] = urlDictIndex
                        
                        # delete 
                        del row[3]

                        # write the row in the right file
                        if row[0] in susp:
                            # row.append('bad')
                            log1_writer.writerow(row)
                        else:
                            # row.append('na')
                            log2_writer.writerow(row)
                        
                print(line_count)
    log1.close()
    log2.close()
    csv_file.close()
    with open('urls_do.csv', mode='w') as urld:
        urld_writer = csv.writer(urld, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for url in urlDict:
            urld_writer.writerow([url, urlDict[url]])
            

def buildUserVictor():
    with open('log2no.csv') as log2:
        log2_reader = csv.reader(log2, delimiter=',')
        for row in log2_reader:
            # if user found
            if row[0] in usrDict2:
                usrHistory = usrDict2[row[0]]
                # if url found
                if row[1] in usrHistory:
                    usrHistory[row[1]]+=1
                else:
                    usrHistory[row[1]]=1
            else:
                usrDict2[row[0]] = {}
                usrDict2[row[0]][row[1]] = 1
    log2.close()

    with open('log2noc.csv', mode='w') as log2noc:
        log2noc_writer = csv.writer(log2noc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for usr in usrDict2:
            userVictor = [usr]
            for url in urlDict:
                urlid = str(urlDict[url])
                if urlid in usrDict2[usr]:
                    userVictor.append(usrDict2[usr][urlid])
                else:
                    userVictor.append(0)
            log2noc_writer.writerow(userVictor)
    log2noc.close()

usersMaxIpChunk = {}

usersActivity = {}
def searchForTimePattern(start,end):
    with open('log2no.csv') as log2:
        log2_reader = csv.reader(log2, delimiter=',')
        for row in log2_reader:
            if row[0] in usersActivity:
                usersActivity[row[0]].append(row[2])
            else:
                usersActivity[row[0]] = []
                usersActivity[row[0]].append(row[2])

    with open('log-user-activity-vetcor.csv', mode='w') as lognoc:
        lognoc_writer = csv.writer(lognoc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for u in usersActivity:
            userVictor = [u]
            usersActivity[u].sort()
            for ai in range(0,len(usersActivity[u])):
                userVictor.append(usersActivity[u][ai])
            lognoc_writer.writerow(userVictor)

    # this part can be parallelized to different processes to boost performance
    n = 0
    r = []
    with open('log-user-activity-vetcor.csv') as log2:
        log2_reader = csv.reader(log2, delimiter=',')
        print(str(datetime.now()) + '  checking #' + str(n))
        for row in log2_reader:
            n+=1
            if(n%1000 == 0):
                print(str(datetime.now()) + '  checking #' + str(n))
            u = row[0]
            us = []
            for i in range(1,len(row)):
                us.append(datetime.strptime(row[i], "%m/%d/%Y %H:%M"))

            f = False
            for t in range(start,end):
                if(f == True):
                    break
                for i in range(0,len(us)):
                    nxt = us[i] + timedelta(seconds=t*60)
                    l = 0
                    while nxt in us:
                        l += 1
                        nxt = nxt + timedelta(seconds=t*60)
                        if l > 50:
                            break
                    if l > 50:
                        print ('p1: ' + str(t) + ' ' + u)
                        f = True
                        r.append(u)
                        break
    
    with open('results.csv', mode='w') as rs:
        rsw = csv.writer(rs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for result in r:
            rsw.writerow([result])

sort_split_replace()
searchForTimePattern(1,16)