with open('maxlevel.txt','r') as f:
    lines = f.readlines()

for line in lines:
    print('line:', line)
    usr, level = line.split(' : ')
    print(usr, level)

### open file reading danish letters correctly and new lines    

# with open('levels/level1.txt', 'r', encoding='utf-8') as f:
#     content = f.read()