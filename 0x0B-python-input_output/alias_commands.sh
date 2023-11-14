#!/bin/bash
alias sendit="git add . && git commit -m 'project 2' && git push"
alias runit="chmod u+x"
alias pycommand="echo -e '#!/usr/bin/python3\n\ndef main():\n\n\nif __name__ == \"__main__\":\n    main()'"
alias gccstd="gcc -Wall -Werror -Wextra -pedantic -std=gnu89"
alias gccmain="gcc -Wall -Werror -Wextra -pedantic -std=gnu89 main.c"
alias gccdebug="gcc -Wall -Werror -Wextra -pedantic -std=gnu89 -g"
alias debug="gdb ./a.out"
alias leaks="valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes -s"
