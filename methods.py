import re


def follow(x, lis):
    if (x in lis):
        y = lis.index(x)
        return lis[y + 1]
    else:
        return "Not in list"

def casing(y, test1):
    newstr = " "
    for x in y:
        # if (test1.find(x) != -1):
        #     newstr += x + " "
        if (test1.find(x) != -1) and (x == "Open Hole"):
            count = test1.count(x)
            i = 0
            while (i < count):
                i += 1
                indx = test1.find(x)
                if(indx == -1 ):
                    break
                test2 = test1[indx:]
                m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
                z = test2.index(m) + len(m)
                newstr += test2[:z] + " "
                test1 = test1[0:indx] + test1[indx + z:]
    return newstr

def getName(str_list):
    end = str_list.find("Report Printed")
    new_str = str_list[9:end]
    return new_str

def comment(y, test1):
    newstr = " "
    for x in y:
        if (test1.find(x) != -1):
            count = test1.count(x)
            i = 0
            while (i < count):
                i += 1
                indx = test1.find(x)
                if (indx == -1):
                    break
                test2 = test1[indx:]
                if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
                    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
                    z = test2.index(m) + len(m)
                    newstr += test2[:z] + " "
                    test1 = test1[0:indx] + test1[indx + z:]
    return newstr


def frac_Date(y, test1):
    fracstr = " "
    for x in y:
        if (test1.find(x) != -1):
            count = test1.count(x)
            i = 0
            while (i < count):
                i += 1
                indx = test1.find(x)
                if (indx == -1):
                    break
                test2 = test1[indx:]
                if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
                    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
                    z = test2.index(m) + len(m)
                    fracstr += m + " "
                    test1 = test1[0:indx] + test1[indx + z:]
    return fracstr

def open_hole(y, test1):
    openstr = " "
    for x in y:
        if (test1.find(x) != -1):
            count = test1.count(x)
            i = 0
            while (i < count):
                i += 1
                indx = test1.find(x)
                if (indx == -1):
                    break
                test2 = test1[indx +len(x):]
                test3 = test1[indx + len(x)+ 1:]
                #print(test3)
                for j in test3:
                    if(j == ";"):
                        getindex = test3.find(j)
                        #print(getindex)
                if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
                    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
                    z = test2.index(m) + len(m)
                    openstr += test2[1:1 + getindex] + " "
                    #print(openstr)
                    test1 = test1[0:indx] + test1[indx + z:]
    return openstr

def ifperf(y, test1, boox):
    for x in y:
        if (test1.find(x) != -1):
                indx = test1.find(x)
                if (indx == -1):
                    break
                boox = 'True'
    return boox

def perf(y, test1):
    newstr = " "
    for x in y:
        if (test1.find(x) != -1):
            count = test1.count(x)
            i = 0
            while (i < count):
                i += 1
                indx = test1.find(x)
                if(indx == -1 ):
                    break
                test2 = test1[indx:]
                if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
                    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
                else:
                    break
                z = test2.index(m) + len(m)
                newstr += test2[:z] + " "
                test1 = test1[0:indx] + test1[indx + z:]
    return newstr