/*
Generates random password
using /dev/urandom device file in linux
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define PROGRAM_NAME "passgen"
#define MAX_LEN 32
#define MIN_LEN 8

/*
if c is not in symbs return 1, else return 0
c - char to test
symbs - string containing symbols
symbs_len - length of symbs
*/
int not_in(char c, char* symbs, size_t symbs_len) {
	for(int i = 0; i < symbs_len; i++) {
		if(c == symbs[i]) {
			return 0;
		}
	}
	return 1;
}

int main(int argc, char* argv[]) {
	if(argc != 2) {
		fprintf(stdout, "Usage: %s PASSWORD_LENGTH\n", PROGRAM_NAME);
		exit(0);
	}

	int pass_len = atoi(argv[1]);
	if(pass_len < MIN_LEN || pass_len > MAX_LEN || pass_len == 0) {
		fprintf(stderr, "Password lenght is integer between %d and %d.\n", MIN_LEN, MAX_LEN);	
		exit(1);
	}

	char buff[pass_len];	
	FILE *fp = NULL;

	fp = fopen("/dev/urandom", "r");
	if(fp == NULL) {
		fprintf(stderr, "Error opening /dev/urandom");
		exit(1);
	}

	char c;
	unsigned int i = 0;
	while(i < pass_len) {
		c = getc(fp);
		if(isprint((int) c) && not_in(c, " \"`'|.~,:()[]{}+*-^;><?!/\\", 26)) {
			buff[i] = c;
			i++;
		}
	}
	
	for(int i = 0; i < pass_len; i++) {
		printf("%c", buff[i]);
	}
	printf("\n");

	fclose(fp);
	return 0;
}
