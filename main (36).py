def tower(disk,sourcs,auxi,dest):
    if(disk==1):
        print("Move{} from {} to {} ")
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("Move{} from {} to {}".format(disk,source,dest))
        tower(dist-1,auxi,source,dest)
        
n=int(input("Enter the number"))
print("Steps involed are:" )
tower(disk,'A','B''c')