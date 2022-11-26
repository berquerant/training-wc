#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

int main(int argc, char **argv) {
  int c, line = 0, word = 0, byte = 0;
  bool prev_is_space = false, is_space = false, is_tail = false,
       met_char = false;

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
    if (!met_char && !is_space) {
      met_char = true;
    }
  }

  printf("%d %d %d\n", line, word, byte);
  return 0;
}
