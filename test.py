import sys
from colorama import Fore, Style
import os
from subprocess import Popen, PIPE, STDOUT

file_name = sys.argv[1]

if len(sys.argv) == 3:
    tests_name = sys.argv[2]
else:
    tests_name = sys.argv[1].rsplit(".")[0] + ".test"

prolog_header = f""":- [{file_name.rsplit(".")[0]}].

tests([]).
tests([H|T]) :- run_test(H), tests(T).

run_test(H) :- H, write(H), write(':P;').
run_test(H) :- not(H), write(H), write(':F;').

"""

tests = open(tests_name).read()

test_sentences = []
for test in tests.lower().splitlines():
    negate = False
    if test[0] == "*":
        test = test[1:]
        negate = True

    if (negate, test) in test_sentences:
        print(f"Duplicate: {test}")
        continue
    test_sentences.append((negate, test))
test_sentences.sort()

file = prolog_header
test_names = []
for (i, (negate, sentence)) in enumerate(test_sentences):
    if negate:
        file += f"t{i} :- not(s(_, {sentence.split(' ')}, [])).\n"
    else:
        file += f"t{i} :- s(_, {sentence.split(' ')}, []).\n"
    test_names.append(f"t{i}")

predicate = f"tests([{','.join(test_names)}])."

open_file = open("test.pl", "w")
open_file.write(file)
open_file.close()

prolog = Popen(["swipl", "test.pl"], stdin=PIPE, stdout=PIPE, stderr=STDOUT, text=True)

stdout_data = prolog.communicate(input=predicate)[0]

result_line = ""
for line in stdout_data.splitlines():
    if ";" in line:
        result_line = line
        break

if result_line == "":
    print(stdout_data)
    os.remove("test.pl")
    quit()

prolog_out = result_line.strip().split(";")[:-1]


test_results = ([], [])
for result in prolog_out:
    name, success = result.split(":")

    negate, sentence = test_sentences[int(name[1:])]

    neg = ["", f"{Fore.RED}[NEG] {Style.RESET_ALL}"][negate]

    if success == "P":
        test_results[0].append(f"{neg}{sentence} --> {Fore.GREEN}Passed{Style.RESET_ALL}")
    else:
        test_results[1].append(f"{neg}{sentence} --> {Fore.RED}Failed{Style.RESET_ALL}")

print(f"Tests:")
print(f"{len(test_results[0])} {Fore.GREEN}Passed{Style.RESET_ALL}")
print(f"{len(test_results[1])}{Fore.RED} Failed{Style.RESET_ALL}")
for t in test_results[0] + test_results[1]:
    print(t)

os.remove("test.pl")