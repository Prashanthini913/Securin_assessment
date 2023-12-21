def diceA_combinations(elements,length,current,all_combinations):
    if len(current)==length:
        all_combinations.append((current))
        return
    for element in elements:
        diceA_combinations(elements,length,current+[element],all_combinations)
    return all_combinations


def diceB_combinations(elements,length,start,current,all_combinations):
    if len(current) == length:
        all_combinations.append((current))
        return
    for i in range(start,len(elements)):
        diceB_combinations(elements,length,i+1,current+[elements[i]],all_combinations)
    return all_combinations

def prob_of_sum(arr1,arr2):
    psum1=[0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            k=arr1[i]+arr2[j]
            psum1[k-1]=psum1[k-1]+1
    for i in range(len(psum1)):
        if psum1[i]!=0:
            psum1[i]=psum1[i]/36
    return psum1

def transform(die_a,die_b):
    elements1=[1,2,3,4]
    length=6
    current=[]
    all_combinations=[]
    elements2=[1,2,3,4,5,6,7,8]
    start=0
    combo1=diceA_combinations(elements1,length,current,all_combinations)
    combo2=diceB_combinations(elements2,length,start,current,all_combinations)          
    flag=0
    probability_of_sums=[0,1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
    for i in combo1:
       for j in combo2:
          if(prob_of_sum(i,j)==probability_of_sums):
             print("new die_a :",end=" ")
             print(i)
             print("new die_b :",end="")
             print(j,end="")
             flag=1
             break
       if (flag):
             break  


die_a=[1,2,3,4,5,6]
die_b=[1,2,3,4,5,6]
transform(die_a,die_b)