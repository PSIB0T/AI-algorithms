% Expert system should be started from here
main :-
  intro,
  reset_answers,
  troubleshoot_e(Error),
  describe(Error), nl.


intro :-
  write('Troubleshoot expert!'), nl,
  write('What is the error that you are facing?'), nl,
  write('To answer, input the number shown next to each answer, followed by a dot (.)'), nl, nl.


troubleshoot_e(Error) :-
  troubleshoot(Error), !.


% Store user answers to be able to track his progress
:- dynamic(progress/2).


% Clear stored user progress
% reset_answers must always return true; because retract can return either true
% or false, we fail the first and succeed with the second.
reset_answers :-
  retract(progress(_, _)),
  fail.
reset_answers.

% Rules for the knowledge base
troubleshoot(system_restore) :-
  what(bsod).

troubleshoot(system_restore) :-
  what(slow_pc),
  slow_pc_path_1(malicious_plugin).

troubleshoot(update_pc) :-
  what(slow_pc),
  slow_pc_path_1(not_upated).

troubleshoot(free_hdd) :-
  what(slow_pc),
  slow_pc_path_1(low_space).

troubleshoot(check_fan) :-
  what(overheating),
  overheating_path_1(fan_not_running).

troubleshoot(better_place) :-
  what(overheating),
  overheating_path_1(no_ventilation).

troubleshoot(contact_isp) :-
  what(net_not_working),
  internet_path_1(yes),
  internet_path_2(modem_not_setup).

troubleshoot(plugin_modem) :-
  what(net_not_working),
  internet_path_1(yes),
  internet_path_2(modem_not_plugged_in).

troubleshoot(power_on_sol) :-
  what(pc_not_starting),
  pc_not_starting_path_1(yes),
  pc_not_starting_path_2(power_on).

troubleshoot(reboot_sol) :-
  what(pc_not_starting),
  pc_not_starting_path_1(yes),
  pc_not_starting_path_2(reboot).

troubleshoot(load_reboot_sol) :-
  what(pc_not_starting),
  pc_not_starting_path_1(yes),
  pc_not_starting_path_2(load_reboot).


% Questions for the knowledge base
question(what) :-
  write('What is the error that you are facing?'), nl.

question(slow_pc_path_1) :-
  write('Which one of the foll options apply to you?'), nl.

question(internet_path_1) :-
  write('Did you try restarting?'), nl.

question(internet_path_2) :-
  write('Which one of the foll options apply to you?'), nl.

question(pc_not_starting_path_1) :-
  write('Is it plugged in?'), nl.

question(pc_not_starting_path_2) :-
  write('Which one of the foll options apply to you?'), nl.

question(overheating_path_1) :-
  write('Which one of the foll options apply to you?'), nl.

% Answers for the knowledge base
answer(slow_pc) :-
  write('Slow PC').

answer(overheating) :-
  write('Overheating').

answer(net_not_working) :-
  write('Internet not working').

answer(pc_not_starting) :-
  write('PC not starting').

answer(bsod) :-
  write('BSOD').

answer(malicious_plugin) :-
  write('Installed a malicious plugin').

answer(not_upated) :-
  write('Haven\'t updated my PC recently').

answer(low_space) :-
  write('Low hard drive space').

answer(fan_not_running) :-
  write('Fan is not running').

answer(no_ventilation) :-
  write('CPU does not have proper ventilation').

answer(yes) :-
  write('Yes').

answer(no) :-
  write('No').

answer(modem_not_setup) :-
  write('Modem not properly setup').

answer(modem_not_plugged_in) :-
  write('Modem is not plugged in').

answer(power_on) :-
  write('Computer Powers On but Nothing Happens').

answer(reboot) :-
  write('Computer Stops or Continuously Reboots During the POST').

answer(load_reboot) :-
  write('Windows Begins to Load but Stops or Reboots Without an Error').

% Solution descriptions for the knowledge base
describe(system_restore) :-
  write('System Restore'), nl,
  write('You gotta do a system restore in this case'), nl.

describe(update_pc) :-
  write('Upate PC'), nl,
  write('You gotta update your PC'), nl.

describe(free_hdd) :-
  write('Free HDD'), nl,
  write('You gotta free your hard disk'), nl.

describe(check_fan) :-
  write('Check fan'), nl,
  write('Check whether the fans are unplugged / wiring issues'), nl.

describe(better_place) :-
  write('Better place'), nl,
  write('Move the PC to a better place'), nl.

describe(contact_isp) :-
  write('Contact ISP'), nl,
  write('Contact your ISP'), nl.

describe(plugin_modem) :-
  write('Plugin modem'), nl,
  write('Plugin your modem'), nl.

describe(power_on_sol) :-
  write('Solution for part 1'), nl,
  write('...'), nl.

describe(reboot_sol) :-
  write('Solution for part 2'), nl,
  write('...'), nl.

describe(load_reboot_sol) :-
  write('Solution for part 3'), nl,
  write('...'), nl.




% Assigns an answer to questions from the knowledge base
slow_pc_path_1(Answer) :-
  progress(slow_pc_path_1, Answer).
slow_pc_path_1(Answer) :-
  \+ progress(slow_pc_path_1, _),
  ask(slow_pc_path_1, Answer, [malicious_plugin, not_upated, low_space]).

what(Answer) :-
  progress(what, Answer).
what(Answer) :-
  \+ progress(what, _),
  ask(what, Answer, [slow_pc, overheating, net_not_working, pc_not_starting, bsod]).

overheating_path_1(Answer) :-
  progress(overheating_path_1, Answer).
overheating_path_1(Answer) :-
  \+ progress(overheating_path_1, _),
  ask(overheating_path_1, Answer, [fan_not_running, no_ventilation]).

internet_path_1(Answer) :-
  progress(internet_path_1, Answer).
internet_path_1(Answer) :-
  \+ progress(internet_path_1, _),
  ask(internet_path_1, Answer, [yes, no]).

internet_path_2(Answer) :-
  progress(internet_path_2, Answer).
internet_path_2(Answer) :-
  \+ progress(internet_path_2, _),
  ask(internet_path_2, Answer, [modem_not_setup, modem_not_plugged_in]).

pc_not_starting_path_1(Answer) :-
  progress(pc_not_starting_path_1, Answer).
pc_not_starting_path_1(Answer) :-
  \+ progress(pc_not_starting_path_1, _),
  ask(pc_not_starting_path_1, Answer, [yes, no]).

pc_not_starting_path_2(Answer) :-
  progress(pc_not_starting_path_2, Answer).
pc_not_starting_path_2(Answer) :-
  \+ progress(pc_not_starting_path_2, _),
  ask(pc_not_starting_path_2, Answer, [power_on, reboot, load_reboot]).

% Outputs a nicely formatted list of answers
% [First|Rest] is the Choices list, Index is the index of First in Choices
answers([], _).
answers([First|Rest], Index) :-
  write(Index), write(' '), answer(First), nl,
  NextIndex is Index + 1,
  answers(Rest, NextIndex).


% Parses an Index and returns a Response representing the "Indexth" element in
% Choices (the [First|Rest] list)
parse(0, [First|_], First).
parse(Index, [First|Rest], Response) :-
  Index > 0,
  NextIndex is Index - 1,
  parse(NextIndex, Rest, Response).


% Asks the Question to the user and saves the Answer
ask(Question, Answer, Choices) :-
  question(Question),
  answers(Choices, 0),
  read(Index),
  parse(Index, Choices, Response),
  asserta(progress(Question, Response)),
  Response = Answer.