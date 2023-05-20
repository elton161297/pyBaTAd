import  nmap
class network(object):
    def__intt__(self):
         ip=input("please enter default ip address of router")
         self.ip=ip

    def networkscanner(self):
         if len(self.ip) == 0:
             network='192.168.1.1/24'
         else:
             network =self.ip+'/24'
         print("scanning please wait ---->")

         nm=nmap.portscanner()
         nm.scan(host=network,arguments='-sn')
         host_list=[(x, nm[x]['status']['state']) for x in nm.all_hosts()]
         for host, status in hosts_list:
             print("host\t{}".format(host))

if __name__ =="__main__"
    d=network()
    d.networkscanner()


    
    


