def tower(disk, source, auxi, dest):
    if disk == 1:
        print("Move disk 1 from {} to {}".format(source, dest))
        return
    
    tower(disk - 1, source, dest, auxi)
 
    print("Move disk {} from {} to {}".format(disk, source, dest))
  
    tower(disk - 1, auxi, source, dest)
    
n = int(input("Enter the number of disks: "))
print("Steps involved are:")
tower(n, 'A', 'B', 'C')
