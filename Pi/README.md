# design system

## hardware 
- 4 led
- 4 ir sensor

## free parking

### ir pin for detect free parking
  - 32
  - 36
  - 38
  - 40

### led pin to display parking status
  - 31
  - 33
  - 35
  - 37

### 7segment pin to display remaining parking space
vcc : 5v
Din : pin 19
CS  : pin 24
CLK : pin 23
should using ground at 20,25

### display remaining on web? or chatbot to ask for remaining parking space?

## vip parking 

ir: 32, 36, 38, 40
led: 31, 33, 35, 37

sent car status and token to netpie 
{
  "token": LineNotifyToken,
  "status": GPIO.LOW or GPIO.HIGH
}