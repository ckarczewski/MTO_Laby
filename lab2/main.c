#include <stdio.h>
#include <string.h>
#include <ctype.h>

void change (char *param){
	for(int j=0; j<strlen(param); j++){
				char letter = param[j];
				int letter_number = (int) letter;
				if (letter_number >=65 && letter_number <= 90) {
					letter_number = letter_number + 32;
				} else if (letter_number >=97 && letter_number <=122){
					letter_number = letter_number - 32;
				}
				putchar(letter_number);
			}
}

int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if (format_string[i] != '#') {
			putchar(format_string[i]);
			continue;
		}
		if((format_string[i] == '#') && (format_string[i+1] == 'k')){
			i++;
			change(param);
		}
		if ((format_string[i] == '#') && (format_string[i+1] == '.') && isdigit(format_string[i+2]) && format_string[i+3] == 'k'){
			int sec_i = i + 2;
			char test = format_string[sec_i];
			int leng = 0;
			while (test >= '0' && test <='9' && sec_i < strlen(format_string)){
				leng = leng * 10 + (test - '0');
				sec_i++;
				test = format_string[sec_i];
			}
			i = sec_i;
			change(param);
			for (int l=0; l < leng; l++){
				if (l >= strlen(param)) break;
				putchar(param[l]);
			}
		} 
			
	}
	puts("");
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}
