#!/usr/bin/env python3


keyboard = \
[\
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],\
    ['tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '$\\backslash$', "|"],\
    ['caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", "enter"],\
    ['shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', "?", "shift"]\
]

print("\\documentclass{article}")
print("\\usepackage{tikz}")
print("\\begin{document}")

print("""\\newcommand{\\key}[5]{   %Obfruscated answer 
    \\fill[#5] (#2, #3) rectangle (#2+#4, #3-#4);
    \\draw (#2, #3) rectangle (#2+#4, #3-#4);
    \\node at (#2+#4*.5, #3-#4*.5) {#1}; %Changed these to rectangles
    }
""")

print("\\begin{tikzpicture}")
key_size = 1

def read_csv(filename):
    f = open(filename, "r")
    data = dict()
    line = f.readline()

    while line is not "":
        line_val = (line.split("\n")[0].split(","))
        data[line_val[1]] = line_val[0]
        line = f.readline()

    return data

len_data = 99
ratio = 10

def cap_at_100(n):
    if n > 100:
        return 100
    else:
        return n

def only_after_dash(data, letter):
    if len(letter) == 1 or letter == "<space>":
        a = []
        for j in data:
            if len(j) == 5 and '-' in j:
                a.append([j[3], data[j]])

        summation = 0
        for val in a:
            if letter in val[0]:
                summation += int(val[1])

        return "blue!" + str(cap_at_100(summation * ratio))
    else:
        return "white"


#print(only_after_dash(read_csv("results.csv"), "a"))

def print_row(xoffset, yoffset, keys):
    key_num = 0

    while key_num < len(keys):
        print("\\key" + \
                "{" + keys[key_num] + "}" \
                "{" + str(key_num + xoffset) + "}" \
                "{" + str(yoffset) + "}" \
                "{" + "1" + "}" \
                "{" + only_after_dash(read_csv("results.csv"), keys[key_num]) + "}" \
                ";"
                )
        key_num += 1

print_row(0, 3, keyboard[0])
print_row(0, 2, keyboard[1])
print_row(0, 1, keyboard[2])
print_row(0, 0, keyboard[3])

print("""
\\key{ctrl}{0}{-1}{1}{red}
\\key{alt}{1}{-1}{1}{red}
\\key{alt}{8}{-1}{1}{red}
\\key{ctrl}{9}{-1}{1}{red}
\\draw (0, -2)--(10, -2);
\\fill[blue!80] (2, -2) rectangle (8, -1);
""")


print("\\end{tikzpicture}\n\\end{document}")



