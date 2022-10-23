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

		if((format_string[i] == '#') && (format_string[i+1] == 'k')){
			i++;
			change(param);
		} else if ((format_string[i] == '#') && isdigit(format_string[i+1])){
			int sec_place = i + 1;
			char sign = format_string[sec_place];
			int leng = 0;
			while (sign >= '0' && sign <='9' && sec_place <= strlen(format_string)){
				leng = leng * 10 + (sign - '0');
				sec_place++;
				sign = format_string[sec_place];
			}
			if (sign != 'k'){
				putchar(format_string[i]);
				continue;
			}
			i = sec_place;
			if (leng > strlen(param)){
				for (int j=0; j<leng-strlen(param); j++){
					putchar(' ');
				}
				change(param);
			} else {
				change(param);
			}
			
		} else if ((format_string[i] == '#') && (format_string[i+1] == '.') && isdigit(format_string[i+2])){
			int sec_place = i + 2;
			char sign = format_string[sec_place];
			int leng = 0;
			while (sign >= '0' && sign <='9' && sec_place <= strlen(format_string)){
				leng = leng * 10 + (sign - '0');
				sec_place++;
				sign = format_string[sec_place];
			}
			if (sign != 'k'){
				putchar(format_string[i]);
				continue;
			}
			i = sec_place;
			
			for (int l=0; l < leng; l++){
				if (l >= strlen(param)) break;
				char letter = param[l];
				int letter_number = (int) letter;
				if (letter_number >=65 && letter_number <= 90) {
					letter_number = letter_number + 32;
				} else if (letter_number >=97 && letter_number <=122){
					letter_number = letter_number - 32;
				}
				putchar(letter_number);

			}
		} else {
			putchar(format_string[i]);
		}
			
	}
	puts("");
	return 0;
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}