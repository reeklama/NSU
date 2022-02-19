import random
import data
import datetime as dt
from datetime import timedelta


n_clients = 100
n_employ = 10
n_payments = 10
n_credit = 10

passport_state = 2410000000
date = [2021, 12, 22]
rates = [[0, 10, 5, 10, 1000000, 50000000], [0, 11, 2, 6, 500000, 3000000], [1, 3, 1, 3, 100000, 1000000],
         [0, 12, 1, 2, 50000, 1000000], [0, 10, 3, 8, 300000, 40000000]]
kind_pay = [[1, 0],[2,3],[3,5],[4,5]]
coin = ['false', 'true']


def create_human():
    person = []
    global passport_state
    if random.choice(coin) == 'false':
        person.append(random.choice(data.mSurname))
        person.append(random.choice(data.mname))
        person.append(random.choice(data.mPatronymic))
    else:
        person.append(random.choice(data.fSurname))
        person.append(random.choice(data.fname))
        person.append(random.choice(data.fPatronymic))
    passport_state = passport_state + random.randint(1, 10)
    person.append(str(passport_state))
    return person


def create_client():
    client_info = create_human()
    client_info.append(str(random.randint(1, 8)))
    return client_info


def create_employ(i):
    employ_info = create_human()
    employ_info.append(str(random.randint(1, 4)))
    if i > 0:
        employ_info.append(str(random.randint(1, i)))
    else:
        employ_info.append('NULL')
    return employ_info


def create_scoring():
    scoring_info = [str(random.randint(1, n_clients)), str(random.randint(1, n_employ)), str(random.choice(coin))]
    return scoring_info


def create_aproved():
    rate = random.randint(0, 4)

    date1 = str(date[0] + random.randint(1, 5))
    date1 = str(date1)
    date2 = (date[1] + random.randint(1, 12)) % 12
    if date2 == 0:
        date2 = '01'
    elif date2 < 10:
        date2 = '0' + str(date2)
    else:
        date2 = str(date2)
    date3 = (date[2] + random.randint(1, 30)) % 30
    if date3 == 0:
        date3 = '01'
    elif date3 < 10:
        date3 = '0' + str(date3)
    else:
        date3 = str(date3)

    aproved_info = [str(rate + 1), date1 + date2 + date3, str(int((rates[rate][4] * (1 / (rate + 1) + 1) *
                                                                   100) / 100)),
                    str(rates[rate][5] // (1 / (rate + 1) + 1))]
    return aproved_info


def main():
    clients = []
    employ = []
    scoring = []
    aproved = []
    loans = []
    time = []
    sheduledate = []
    shedulescore = []
    dates_payments = []
    mainsum=[]
    procsum=[]
    f1 = open('clients.txt', 'w')
    f2 = open('employ.txt', 'w')
    f3 = open('scoring.txt', 'w')
    f4 = open('aproved.txt', 'w')
    f5 = open('loans.txt', 'w')
    f6 = open('balance.txt', 'w')
    f7 = open('shedule.txt', 'w')
    f8 = open('payments.txt', 'w')
    for i in range(n_clients):
        clients.append(create_client())
        f1.write(
            "('" + clients[i][0] + "', '" + clients[i][1] + "', '" + clients[i][2] + "', '" + clients[i][3] + "', '"
            + clients[i][4] + "')," + '\n')

    for i in range(n_employ):
        employ.append(create_employ(i))
        f2.write("('" + employ[i][0] + "', '" + employ[i][1] + "', '" + employ[i][2] + "', '" + employ[i][3] + "', '"
                 + employ[i][4] + "', '" + employ[i][5] + "')," + '\n')

    for i in range(n_clients):
        scoring.append(create_scoring())
        f3.write("('" + scoring[i][0] + "', '" + scoring[i][1] + "', " + scoring[i][2] + ")," + '\n')

    j = 0
    for i in range(n_clients):
        if scoring[i][2] == 'true':
            aproved.append(create_aproved())
            f4.write(
                "('" + str(i + 1) + "', '" + aproved[j][0] + "', '" + aproved[j][1] + "', '" + aproved[j][2] + "', '" +
                aproved[j][3] + "')," + '\n')
            j = j + 1

    for i in range(len(aproved)):

        date2 = random.randint(1, 12)
        if date2 < 10:
            date2 = '0' + str(date2)
        else:
            date2 = str(date2)
        date3 = random.randint(1, 30)
        if date3 < 10:
            date3 = '0' + str(date3)
        else:
            date3 = str(date3)

        fin = aproved[i][1][0] + aproved[i][1][1] + aproved[i][1][2] + str(
            int(aproved[i][1][3]) - random.randint(0, 1)) + aproved[i][1][4] + aproved[i][1][5] + aproved[i][1][6] + \
              aproved[i][1][7]
        fon = str(2018 + (i % 3)) + date2 + date3

        t1 = dt.date(int(fin[0] + fin[1] + fin[2] + fin[3]), int(fin[4] + fin[5]), int(fin[6] + fin[7]))
        t2 = dt.date(int(fon[0] + fon[1] + fon[2] + fon[3]), int(fon[4] + fon[5]), int(fon[6] + fon[7]))

        t3 = t1 - t2
        time.append(t3)

        loans.append([str(aproved[i][3]), fon,
                      fin])
        f5.write("('" + str(i + 1) + "', '" + loans[i][0] + "', '" + loans[i][1] + "', '" + loans[i][2] + "')," + '\n')

    for i in range(len(loans)):
        pcount = int(time[i].days) // 30
        loans[i][0] = loans[i][0].replace('.0', '')
        sum = int(loans[i][0])
        start = dt.date(int(loans[i][1][0] + loans[i][1][1] + loans[i][1][2] + loans[i][1][3]),
                        int(loans[i][1][4] + loans[i][1][5]), int(loans[i][1][6] + loans[i][1][7]))
        print(start)

        date_payment = dt.date(int(loans[i][1][0] + loans[i][1][1] + loans[i][1][2] + loans[i][1][3]),
                        int(loans[i][1][4] + loans[i][1][5]), int(loans[i][1][6] + loans[i][1][7]))
        procsum.append([i])
        sheduledate.append([i])
        shedulescore.append([i])
        dates_payments.append([i])
        mainsum.append([i])
        for k in range(pcount):

            proc = sum * (int(aproved[i][0]) / 100)
            o = sum // (pcount - k)
            platez = round(o + proc)
            start = start + timedelta(days=30 + (k % 2))
            date_payment = start + timedelta(days=random.randint(-2, 29))
            mainsum[i].append(sum)
            procsum[i].append(round(proc))
            sum = sum - platez
            dates_payments[i].append(date_payment)
            sheduledate[i].append(start)
            shedulescore[i].append(platez)
            s1 = str(start)
            s2 = s1[0]+s1[1]+s1[2]+s1[3]+s1[5]+s1[6]+s1[8]+s1[9]
            f7.write("('" + str(i + 1) + "', '" + s2 + "', '" + str(platez) + "')," + '\n')
    for i in range(len(sheduledate)):
        finesum = 0
        for k in range(len(sheduledate[i])):
            if k == 0:
                continue
            a = (sheduledate[i][k])
            print(dates_payments[i][k])
            way = random.randint(1,4)
            if dates_payments[i][k] < sheduledate[i][k]:
                finesum = int(shedulescore[i][k]) * 1 / 10
            s3 = str(dates_payments[i][k])
            s4 = s3[0] + s3[1] + s3[2] + s3[3] + s3[5] + s3[6] + s3[8] + s3[9]
            f8.write("('" + str(i + 1) + "', '" + str(shedulescore[i][k] + procsum[i][k]) + "', '" + s4 + "', '"
                     + str(way) + "')," + '\n')
            f6.write("('" + str(i + 1) + "', '" + str(mainsum[i][k]) + "', '" + str(procsum[i][k]) + "', '"
                     + str(finesum) + "')," + '\n')

if __name__ == '__main__':
    main()
