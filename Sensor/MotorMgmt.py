#ifndef WHEEL_MOTOR_MGMT_H_
#define WHEEL_MOTOR_MGMT_H_
#include "ev3api.h"
#include "Motor.h"
#include "Walker"
#include "BrightnessSensor.h"

class WheelMotorMgmt {
    public:
        WheelMotorMgmt(ev3api::Motor& leftWheel,
                                 ev3api::Motor& rightWhee);
        ~WheelMotorMgmt();
        void walkDriveOrder(int rpwm,int lpwm);
        void init();
        float getRCount();
        float getLCount();
           // void armDriveOrder(int pwm);
       // void tailDriveOrder(int pwm);
    private:
        int r_current_encoded_value;
        int l_current_encoded_value;
        ev3api::Motor mLeftWheel;
        ev3api::Motor mRightWheel;
        //int rpwm;
       // int lpwm;
        //int arm_current_encoded_value;
        //int tail_current_encoded_value;
};


#endif