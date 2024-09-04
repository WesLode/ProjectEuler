sizes= [12, 17, 2, 27, 23]
uploadingStart= [2, 5, 8, 6, 2]
v= 9

def dl_object(size, startTime):
    return {
        "size": size,
        "init_size": size,
        "startTime": startTime,
        "startStatus": False,
        "endTime": startTime,
        "speed": 0,
        "status": True
    }
def solution(sizes, uploadingStart, v):
    count_object = 1
    total_object = {"payload":{}}
    ans = []        
    
    for i in range(len(sizes)):
        total_object["payload"][str(count_object)] = dl_object(sizes[i],uploadingStart[i]-min(uploadingStart))
        count_object +=1
    total_object["stillDownload"] = True
    time_now = 0
    while total_object["stillDownload"] == True and len(sizes) >0:
        check_status = False
        # check status
        simu_dl = 0
        for i in total_object["payload"]:
            if total_object["payload"][i]['status'] == True and total_object["payload"][i]["startTime"] <= time_now:
                total_object["payload"][i]["startStatus"]=True
                simu_dl = simu_dl + 1
        
        if simu_dl !=0:
            dl_speed = v/simu_dl
            for i in total_object["payload"]:
                if total_object["payload"][i]['startStatus'] == True:
                    total_object["payload"][i]['speed'] = dl_speed
                    total_object["payload"][i]['size'] = total_object["payload"][i]['size'] - dl_speed
                    total_object["payload"][i]['endTime'] = total_object["payload"][i]['endTime'] +1
                    if total_object["payload"][i]['size'] <=0 :
                        total_object["payload"][i]['status'] = False
                        total_object["payload"][i]['startStatus'] = False
                        # if (total_object["payload"][i]['size'] + dl_speed)/dl_speed <=0.5:
                        #     total_object["payload"][i]['endTime'] = total_object["payload"][i]['endTime'] -1
        
        time_now = time_now + 1

        check_dl = 0
        for i in total_object["payload"]:
            if total_object["payload"][i]['status'] == True:
                check_dl = check_dl + 1
        if check_dl == 0:    
            total_object["stillDownload"] = False
        
        print(total_object)
        if check_status == True :
            total_object["stillDownload"] = False
        
                        
    for i in total_object['payload']:
        ans.append(total_object["payload"][i]['endTime']+min(uploadingStart))


    return ans


print(solution(sizes, uploadingStart, v))
