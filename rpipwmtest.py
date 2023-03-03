import pigpio
from time import sleep

ch1_rise_tick = 0
ch2_rise_tick = 0

ch1_in = 23
ch2_in = 24

ch1_out = 18
ch2_out = 19
on = True
pi = pigpio.pi()

class rpipwmtest:
    
    def gpiocallback(gpio, level, tick):
        global ch1_rise_tick, ch2_rise_tick
        global ch1_in, ch2_in
        global ch1_out, ch2_out
        global on
        on = False
        if gpio == ch1_in :
            if level==1 :
                ch1_rise_tick = tick
            elif level==0 : 
                pwm_width = tick - ch1_rise_tick
                if 500<pwm_width and pwm_width<2500 :
                    pi.set_servo_pulsewidth(ch1_out, pwm_width)
            else :
                pi.set_servo_pulsewidth(ch1_out, 0)

        if gpio == ch2_in :
            if level==1 :
                ch2_rise_tick = tick
            elif level==0 : 
                pwm_width = tick - ch2_rise_tick
                if 500<pwm_width and pwm_width<2500 :
                    pi.set_servo_pulsewidth(ch2_out, pwm_width)
            else :
                pi.set_servo_pulsewidth(ch2_out, 0)
                
        
                    
    def callb(self):
        
        global ch1_in, ch2_in
        global ch1_out, ch2_out
        global on
        power = 0
        print("s")
        pi.set_mode(ch1_out, pigpio.OUTPUT)
        pi.set_mode(ch2_out, pigpio.OUTPUT)
        pi.set_mode(ch1_in, pigpio.INPUT)
        pi.set_mode(ch2_in, pigpio.INPUT)
        rp = pi.callback(ch1_in, pigpio.EITHER_EDGE, rpipwmtest.gpiocallback)
        rp = pi.callback(ch2_in, pigpio.EITHER_EDGE, rpipwmtest.gpiocallback)
        while True:
            if power == 0 and on == False:
                power = 1
                return False
            sleep(1)
            
            
def main():
    rpip = rpipwmtest()
    rpip.callb()
        
if __name__ == '__main__':
    main()
