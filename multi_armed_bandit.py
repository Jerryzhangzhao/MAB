# Multi-Armed Bandit
import random
import math

class MAB():
    arm_num=0
    probability=dict({}) # reward probability of each arm
    try_time=dict({}) # total trird times for each arm
    reward=dict({}) # total reward for each arm
    
    def set_arm_num(self):
        '''
           set the number of arms of MAB and the reward probability 
           of each arm.
        '''
        num = (int)(input('set the number of arms:'))
        if(num>0 and num<100):
            self.arm_num=num
            for i in range(num):
                self.probability[str(i+1)]=random.random()
                self.try_time[str(i+1)]=0 
                self.reward[str(i+1)]=0
            print("the bandit has "+str(num)+" arms!")
        else:
            print("Please input a correct number, for example:5")
        print(self.try_time)

    def draw_bandit(self):
        '''
           draw the multi-armed bandit,including tried times and reward
           for each arm, and total tried times and rewards.
        '''
        print('\n')
        if(self.arm_num<=8):
            print('*'*8*(self.arm_num+1)+'**')
            title = str(self.arm_num)+" arm bandit"
            title_format='{:^'+str(8*(self.arm_num+1))+'s}'
            print('*'+title_format.format(title)+'*')

            print('*'+' '*8*(self.arm_num+1)+'*')

            print('*{:^8s}'.format('arm'),end='')
            for arm in range(self.arm_num):
                print('{:^8d}'.format(arm+1),end='')
            print('*\n')

            print('*{:^8s}'.format('tried'),end='')
            for arm in range(self.arm_num):                
                print('{:^8d}'.format(self.try_time[str(arm+1)]),end='')
            print('*\n')

            print('*{:^8s}'.format('reward'),end='')
            for arm in range(self.arm_num):
                print('{:^8d}'.format(self.reward[str(arm+1)]),end='')   
            print('*\n')
            
            total_tried = 0
            total_rewards = 0
            for key in self.try_time:
                total_tried+=self.try_time[key]
                total_rewards+=self.reward[key]
            print('*'+title_format.format("total tried:"+str(total_tried))+'*')
            print('*'+title_format.format("total rewards:"+str(total_rewards))+'*')
            print('*'+' '*8*(self.arm_num+1)+'*')
            print('*'*8*(self.arm_num+1)+'**')

    def e_greedy_method(self):
        '''
           e greedy method: define a e_greedy_factor and create a random number,
           when the random number is less then e_greedy_factor, then pick a arm
           randomly, else pick the arm with greatest average reawards. 
        '''
        e_greedy_factot = 0.9
        rand = random.random()
        print("rand " + str(rand))
        arm_index = 1
        if(rand < e_greedy_factot):
            arm_index =  random.randint(1,self.arm_num)  
        else:
            max_avg_reward = 0
            for key in self.try_time:
                if(self.try_time[key]>0 and self.reward[key]/self.try_time[key]>max_avg_reward):
                    max_avg_reward = self.reward[key]/self.try_time[key]
                    print(max_avg_reward)
                    arm_index = (int)(key)
        return arm_index
            
    def sofmax_method(self):
        '''
           softmax method: calculate the softmax value of each arm's avarage reward,
           and pick the arm with greatest softmax value. 
        '''
        tao = 1
        exp_sum = 0
        acc_softmax_value = 0
        rand = random.random()
        arm_index = 0

        for key in self.try_time:
            if(self.try_time[key]>0):
                exp_sum += math.exp(self.reward[key]/self.try_time[key]/tao)
            else:
                exp_sum += math.exp(0/tao)
        for key in self.try_time:
            if( exp_sum>0):
                avg_reward_temp = 0
                if (self.try_time[key]==0):
                    avg_reward_temp=0
                else :
                    avg_reward_temp=self.reward[key]/self.try_time[key]
                acc_softmax_value += math.exp(avg_reward_temp/tao)/exp_sum
                if(rand > acc_softmax_value):
                    arm_index = int(key)
        return arm_index+1


if __name__ == '__main__':
    mab = MAB()
    print("****Multi-armed Bandit***")
    mab.set_arm_num()
    mab.draw_bandit()
    while(1):
        input("Press Enter to continue...") # this line for manual control process of each step
        choice = mab.sofmax_method() #mab.e_greedy_method()#input("please choose a arm:")
        if(choice=="q" or choice=="Q"):
            break;
        else:
            arm_index = (int)(choice)
            if(arm_index>0 and arm_index<=mab.arm_num):
                mab.try_time[str(arm_index)]+=1
                if(random.random()>mab.probability[str(arm_index)]):
                    print("get reward!")
                    mab.reward[str(arm_index)]+=1
                else:
                    print("sad,no reward!") 
                mab.draw_bandit()  
            else:
                print("not arm with index "+choice)






