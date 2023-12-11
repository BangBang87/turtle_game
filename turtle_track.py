import turtle
import random
import time

# 創建一個 Turtle 畫布
screen = turtle.Screen()
screen.title("Dodger Game")
screen.bgcolor('black')
turtle.colormode(255)

# 設定畫布大小
screen.setup(width=600, height=600)

#取消動畫效果
screen.tracer(0)

# 創建小龜
player = turtle.Turtle()
player.shape("turtle")
player.color(random.randint(50, 250),random.randint(50, 250),random.randint(50, 250))
player.penup()
player.speed(0)
player.shapesize(2, 2, 2)
player.goto(0, 0)

#創建時間烏龜
time_turtle = turtle.Turtle()
time_turtle.shapesize(0.0001)
time_turtle.color('white')
time_turtle.penup()
time_turtle.goto(-300, -300)
time_set = 0

# 創建球red
rad_ball = turtle.Turtle()
rad_ball.shape("circle")
rad_ball.color('red')
rad_ball.penup()
rad_ball.speed(0)
rad_ball.shapesize(3, 3, 3)
rad_ball.goto(-290, 290)
rad_ball.dy = -0.12

# 創建green
green_ball = turtle.Turtle()
green_ball.shape("circle")
green_ball.color('green')
green_ball.penup()
green_ball.speed(0)
green_ball.shapesize(3, 3, 3)
green_ball.goto(-290, 290)
green_ball.dy = -0.12#移動速度

# 創建pink

pink_ball = turtle.Turtle()
pink_ball.shape('circle')
pink_ball.color('pink')
pink_ball.penup()
pink_ball.speed(0)
pink_ball.shapesize(3, 3, 3)
pink_ball.goto(290,-290)
pink_ball.dy = -0.12

#創建追蹤ball
track_ball = turtle.Turtle()
track_ball.shape('circle')
track_ball.color('white')
track_ball.penup()
track_ball.speed(0)
track_ball.shapesize(3, 3, 3)
track_ball.goto(290, -290)
track_ball.dy = -0.12
# 定義小龜上下左右移的函數
def move_left():
    player.setheading(180)

def move_right():
    player.setheading(0)

def move_down():
    player.setheading(-90)

def move_up():
    player.setheading(90)


# 綁定按鍵事件
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_up, "Up")

def record_point():
    #儲存分數
    player_name = input('your name= ')
    with open('turtle_track_gamere_cord.txt', 'a') as file:
        file.write(player_name+ '='+ str(point)+ '\n')
        
    #讀取分數
    with open('turtle_track_gamere_cord.txt', 'r') as file:
        turtle_track_gamere_cord = file.readlines()
        
    #印出分數
    print('-record-', turtle_track_gamere_cord)

def gameover():
    time_turtle.color('yellow')
    time_turtle.goto(-340, -20)
    time_turtle.write('-----Game Over-----', font = ('Arial', 60, 'normal'))
    
# 遊戲迴圈
while True:

    #移動烏龜
    player.forward(0.2)
    
    #計時
    time_set += 1
    if time_set % 100 == 0:
        time_turtle.clear()
        point = int(time_set / 100)
        time_turtle.write(point, font = ('Arial', 50, 'normal'))
        #彩色烏龜
        #player.color(random.randint(50, 250),random.randint(50, 250),random.randint(50, 250))
    
    # 移動障礙物
    y = rad_ball.ycor()
    y += rad_ball.dy
    rad_ball.sety(y)

    y = track_ball.ycor()
    y -= track_ball.dy
    track_ball.sety(y)

    x = green_ball.xcor()
    x -= green_ball.dy
    green_ball.setx(x)

    x = pink_ball.xcor()
    x += pink_ball.dy
    pink_ball.setx(x)

    # 如果球超出畫布底部，重新設定位置
    if rad_ball.ycor() < -290:
        ball_speed = random.uniform(-0.15 ,-0.25)
        rad_ball.dy = ball_speed
        rad_ball.goto(player.xcor(), 290)

    if track_ball.ycor() > 290:
        ball_speed = random.uniform(-0.15 ,-0.25)
        track_ball.dy = ball_speed
        track_ball.goto(player.xcor(), -290)
    # 如果障礙物超出畫布底部，重新設定位置
    if green_ball.xcor() > 290:
        ball_speed = random.uniform(-0.15 ,-0.25)
        green_ball.dy = ball_speed
        green_ball.goto(-290, player.ycor())
        
    if pink_ball.xcor() < -290:
        ball_speed = random.uniform(-0.15 ,-0.25)
        pink_ball.dy = ball_speed
        pink_ball.goto(290, player.ycor())

    #邊界檢測

    if (player.xcor() < -290 or player.xcor() > 290 or player.ycor() < -290 or player.ycor() > 290
        ):
        print('遊戲結束! 你碰到邊界了')
        print('你的分數= ', point)
        gameover()
        record_point()
        
        break

    # 碰撞檢測
    if (
        (player.xcor() - 40 < rad_ball.xcor() < player.xcor() + 40
        and player.ycor() - 40 < rad_ball.ycor() < player.ycor() + 40)
    ):
        print("遊戲結束! 碰到紅色")
        print('你的分數= ', point)
        gameover()
        record_point()
        break

    if (
        (player.xcor() - 40 < green_ball.xcor() < player.xcor() + 40
        and player.ycor() - 40 < green_ball.ycor() < player.ycor() + 40)
    ):
        
        print("遊戲結束! 碰到綠色")
        print('你的分數= ', point)
        gameover()
        record_point()
        break
    
    if (
        (player.xcor() - 40 < pink_ball.xcor() < player.xcor() + 40
        and player.ycor() - 40 < pink_ball.ycor() < player.ycor() + 40)
    ):
        print("遊戲結束! 碰到粉色")
        print('你的分數= ', point)
        gameover()
        record_point()
        break
    
    if (
       (player.xcor() - 40 < track_ball.xcor() < player.xcor() + 40
        and player.ycor() - 40 < track_ball.ycor() < player.ycor() + 40)
    ):
        
        print("遊戲結束! 碰到白色")
        print('你的分數= ', point)
        gameover()
        record_point()
        
        break
        


#更新畫布
    screen.update()

# 保持視窗開啟
#turtle.done()