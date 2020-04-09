def hanoi(w , from, to, aux): 
    if q == 1: 
        print ("Take disk 1 from rod ",from,"to rod ",to )
        return
    hanoi(w-1, from, aux, to) 
    print ("Take disk",w,"from rod ",from,"to rod ",to )
    hanoi(w-1, aux, to, from) 
           
w =int(input("Enter no of Disks="))
hanoi(w, ' A', ' C', ' B')

