# a simple module for parsing Python to .gcode
class Parser:
    def __init__(self):
        pass
    def setup(self,rel_pos=True,mm=True,home=(0,0,20)):
        cmd_list=[]
        self.home=home
        self.pos=rel_pos
        if mm:
            cmd_list.append('G21 ; mm')
        else:
            cmd_list.append('G20 ; inches')
        cmd_list.append('G90 ; set absolute position for homing')
        cmd_list.append('G00 X{x} Y{y} Z{z} ; go to set home'.format(x=str(home[0]), y=str(home[1]), z=str(home[2])))
        if self.pos:
            cmd_list.append('G91 ; set relative position')
        else:
            cmd_list.append('G90 ; set absolute position')
        return tuple(cmd_list)
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
            return tuple([cmd])
        else:
            pass
    def add_home(self):
        cmd_list=[]
        old_pos=self.pos
        cmd_list.append(self.change_pos(rel_pos=False))
        cmd_list.append('G00 X{x} Y{y} Z{z} ; go to set home'.format(x=str(self.home[0]), y=str(self.home[1]), z=str(self.home[2])))
        cmd_list.append(self.change_pos(old_pos))
        return tuple(cmd_list)
    def add_fan(self,speed=255):
        if speed==255:
            return tuple(['M106 ; use fan'])
        elif speed==0:
            return tuple(['M107 ; use fan'])
        else:
            return tuple(['M106 S{s} ; use fan'.format(s=str(speed))])
    def change_pos(self,rel_pos=True):
        self.pos=rel_pos
        if self.pos:
            return tuple(['G91 ; set relative position'])
        else:
            return tuple(['G90 ; set absolute position'])
    def change_mm(self,mm=True):
        if mm:
            return tuple(['G21 ; mm'])
        else:
            return tuple(['G20 ; inches'])
        def change_home(self,home=(0,0,20)):
            self.home=home

print('Gcodelib v2.1')
print('MIT Licence 2024 Benjamin Porter')
