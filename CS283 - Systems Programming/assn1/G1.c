#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <unistd.h>

create a data structure which has all these attributes

const char delim_nl[2] = "\n";
const char delim_com[2] = ",";

struct Node {
	char *data;
	struct Node * next;
};

struct List {
	struct Node *head;
	struct Node *tail;
};

char * fileReader(char *fileName){
	FILE * fd;
        fd = fopen(fileName, "r");
        char *buffer;
        buffer = malloc(256*sizeof(char));
        fread (buffer, 256, 1, fd);
	return buffer;
}

void listParser(char *fileName, ){
	FILE * fd;
	fd = fopen(fileName, "r");
	char *buffer;
	buffer = malloc(256*sizeof(char));
	fread (buffer, 256, 1, fd);
	
}

void create_f(string fileName, char ** fields, int n){
	FILE * pFile;
	pFile = fopen(fileName, "a"); //can use w, but will truncate everything in the file
	for(int i = 0; field
	fwrite(fields, sizeof(char), sizeof(fields), pFile);
	fclose(pFile);
}

void select_f(char* fileName, char* checkField, char* value){
	char * buffer;
	buffer = malloc(256*sizeof(char));
	buffer = fileReader(fileName);
	char *line_token;
	
	line_token = strtok(buffer, delim_nl);
	char *print_line_token;
	strcpy(print_line_token, line_token);
	char *attr_token;
	attr_token = strtok(line_token, delim_com);
	int checkFieldCount = 0;
	while(attr_token != NULL){
		printf("%s | ", attr_token);
		attr_token = strtok(print_line_token, delim_com);
	}
	
	while(attr_token != NULL){
		char example1[50];
		char example2[50];
		strcpy(example1, attr_token);
		strcpy(example2, checkField);
		result = strcmp(example1, example2);
		if(result == 0){
			break;
		}
		attr_token = strtok(NULL, delim_com);
		checkFieldCount++;
	}
	
	while(line_token != NULL){
		char *copy_line_token;

		line_token = strtok(NULL, delim_com);

		strcpy(copy_line_token, line_token);

		for(int i = 0; i < checkFieldCount; i++){
			attr_token = strtok(copy_line_token, delim_com);
		}
		
		char example1[50];
                char example2[50];
                strcpy(example1, attr_token);
                strcpy(example2, value);
                result = strcmp(example1, example2);
                if(result == 0){
			attr_token = strtok(line_token, delim_com);
			printf("%s | ", attr_token);
                }
	}
	
	fopen() fileName
	read every line
	strcmp to compare the value to the field in the line
	read the first line first, to know about the columns
}

void delete_f(){

}

void update_f(char* fileName, char* updateField, char* updateValue, char* checkField, char* checkValue){
	char * buffer;
        buffer = malloc(256*sizeof(char));
        buffer = fileReader(fileName);
        char *line_token;

        line_token = strtok(buffer, delim_nl);
	char* updateLineCopy;
	char* checkLineCopy;
	strcpy(updateLineCopy, line_token);
	strcpy(checkLineCopy, line_token);
        char *attr_token;
	
	int updateFieldCount = 0;
	int checkFieldCount = 0;
	
	attr_token = strtok(checkLineCopy, delim_com);
	while(attr_token != NULL){//get the index for column value to be checked with the condition
		char example1[50];
		char example2[50];
		strcpy(example1, attr_token);
		strcpy(example2, checkField);
		result = strcmp(example1, example2);
		if(result == 0){
			break;
		}
		attr_token = strtok(NULL, delim_com);
		checkFieldCount++;
	}
	
	attr_token = strtok(updateLineCopy, delim_com);
	while(attr_token != NULL){//get the index of the column that has to be updated
		char example1[50];
                char example2[50];
                strcpy(example1, attr_token);
                strcpy(example2, checkField);
                result = strcmp(example1, example2);
                if(result == 0){
                        break;
                }
                attr_token = strtok(NULL, delim_com);
                updateFieldCount++;
	}
	
	FILE * fd;
	fd = fopen("temp", "w+");
	char *writeBuffer;
	
	while(line_token != NULL){//loops through the lines, then writes token by token to a temp file
		char *copy_line_token;
		strcpy(copy_line_token, line_token);
		for(int i = 0; i < checkFieldCount; i++){
			//fwrite(attr_token, 1, sizeof(attr_token), fd);
			//fwrite(delim_com, 1, sizeof(delim_com), fd);
			attr_token = strtok(copy_line_token, delim_com);
		}
		char example1[50];
		char example2[50];
		strcpy(example1, attr_token);
		strcpy(example2, checkValue);
		result = strcmp(example1, example2);
		if(result == 0){
			for(int i = 0; i < updateFieldCount; i++){
				attr_tok = strtok(line_token, delim_com);
				fwrite(attr_tok, 1, sizeof(attr_tok), fd);
				fwrite(delim_com, 1, sizeof(attr_tok), fd);
			}
			fwrite(updateValue, 1, sizeof(updateValue), fd);
			fwrite(delim_com, 1, sizeof(delim_com), fd);
			while(attr_token != NULL){
				attr_token = strtok(line_token, delim_com);
				fwrite(attr_tok, 1, sizeof(attr_tok), fd);
				fwrite(delim_com, 1, sizeof(delim_com), fd);
			}
			fwrite(delim_nl, 1, sizeof(delim_nl), fd);
		}
		else{
			while(attr_token != NULL){
				attr_token = strtok(line_token, delim_com);
				fwrite(attr_tok, 1, sizeof(attr_tok), fd);
				fwrite(delim_com, 1, sizeof(delim_com), fd);
			}
		}
		
		
	}
}

void insert_f(){
	
}

void drop_f(char* fileName){
	unlink(fileName);
}

	//we don't use argv becasue we don't know when one command ends and other begins

int main(int argc, char **argv){
	int i = 1;
	int j = 0;
	if(strcmp(argv[1],"CREATE")==0){
		do_create(argv[3], argv[4]);
	}
	else if(strcmp(argv[1], "SELECT")==0){
		do_select(argv[4], argv[6], argv[8]);
	}
	else if(strcmp(argv[1], "DELETE")==0){
		do_delete(argv[3], argv[5], argv[7]);
	}
	else if(strcmp(argv[1], "UPDATE")==0){
		do_update(argv[2], argv[4], argv[6], argv[8], argv[10]);
	}
	else if(strcmp(argv[1], "INSERT")==0){
		do_insert(argv[3], argv[4], argv[6]);
	}
	else if(strcmp(argv[1], "DROP")==0){
		do_drop(argv[2]);
	}
}

