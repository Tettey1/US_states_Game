import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.hideturtle()
data = pandas.read_csv('50_states.csv')

state_list = data['state'].to_list()
score = 0

answer = []
while score < 50:
    answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt="What's Another State's Name?").title()
    if answer_state == 'Exit':
        missing_state = [state for state in state_list if state not in answer]
        break
    if answer_state in state_list:
        answer.append(answer_state)
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        score += 1
        tim.write(answer_state)


# generate a new file

missed = {
    'Missing State': missing_state
}

file = pandas.DataFrame(missed)
file.to_csv('missed_states.csv')


