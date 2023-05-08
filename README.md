# firstname_lastname_grade_the_exams.py

## Introduction

A python program that grades and reports multiple-choice exams.

## Main features
- **Grading the exams:** 
The program reads every single line of text files which contain the exam answer of each class. Invalid answers are eliminated from the result. Total student of high scores, mean (average) score, highest score, lowest score, question that most people skip, question that most people answer incorrectly... are reported and displayed on the screen.
- **Exporting grades:** 
Grades are scored and exported automatically to a text file.

## How to use

1. Save the exam answer text file of each class to the folder: _..\\data_files\Data Files_
2. Run the program. Type the file name that needs to grade (not include the extension ".txt")
3. The program will caculate and report the result to the screen. The text file of students' score will then be generated to the folder _"grades_output"_.
4. After grading process finishes, the program will ask you if you want to grade the other class. Type any characters except "N" in case you want to restart.
5.  Type "N" if you want to exit the program.

## Forking GitHub repo

First use the GitHub interface to "fork" this repository into your own account. Then do git clone of your repository to get a local copy. Inside that checkout, do:
```
git remote add upstream https://github.com/Liin207/DSP301x_asm2_linhntFX18208-funix.edu.vn.git
```
This will allow you to git pull upstream master in order to get updates. When you create new files, git add/commit/push them to your repository.
