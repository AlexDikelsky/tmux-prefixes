#!/usr/bin/env python3

keyboard = \
[\
    ['\\`{}', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],\
    ['tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '$\\backslash$', "|"],\
    ['caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", "enter"],\
    ['shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', "?", "shift"]\
]

print("\\documentclass{article}")
print("\\usepackage{tikz}")
print("\\begin{document}")

print("""\\newcommand{\\key}[4]{   %Obfruscated answer
    \\draw (#2, #3)--(#2+#4, #3)--(#2+#4, #3-#4)--(#2, #3-#4)--(#2, #3);
    \\node at (#2+#4*.5, #3-#4*.5) {#1};
    }
""")

print("\\begin{tikzpicture}")
key_size = 1
def print_row(xoffset, yoffset, keys):
    key_num = 0

    while key_num < len(keys):
        print("\\key" + \
                "{" + keys[key_num] + "}" \
                "{" + str(key_num + xoffset) + "}" \
                "{" + str(yoffset) + "}" \
                "{" + "1" + "}"\
                ";"
                )
        key_num += 1

print_row(0, 3, keyboard[0])
print_row(0, 2, keyboard[1])
print_row(0, 1, keyboard[2])
print_row(0, 0, keyboard[3])

print("""
\\key{ctrl}{0}{-1}{1}
\\key{meta}{1}{-1}{1}
\\key{meta}{8}{-1}{1}
\\key{ctrl}{9}{-1}{1}
\\draw (0, -2)--(10, -2);
""")


print("\\end{tikzpicture}\n\\end{document}")

