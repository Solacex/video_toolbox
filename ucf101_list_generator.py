import sys
import os

frames_path = '/home/liguangrui/ucf101-frames'
ori_train = sys.argv[1]

ori_test = 'test'+ ori_train[5:]


train_name =  [x.strip().split(' ')[0] for x in open(ori_train)]
train_label = [x.strip().split(' ')[1] for x in open(ori_train)]
test_name =   [x.strip().split(' ')[0] for x in open(ori_test)]
#test_label =  [x.strip().split(' ')[1] for x in open(ori_test)]


cls_name = [x.split('/')[0] for x in train_name]
cls_name_test = [x.split('/')[0] for x in test_name]

train_name = [x.split('/')[1][:-4] for x in train_name]
test_name = [x.split('/')[1][:-4] for x in test_name]

label_dic = {}
for i in range(len(cls_name)):
    tmp = cls_name[i]
    if tmp not in label_dic:
        label_dic[tmp] = train_label[i]


#label_dic = {cls_name[i]:train_label[i] for i in range(len(cls_name))}
test_label = [label_dic[i] for i in cls_name_test]

train_path =[]
test_path = []
train_lines = []
test_lines = []

for i in range(len(train_name)):
    cu_path = os.path.join(frames_path, train_name[i])
    if not os.path.exists(cu_path):
        continue
    cu_label = train_label[i]
    cu_len = len([f for f in os.listdir(cu_path)])
    cu_line = cu_path + ' ' + str(cu_len) + ' ' +  cu_label + '\n'
    train_lines.append(cu_line)

for i in range(len(test_name)):
    cu_path = os.path.join(frames_path, test_name[i])
    if not os.path.exists(cu_path):
        continue
    cu_label = test_label[i]
    cu_len = len([f for f in os.listdir(cu_path)])
    cu_line = cu_path + ' ' + str(cu_len) + ' ' +  cu_label + '\n'
    test_lines.append(cu_line)

rec_train_name = 'train_record_split' + ori_train.split('.')[0][-2:] + '.txt'
rec_test_name = 'test_record_split' + ori_test.split('.')[0][-2:] + '.txt'
tra = open(rec_train_name, 'w')
for i in train_lines:
    tra.writelines(i)

tra.close()
te = open(rec_test_name, 'w')
for i in test_lines:
    te.writelines(i)
te.close()




