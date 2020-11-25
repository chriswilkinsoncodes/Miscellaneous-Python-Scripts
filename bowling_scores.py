#!/usr/bin/env python

''' Keeps bowling score for one player. Error checks for valid input.
    Based on code example from Oh! Pascal! p200'''


def get_the_next_ball(maximum):
    ''' Reads a ball value and makes sure it's between 0 and maximum. '''

    number_of_pins = int(input('Enter number of pins for current ball '
                               f'(0-{maximum}): '))

    # Assume 0 for a negative entry.
    if number_of_pins < 0:
        number_of_pins = 0
        print('Negative ball value; assuming 0.')

    # Assume spare for too large value.
    elif number_of_pins > maximum:
        number_of_pins = maximum
        print(f'Ball value too large; assuming {maximum}.')

    return number_of_pins


def handle_frame(frame, score, last_two_were_strikes,
                 last_was_strike, last_was_spare):
    ''' Score one frame, update the strike and spare state variables. '''

    print(f'*** Frame: {frame} ***')
    first_ball = get_the_next_ball(10)

    # Was first ball a strike?
    if first_ball == 10:
        second_ball = 0
    else:
        second_ball = get_the_next_ball(10 - first_ball)

    # Complete the scoring of earlier frames if necessary.
    if last_two_were_strikes:
        score = score + first_ball + 20
        print(f'Frame: {frame-2} Score: {score}')

    if last_was_strike and (first_ball < 10):
        score = score + first_ball + second_ball + 10
        print(f'Frame: {frame-1} Score: {score}')

    if last_was_spare:
        score = score + first_ball + 10
        print(f'Frame: {frame-1} Score: {score}')

    if (first_ball + second_ball) < 10:
        score = score + first_ball + second_ball
        print(f'Frame: {frame} Score: {score}')

    # Update the game state variables - what are we working on?
    last_two_were_strikes = last_was_strike and (first_ball == 10)
    last_was_strike = first_ball == 10
    last_was_spare = (first_ball < 10) and ((first_ball + second_ball) == 10)

    return score, last_two_were_strikes, last_was_strike, last_was_spare


def two_more_balls(score, last_two_were_strikes):
    ''' A special case - get two more balls for a strike in the 10th frame. '''

    first_ball = get_the_next_ball(10)

    # Was first ball a strike?
    if first_ball == 10:
        second_ball = get_the_next_ball(10)
    else:
        second_ball = get_the_next_ball(10 - first_ball)

    # Complete the scoring of the 9th frame, if necessary.
    if last_two_were_strikes:
        score = score + first_ball + 20
        print(f'Frame: 9 Score: {score}')

    # Finish by scoring the 10th frame.
    score = score + first_ball + second_ball + 10
    print(f'Frame: 10 Score: {score}')


def one_more_ball(score):
    ''' Another special case - get one more ball for a 10th frame spare. '''

    first_ball = get_the_next_ball(10)
    score = score + first_ball + 10
    print(f'Frame: 10 Score: {score}')


if __name__ == '__main__':
    # Initialize the game's state variables.
    score = 0
    last_two_were_strikes = False
    last_was_strike = False
    last_was_spare = False

    # Process the score for each frame.
    for frame in range(1, 11):
        score, last_two_were_strikes, last_was_strike, last_was_spare = \
            handle_frame(frame, score, last_two_were_strikes,
                         last_was_strike, last_was_spare)

    # Take care of special cases in the 10th frame.
    if last_was_strike:
        two_more_balls(score, last_two_were_strikes)
    elif last_was_spare:
        one_more_ball(score)
