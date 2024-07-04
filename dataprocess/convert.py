import json
import random

if __name__ == '__main__':
    file_Convert = "/public/zs/npc/convert_dataset/"
    fileo_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3_origin.json"
    file0_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-1_style_based_fake.json"
    file1_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-2_content_based_fake.json"
    file2_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-3_integration_based_fake_tn200.json"
    file3_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-4_story_based_fake.json"
    
    file4_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-4_story_based_fake.json"

    file5_path = "/home/yangxiaofan/machine/FakingFakeNews-master/data/gossipcop_v3-7_integration_based_legitimate_tn300.json"
    # file_path = "/public/zs/npc/fakenews/gossipcop_v3-1_style_based_fake.json"
    # file_train_convert = file_Convert+file_path.split(".")[0].split('/')[-1]+"_"+"train_convert.txt"

    fileo_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/traino.jsonl"
    file0_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train0.jsonl"
    file1_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train1.jsonl"
    file2_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train2.jsonl"
    file3_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train3.jsonl"
    file4_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train4.jsonl"
    file5_train_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/train5.jsonl"


    # file_test_convert = file_Convert+file_path.split(".")[0].split('/')[-1]+"_"+"test_convert.txt"
    fileo_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/testo.jsonl"
    file0_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test0.jsonl"
    file1_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test1.jsonl"
    file2_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test2.jsonl"
    file3_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test3.jsonl"
    file4_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test4.jsonl"
    file5_test_convert = "/home/yangxiaofan/machine/FakingFakeNews-master/data/test5.jsonl"

    #在下面选择打开哪个文件
    with open(fileo_path, 'r', encoding='utf-8') as file:
        # 使用json.load()方法解析JSON数据
        ids = json.load(file)
    count = 0
    print(len(ids))
    list_number = range(0,len(ids)-1)
    print(list_number)
    test_number = int(len(ids)*0.3)
    train_number = len(ids) - test_number
    print(test_number)
    print(train_number)
    # print(random.sample(list_number,int(len(ids)*0.3)))
    print(type(ids))
    id_tests = random.sample(list(ids),test_number)
    # id_trains = random.sample(list(ids),train_number)
    # id_trains = list_number[id_tests,:]
    print(id_tests)
    count =0
    origin_text1=""
    origin_label1=""
    origin_text2=""
    origin_label2=""
    origin_text=""
    origin_label=""
    dic1 = {"txt":"","label":bool}
    dic2 = {"txt": "", "label": bool}
    for id in ids:
        # if file0_path == "/public/zs/npc/fakenews/gossipcop_v3-3_integration_based_fake_tn200.json" or file5_path == "/public/zs/npc/fakenews/gossipcop_v3-7_integration_based_legitimate_tn300.json":
        #     dic1["txt"] = ids[id]['doc_1_text']
        #     # dic1["label"] = ids[id]['doc_1_label']
        #     if ids[id]['doc_1_label'] == "fake":
        #         dic1["label"] = False
        #     else:
        #         dic1["label"] = True
        #     if ids[id]['doc_2_label'] == "fake":
        #         dic2["label"] = False
        #     else:
        #         dic2["label"] = True
        #     dic2["txt"] = ids[id]['doc_2_text']
            # dic2["label"] = ids[id]['doc_2_label']
            # origin_text1 = "{"+ids[id]['doc_1_text']+"}"
            # origin_label1 = "{"+ids[id]['doc_1_label']+"}"
            # origin_text2 = "{"+ids[id]['doc_2_text']+"}"
            # origin_label2 = "{"+ids[id]['doc_2_label']+"}"

        #0145可以下面这个
        # dic1["txt"] = ids[id]['origin_text']
        #origin可以下面这个
        dic1["txt"] = ids[id]['text']
        # dic1["label"] = ids[id]['doc_1_label']

        #0145可以下面这个
        # if ids[id]['origin_label'] == "fake":
            #origin可以下面这个
        if ids[id]['label'] == "fake":
            dic1["label"] = False
        else:
            dic1["label"] = True

        # else:
        #     dic1["txt"] = ids[id]['doc_1_text']
        #     if ids[id]['doc_1_label'] == "fake":
        #         dic1["label"] = False
        #     else:
        #         dic1["label"] = True
            # dic1["label"] = ids[id]['doc_1_label']
        print(dic1)
        print(dic1["label"])
        print(dic2)
        print(dic2["label"])
        # break
        flag = True
        for name in id_tests:
            if name==id:
                #在下面选择打开哪个文件
                with open(fileo_test_convert, "a", encoding='utf-8') as f:
                    json.dump(dic1, f,ensure_ascii=False)
                    f.write('\n')
                    if dic2["txt"]!="":
                        json.dump(dic2, f,ensure_ascii=False)
                        f.write('\n')
                count= count+1
                flag = False
                break
                # with open(file5_test_convert, 'a', encoding='utf-8') as file:
                #     file.write(origin_label1+"\t" + origin_text1.replace("\n", " "))
                #     file.write("\n")
                #     file.write(origin_label2+"\t" + origin_text2.replace("\n", " "))
                #     # file.write(origin_label + "\t" + origin_text.replace("\n", " "))
                #     file.write("\n")
                # count= count+1
                # flag = False
                # break
        if flag == True:
            #在下面选择打开哪个文件
            with open(fileo_train_convert, "a", encoding='utf-8') as f:
                json.dump(dic1, f, ensure_ascii=False)
                f.write('\n')
                if dic2["txt"] != "":
                    json.dump(dic2, f, ensure_ascii=False)
                    f.write('\n')
        # break
            # with open(file5_train_convert,'a',encoding = 'utf-8') as file:
            #     file.write(origin_label1+"\t" + origin_text1.replace("\n", " "))
            #     file.write("\n")
            #     file.write(origin_label2+"\t" + origin_text2.replace("\n", " "))
            #     # file.write(origin_label+"\t"+origin_text.replace("\n"," "))
            #     file.write("\n")
    print(count)
        # print(id)
    # print(id_trains)

    # 打印解析后的Python对象
    # for id in ids:
    #     origin_text = "{"+ids[id]['origin_text']+"}"
    #     origin_label = "{"+ids[id]['origin_label']+"}"
    #     print(origin_text+"\n"+origin_label)
    #     if count < 3000:
    #         with open(file1_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     # break
    #     if count<15000and count >= 13000:
    #         with open(file1_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     else:
    #         with open(file1_train_convert, 'a', encoding='utf-8') as file:
    #             file.write(origin_label + "\t" + origin_text.replace("\n", " "))
    #             file.write("\n")
    #     count= count + 1


    # print(file_test_convert)
    # print(file_train_convert)
    # print(file_convert)
    # 打开文件并读取内容
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     # 使用json.load()方法解析JSON数据
    #     ids = json.load(file)
    # count = 0
    # print(len(ids))
    # # 打印解析后的Python对象
    # for id in ids:
    #     origin_text = "{"+ids[id]['origin_text']+"}"
    #     origin_label = "{"+ids[id]['origin_label']+"}"
    #     print(origin_text+"\n"+origin_label)
    #     if count < 3000:
    #         with open(file_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     # break
    #     if count<15000and count >= 13000:
    #         with open(file_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     else:
    #         with open(file_train_convert, 'a', encoding='utf-8') as file:
    #             file.write(origin_label + "\t" + origin_text.replace("\n", " "))
    #             file.write("\n")
    #     count= count + 1
        # if count == 10000:
        # break


    # print(data[1])
    # print(data['name'])  # 提取name字段的值
    # print(data['age'])  # 提取age字段的值

