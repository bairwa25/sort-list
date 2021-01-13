def sort_lists(list1,c):
    for i in range(len(list1)-1):
        # if the next element is greater then the next element, swap it.
        # c is the column according to which you want to sort the data
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
 
list1=[ 
        ['Bajaj Pulsar', '220 F', 40],
        ['Yamaha', 'YZF R15 Ver 3.0', 50],
        ['TVS Apache', 'rtr 160', 45]
      ]
c=2
sort_lists(list1,c)
