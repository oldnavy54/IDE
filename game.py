import numpy as np

number=np.random.randint(1, 101) # загадываем число
count = 0

while True:
    predoct_number = int(input('угадай число от 1 до 100'))
    
    if predoct_number > number:
        print('Number should be smaller')
        
    elif predoct_number < number:
        print('number should be larger')
        
    else:
        print(f'you got the nuber {number} from the {count} attempt')
        break
