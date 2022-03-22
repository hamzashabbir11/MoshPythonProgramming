from pathlib import Path

obj1=Path('')
for file in obj1.glob('*.py'):
    print(file)
print('lOOP 1 END *******************************')
obj2=Path('')
for file in obj2.glob('*'):
    print(file)