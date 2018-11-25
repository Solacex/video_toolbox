import json
import sys,os
dataset_path = sys.argv[1]#'/home/liguangrui/20bn-something-something-v2-imageio'


with open('something-something-v2-labels.json', 'r') as f:
    label = json.load(f)
with open('something-something-v2-train.json', 'r') as f:
    train = json.load(f)
with open('something-something-v2-validation.json', 'r') as f:
    val = json.load(f)
with open('something-something-v2-test.json', 'r') as f:
    test = json.load(f)

cnt = 0

category = [k for k in label.keys()]

train_txt = []
for i in range(len(train)):
    cur_index = train[i]['id']
    cur_label = train[i]['template']
    cur_label = cur_label.replace(']', '').replace('[', '')
    cur_id = label[cur_label]
    num_frames = len(os.listdir(os.path.join(dataset_path, cur_index)))
    if num_frames==0:
        cnt+=1
    train_txt.append('%s %d %s'%(cur_index, num_frames, cur_id))
    print('%d/%d'%(i, len(train)))

val_txt = []
for i in range(len(val)):
    cur_index = train[i]['id']
    cur_label = train[i]['template']
    cur_label = cur_label.replace(']', '').replace('[', '')
    cur_id = label[cur_label]
    num_frames = len(os.listdir(os.path.join(dataset_path, cur_index)))
    if num_frames==0:
        cnt+=1
    val_txt.append('%s %d %s'%(cur_index, num_frames, cur_id))
    print('%d/%d'%(i, len(val)))

with open('train_video_folder.txt', 'w') as f:
    f.write('\n'.join(train_txt))
with open('val_video_folder.txt', 'w') as f:
    f.write('\n'.join(val_txt))

with open('category.txt', 'w') as f:
    f.write('\n'.join(category))

print(cnt, 'empty')





