# Problem from Codeforces
# http://codeforces.com/problemset/problem/61/B

# After the contest in comparing numbers, Shapur's teacher found out that he is a real genius and that no one could possibly do the calculations faster than him even using a super computer!
#
# Some days before the contest, the teacher took a very simple-looking exam and all his n students took part in the exam. The teacher gave them 3 strings and asked them to concatenate them. Concatenating strings means to put them in some arbitrary order one after the other. For example from concatenating Alireza and Amir we can get to AlirezaAmir or AmirAlireza depending on the order of concatenation.
#
# Unfortunately enough, the teacher forgot to ask students to concatenate their strings in a pre-defined order so each student did it the way he/she liked.
#
# Now the teacher knows that Shapur is such a fast-calculating genius boy and asks him to correct the students' papers.
#
# Shapur is not good at doing such a time-taking task. He rather likes to finish up with it as soon as possible and take his time to solve 3-SAT in polynomial time. Moreover, the teacher has given some advice that Shapur has to follow. Here's what the teacher said:
#
# As I expect you know, the strings I gave to my students (including you) contained only lowercase and uppercase Persian Mikhi-Script letters. These letters are too much like Latin letters, so to make your task much harder I converted all the initial strings and all of the students' answers to Latin.
# As latin alphabet has much less characters than Mikhi-Script, I added three odd-looking characters to the answers, these include "-", ";" and "_". These characters are my own invention of course! And I call them Signs.
# The length of all initial strings was less than or equal to 100 and the lengths of my students' answers are less than or equal to 600
# My son, not all students are genius as you are. It is quite possible that they make minor mistakes changing case of some characters. For example they may write ALiReZaAmIR instead of AlirezaAmir. Don't be picky and ignore these mistakes.
# Those signs which I previously talked to you about are not important. You can ignore them, since many students are in the mood for adding extra signs or forgetting about a sign. So something like Iran;;-- is the same as --;IRAN
# You should indicate for any of my students if his answer was right or wrong. Do this by writing "WA" for Wrong answer or "ACC" for a correct answer.
# I should remind you that none of the strings (initial strings or answers) are empty.
# Finally, do these as soon as possible. You have less than 2 hours to complete this.
# Input
# The first three lines contain a string each. These are the initial strings. They consists only of lowercase and uppercase Latin letters and signs ("-", ";" and "_"). All the initial strings have length from 1 to 100, inclusively.
#
# In the fourth line there is a single integer n (0 ≤ n ≤ 1000), the number of students.
#
# Next n lines contain a student's answer each. It is guaranteed that the answer meets what the teacher said. Each answer iconsists only of lowercase and uppercase Latin letters and signs ("-", ";" and "_"). Length is from 1 to 600, inclusively.
#
# Output
# For each student write in a different line. Print "WA" if his answer is wrong or "ACC" if his answer is OK.
#
# Examples
# input
# Iran_
# Persian;
# W_o;n;d;e;r;f;u;l;
# 7
# WonderfulPersianIran
# wonderful_PersIAN_IRAN;;_
# WONDERFUL___IRAN__PERSIAN__;;
# Ira__Persiann__Wonderful
# Wonder;;fulPersian___;I;r;a;n;
# __________IranPersianWonderful__________
# PersianIran_is_Wonderful
# output
# ACC
# ACC
# ACC
# WA
# ACC
# ACC
# WA
# input
# Shapur;;
# is___
# a_genius
# 3
# Shapur__a_is___geniUs
# is___shapur___a__Genius;
# Shapur;;is;;a;;geni;;us;;
# output
# WA
# ACC
# ACC

str11 = input().strip().replace(';', '').replace('-', '').replace('_', '').lower()
str12 = input().strip().replace(';', '').replace('-', '').replace('_', '').lower()
str13 = input().strip().replace(';', '').replace('-', '').replace('_', '').lower()

n = int(input())
for i in range(n):
    ai = input().strip().replace(';', '').replace('-', '').replace('_', '').lower()
    if len(ai) != len(str11) + len(str12) + len(str13):
        print('WA')
        continue
    if (str11 + str12 + str13) == ai or (str11 + str13 + str12) == ai or (str12 + str11 + str13) == ai or (
            str12 + str13 + str11) == ai or (str13 + str11 + str12) == ai or (str13 + str12 + str11) == ai:
        print('ACC')
        continue
    print('WA')
