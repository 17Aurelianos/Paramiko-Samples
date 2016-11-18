import paramiko
import time

#Uses Python 3.0+ syntax

if __name__ == '__main__':
	username = "[Your Username]"
	password = "[Your Password]"
	
	
	# Opens files in read mode
	f1 = open(".\hostfile.txt","r") #A flat file with hostnames or IP addresses. 
	f2 = open("results.txt", "w") #Results/Exception output.


	# Creates list based on f1
	devices = f1.readlines()


	for device in devices:
		device = device.rstrip()
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			remote_conn_pre.connect(device, username=username, password=password, look_for_keys=False, allow_agent=False, timeout=10)
		except Exception:
			print (device, Exception, file=f2)
			print ("", file=f2)
			continue
		remote_conn = remote_conn_pre.invoke_shell()	
		remote_conn.send("\n")
		remote_conn.send("show version\n")
		time.sleep(2)
		output = remote_conn.recv(5000)
		print (device, output, file=f2)
		print ("", file=f2)
		remote_conn_pre.close()
	f1.close()
	f2.close()
