# Import pandas, numpy and regex lib
import pandas as pd
import numpy as np
import re

while True:
    # Task 1: Open and Read file
    while True:
        file_inp = input('Enter a class file to grade'
                         '(i.e. class1 for class1.txt): ')
        file_path = 'data_files\\Data Files\\' + file_inp + '.txt'
        try:
            df = pd.read_csv(file_path, sep=' ', header=None)
            print('Successfully opened {}'.format(file_inp))
            break
        except FileNotFoundError:
            print('File can not be found')

    # Task 2: Analyze and Report Data
    print('')
    print('**** ANALYZING ****')
    print('')

    arr_inp = np.array(df)
    invalid_line = 0
    lst_valid_line = []

    for i in range(len(arr_inp)):
        # Split each line into list of ID and answers
        line = list(arr_inp[i][0].split(','))
        # Check if the length of line is correct
        if len(line) != 26:
            invalid_line = invalid_line + 1
            print('Invalid line of data: does not contain exactly 26 '
                  'values:\n{}'.format(arr_inp[i][0]))
            print('')
        # Check if ID format is correct
        elif not re.match('^N[0-9]{8}', line[0]):
            invalid_line = invalid_line + 1
            print('Invalid line of data: '
                  'N# is invalid\n{}'.format(arr_inp[i][0]))
            print('')
        else:
            lst_valid_line.append(line)

    if invalid_line == 0:
        print('No errors found!')
        print('')

    print('**** REPORT ****')
    print('')
    print('Total valid lines of data:', len(lst_valid_line))
    print('Total invalid lines of data:', invalid_line)
    print('')

    # Task 3: Score
    answer_key = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'
    lst_key = answer_key.split(',')

    # Create DataFrame for valid lines
    df = pd.DataFrame(lst_valid_line)
    df.set_index([0], inplace=True)
    df = df.rename_axis('ID', axis=1)

    # Replace each answer by its score (-1, 0, 4) in DataFrame
    for i in range(1, 26):
        df[i] = df[i].apply(lambda x: 'Skip' if x == ''
                            else (True if x == lst_key[i-1] else False))

    df = df.replace(to_replace=True, value=4)
    df = df.replace(to_replace=False, value=-1)
    df = df.replace(to_replace='Skip', value=0)

    # Create new column of total score for each ID in DataFrame
    total_score = list(df.sum(axis=1))
    df['Total_score'] = total_score

    # Report class' result
    # 3.1. Total high-score students
    high_score = df[df['Total_score'] > 80]
    print('Total student of high scores:', len(high_score))

    # 3.2. Average score
    avg_score = df['Total_score'].mean()
    print('Mean (average) score:', round(avg_score, 2))

    # 3.3. Highest score
    max_score = df['Total_score'].max()
    print('Highest score:', max_score)

    # 3.4. Lowest score
    min_score = df['Total_score'].min()
    print('Lowest score:', min_score)

    # 3.5. Range score
    range_score = max_score - min_score
    print('Range of scores:', range_score)

    # 3.6. Median score
    list_score = sorted(total_score)
    length = len(list_score) // 2

    if len(list_score) % 2 == 0:
        print('Median score:',
              (list_score[length - 1] + list_score[length]) / 2)
    else:
        print('Median score:', list_score[length])

    print('')

    # 3.7. Questions skipped
    # Count the number of answers skipped for each question
    count_skip = []
    for i in range(1, 26):
        count_skip.append(len(df[df[i] == 0]))

    # Find questions that most people skip and number of answer skipped
    max_idx_skip = np.argwhere(count_skip == np.amax(count_skip))
    max_cnt_skip = max(count_skip)
    str_skip = ''

    for i in range(len(max_idx_skip)):
        str_skip = (str_skip + str(max_idx_skip[i, 0] + 1)
                    + ' - ' + str(max_cnt_skip)
                    + ' - ' + str(round(max_cnt_skip / len(lst_valid_line), 2))
                    + ', ')

    print('Question that most people skip:', str_skip.rstrip(', '))

    # 3.8. Incorrect questions
    # Count the number of incorrect answers for each question
    count_incorrect = []
    for i in range(1, 26):
        count_incorrect.append(len(df[df[i] == -1]))

    # Find questions that most people answer incorrectly
    # Find number of incorrect answer
    max_idx_inc = np.argwhere(count_incorrect == np.amax(count_incorrect))
    max_cnt_inc = max(count_incorrect)
    str_inc = ''

    for i in range(len(max_idx_inc)):
        str_inc = (str_inc + str(max_idx_inc[i, 0] + 1)
                   + ' - ' + str(max_cnt_inc)
                   + ' - ' + str(round(max_cnt_inc / len(lst_valid_line), 2))
                   + ', ')

    print('Question that most people answer incorrectly:',
          str_inc.rstrip(', '))

    # Task 4: Export result to file
    file_out = 'grades_output\\' + file_inp + '_grades.txt'
    df2 = df[['Total_score']].copy()
    df2.to_csv(file_out, header=False)

    # Restart program
    print('')
    restart = input('Do you want to restart the program? (Y/N)')
    restart = restart.lower().strip()
    if restart == 'n':
        quit()
    else:
        print('--------RESTARTING--------')
