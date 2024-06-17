# a simple module for parsing Python to .gcode
class Parser:
    def __init__(self):
        self.cmd_list=[]
    def add_manual(self,cmd):
        # Warning: command may break Parser
        self.cmd_list.add(str(cmd))
    def setup(self,rel_pos=True,mm=True,home=[0,20,0]):
        self.cmd_list.append('%')
        self.home=home
        
        if rel_pos:
            self.cmd_list.append('G91 ; set relative position')
        else:
            self.cmd_list.append('G90 ; set absolute position')
        if mm:
            self.cmd_list.append('G21 ; mm')
        else:
            self.cmd_list.append('G20 ; inches')
        self.cmd_list.append('G00 X{x} Y{y} Z{z} ; go to set home'.format(x=str(home[0]), y=str(home[1]), z=str(home[2])))
    def add_movement(self,x=0,y=0,z=0,speed=200):
        if (x!=0 or y!=0 or z!=0):
            cmd='G01 '
            if x!=0:
                cmd+='X{coordx} '.format(coordx=str(x))
            if y!=0:
                cmd+='Y{coordy} '.format(coordy=str(y))
            if z!=0:
                cmd+='Z{coordz} '.format(coordz=str(z))
            cmd+='F{f}'.format(f=str(speed))
            self.cmd_list.append(cmd)
        else:
        	pass
    def add_home(self):
        self.cmd_list.append('G00 X{x} Y{y} Z{z} ; go to set home'.format(x=str(self.home[0]), y=str(self.home[1]), z=str(self.home[2])))
    def add_fan(self,speed=255):
        if speed==255:
            self.cmd_list.append('M106 ; use fan'.format(s=str(speed)))
        else:
            self.cmd_list.append('M106 S{s} ; use fan'.format(s=str(speed)))
    def change_pos(self,rel_pos=True):
        if rel_pos:
            self.cmd_list.append('G91 ; set relative position')
        else:
            self.cmd_list.append('G90 ; set absolute position')
    def change_mm(self,mm=True):
        if mm:
            self.cmd_list.append('G21 ; mm')
        else:
        	self.cmd_list.append('G20 ; inches')
    def change_home(self,home=[0,20,0]):
        self.home=home
    def parse(self, target=''):
        if self.cmd_list[len(self.cmd_list)-1]!='%':
            self.cmd_list.append('%')
        if len(target)>0:
            if target=='stdout':
                output=''
                for cmd in self.cmd_list:
                    print('Parsing '+cmd+'...')
                    output+=cmd+'\n'
                return output
            else:
                f=open(target,'w')
                for cmd in self.cmd_list:
                    print('Parsing '+cmd+'...')
                    f.write(cmd+'\n')
                    f.close()
        
        else:
            f=open('output.gcode','w')
            for cmd in self.cmd_list:
                print('Parsing '+cmd+'...')
                f.write(cmd+'\n')
                f.close()
    def clear(self):
        self.cmd_list=[]
        
        
                
        
        
        
        
