#automated movement with no joystick 
task main()
{
    int normalSpeed;
    int slowSpeed;
    normalSpeed = 63;
    slowSpeed = 50;

    wait1Mspec(2000);

    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //First Forward Movement
    while(SensorValue[leftEncoder] < 1260)
    {
        if(SensorValue[leftEncoder] > SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = slowSpeed;
        }
        if(SensorValue[rightEncoder] > SensorValue[leftEncoder])
        {
            motor[rightMotor] = slowSpeed;
            motor[leftMotor] = normalSpeed;
        }
        if(SensorValue[leftEncoder] == SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = normalSpeed;
        }
    }
    
    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //left Turn
    while(SensorValue[leftEncoder] < 720)
    {
        motor[rightMotor] = 63;
        motor[leftMotor] = -63;
    }

    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //Second Forward Movement
    while(SensorValue[leftEncoder] < 1080)
    {
        if(SensorValue[leftEncoder] > SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = slowSpeed;
        }
        if(SensorValue[rightEncoder] > SensorValue[leftEncoder])
        {
            motor[rightMotor] = slowSpeed;
            motor[leftMotor] = normalSpeed;
        }
        if(SensorValue[leftEncoder] == SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = normalSpeed;
        }
    }

    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //Right Turn
    while(SensorValue[leftEncoder] < 720)
    {
        motor[rightMotor] = -63;
        motor[leftMotor] = 63;
    }


    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //Third Forward Movement
    while(SensorValue[leftEncoder] < 800)
    {
        if(SensorValue[leftEncoder] > SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = slowSpeed;
        }
        if(SensorValue[rightEncoder] > SensorValue[leftEncoder])
        {
            motor[rightMotor] = slowSpeed;
            motor[leftMotor] = normalSpeed;
        }
        if(SensorValue[leftEncoder] == SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = normalSpeed;
        }
    }
    
    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //Right Turn
    while(SensorValue[leftEncoder] < 720)
    {
        motor[rightMotor] = -63;
        motor[leftMotor] = 63;
    }

    SensorValue[rightEncoder] = 0;
    SensorValue[leftEncoder] = 0;
    //Fourth Forward Movement
    while(SensorValue[leftEncoder] < 600)
    {
        if(SensorValue[leftEncoder] > SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = slowSpeed;
        }
        if(SensorValue[rightEncoder] > SensorValue[leftEncoder])
        {
            motor[rightMotor] = slowSpeed;
            motor[leftMotor] = normalSpeed;
        }
        if(SensorValue[leftEncoder] == SensorValue[rightEncoder])
        {
            motor[rightMotor] = normalSpeed;
            motor[leftMotor] = normalSpeed;
        }
    }
}

#users controllers with joystick
'''
task main()
{
    while(vexRT[Btn7D] == 0 )
    {
    }
    
    ClearTimer(T1);
    while(timer[T1] < 90000)
    {
        motor[leftMotor] = vexRT[Ch3] / 2;
        motor[leftMotor] = vexRT[Ch2] / 2;

        if (vexRT[Btn6U] == 1 )
        {
            motor[armMotor] = 40;
        }
        else if(vexRT[Btn6D] == 1 )
        {
            motor[armMotor] = -40;
        }
        else
        {
            motor[armMotor] = 0;
        }
            
     }
     motor[leftMotor] = 0;
     motor[rightMotor] = 0;
    
}
'''

