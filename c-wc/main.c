#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

int main(int argc, char **argv) {
  int c;
  unsigned int line = 0, word = 0, byte = 0;
  bool prev_is_space = false, is_space = false, is_tail = false;

  while ((c = getchar()) != EOF) {
    byte++;
    is_space = isspace(c);

    if (is_space && !prev_is_space && is_tail) {
      word++;
    }
    if (c == '\n') {
      line++;
    }

    prev_is_space = is_space;
    is_tail = true;
  }

  printf("%d %d %d\n", line, word, byte);
  return 0;
}
