paragraph = '''Once upon a time, in a small village, there lived a farmer with his faithful Donkey. The Donkey was very hardworking and helped the farmer every day. One day, the farmer decided to take the Donkey to the market. As they walked through the village, the Donkey saw a field of fresh green grass and started munching. The farmer had to pull the Donkey away from the grass to continue their journey. At the market, many people admired the strong and healthy Donkey. The farmer was proud of his Donkey and treated it with care and kindness. After selling their goods, the farmer and the Donkey returned home. That night, the farmer fed the Donkey some extra hay as a reward for its hard work. The donkey brayed happily, feeling content and loved.
'''
with open('story.txt','w') as f:
    f.write(paragraph)

with open('story.txt','r+') as f:
    li = f.read()

words = li.split()
words = [w.lower() for w in words]

modified_words = ['#####' if word=='donkey' else word for word in words]
para = ' '.join(modified_words)
with open('story.txt','w') as f:
    f.write(para)