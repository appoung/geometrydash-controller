# What is it?
지오메트리 대쉬라는 게임을 손으로 간단하게 조작할수 있게 하는 작품입니다
[![Video Label](http://img.youtube.com/vi//FLHfpF7-nw4/0.jpg)](https://youtube.com/shorts/FLHfpF7-nw4?feature=share)
# How?
라즈베리파이 피코 짭퉁을 알리익스프레스에서 구매하였습니다.
거기에 초음파센서(hsr04)를 납땜하여 연결 후 코드를 업로드하여 보드를 마우스 입력처럼 인식하여 손과 센서와의 거리가 멀어지면 마우스가 클릭을해 점프하는 것입니다. 애플기기,안드로이드기기,컴퓨터등 모두 적용됩니다.
# Code
코드는 Circuitpython이라는 언어로 쉽게 파이썬 문법을 쓰며 작성하였고요, Thonny Ide로 업로드까지 하였습니다.


소스코드 입니다.


```python
import time
import board
import adafruit_hcsr04
import usb_hid
from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP22, echo_pin=board.GP16)

while True:
    try:
        if sonar.distance > 6:
            print("jump")
            mouse.click(Mouse.LEFT_BUTTON)
            
    except RuntimeError:
        print("Retrying!")
```  

## 설명

피코보드의 22번핀에 초음파센서의 trigger_pin을,16번핀에 echo_pin을 연결해주면, 피코보드에서 sonar.distance값으로 손과 센서와의 거리를 알수있고, 거리가 6cm보다 길어지면,화면을 클릭하는 코드입니다.
