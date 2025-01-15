# 	DEFINE		
.eqv	readIndex	$t0	# index
.eqv	readValue	$t1	# value
.eqv	accumulated	$t4	# CharToInt 1
.eqv	digit		$t5	# CharToInt 2

.eqv	actualIndex	$t0 	# index
.eqv	actualValue	$t1	# value
.eqv	nextIndex	$t2	# index 2
.eqv	nextValue	$t3	# value 2
.eqv	ordered		$t4	# loop 1
.eqv	L1_lastIndex	$t5	# loop 1 range
.eqv	L2_lastIndex	$t6	# loop 2 range
.eqv	LENGHT		$s1	# int_list LENGHT

.eqv	writeIndex	$t0	# index
.eqv	number		$t1	# value
.eqv	bufferIndex	$t2	# index 2
.eqv	character	$t3	# value 2
.eqv	charIndex	$t4	# index 3
.eqv	remainder	$t5	# IntToChar 1
.eqv	quotient	$t6	# IntToChar 2
.eqv	flagSign	$t7	# flag

.eqv	fileDescriptor	$s2	# descriptor

.eqv 	aux		$t9	# auxíliar

.eqv	CHAR_READ	$s0	# loop CharToInt end condition
.eqv	CHAR_TO_WRITE	$s0	# char_list LENGHT
.eqv	CHAR_TO_READ	1024	# máx. de caracteres q podem ser lidos	

# 0 - DATA
.data
	# 1 - LEITURA 
	file_name1:	.asciiz "C:\\Users\\Gabriel\\Desktop\\lista.txt"
			.align 2
	buffer1:     	.space CHAR_TO_READ	# ESPAÇO RESERVADO PARA O BUFFER DE LEITURA
    	int_list:   	.space 1024		# ESPAÇO RESERVADO PARA A LISTA NÚMERICA
    	
    	# 3 - ESCRITA
	file_name2:	.asciiz	"C:\\Users\\Gabriel\\Desktop\\lista_ordenada.txt"
			.align	2
	buffer2:	.space	32		# ESPAÇO RESERVADO PARA O BUFFER DE CONVERSÃO PARA ESCRITA	
	char_list:	.space	CHAR_TO_READ	# ESPAÇO RESERVADO PARA A LISTA DE CARACTERES
	
.text

# 1 - LEITURA
# 1.1 - OPEN FILE
init:
	li	LENGHT,	0
	
	# OPEN FILE SYSCALL
    	li 	$v0, 	13                	
    	la 	$a0, 	file_name1        	
   	li 	$a1, 	0                	
    	li 	$a2, 	0                	
    	syscall
    	move 	fileDescriptor,	$v0      	

    	# READ FROM FILE SYSCALL
    	li 	$v0, 	14               	
   	move 	$a0, 	fileDescriptor        	
    	la 	$a1, 	buffer1           	
    	la 	$a2, 	CHAR_TO_READ   	
    	syscall

    	move 	CHAR_READ,	$v0              	

# 1.2 - CONVERSÃO DE CHAR PARA INT
CharToInt_init:
	li 	bufferIndex, 	0                	
    	li 	readIndex, 	0
    	
parse_buffer:
    	bge 	bufferIndex, 	CHAR_READ, 	end_parse

    	# LOAD CHAR
    	lb 	character, 	buffer1(bufferIndex)  		
    	addi 	bufferIndex, 	bufferIndex, 	1         	

    	# IGNORAR VÍRGULAS
    	li 	aux, 		0x2c	# ASCII ','
    	beq 	character, 	aux, 	parse_buffer		

   	# IDENTIFICAR NEGATIVO
    	li 	aux, 		0x2d	# ASCII '-'
    	beq 	character, 	aux, 	negative_number

    	# CONVERSÃO INIT
    	li 	accumulated,	0
    	li 	flagSign, 	0

parse_number:
    	# VERIFICAR SE CARACTERE É UM DÍGITO
	li 	aux, 		0x30               	# ASCII '0'
    	blt 	character, 	aux, 	store_number
    	li 	aux, 		0x39               	# ASCII '9'
    	bgt 	character, 	aux, 	store_number
	
    	# UPDATE accumulated ( accumulated = accumulated * 10 + (digit - '0') )
    	sub 	digit,		character, 	0x30	# '0' em ASCII
    	mul 	accumulated, 	accumulated, 	10
   	add 	accumulated, 	accumulated, 	digit

    	# LOAD NEXT CHAR
    	lb 	character, 	buffer1(bufferIndex)
    	addi 	bufferIndex, 	bufferIndex, 	1
    	j 	parse_number

negative_number:
    	# DEFINIR FLAG E SEGUIR PARA PRÓXIMO CARACTERE
   	li 	flagSign, 	1
    	lb 	character, 	buffer1(bufferIndex)
    	addi 	bufferIndex, 	bufferIndex, 	1
    	j 	parse_number

store_number:
    	# VERIFICAR flagSign
   	beq 	flagSign, 	0, 	positive_number
   	sub 	accumulated, 	$zero, 	accumulated

positive_number:
	# UPDATE int_list
	sw 	accumulated, 	int_list(readIndex)
    	addi 	readIndex, 	readIndex,	4
    	li 	accumulated, 	0
    	li 	flagSign, 	0
    	j 	parse_buffer

end_parse:
        # CLOSE FILE
        li 	$v0, 	16
	move 	$a0, 	fileDescriptor
	syscall
	
# 2 - BUBBLE SORT
# 2.1 - INIT
bubble_init:
	move	LENGHT, 	readIndex
	
	li	ordered, 	0
	sub	L1_lastIndex, 	LENGHT,		4
	
# 2.2 - ORDENAÇÃO
loop_1: 
	bge	ordered, 	L1_lastIndex, 		IntToChar_init
	sub	L2_lastIndex, 	L1_lastIndex, 		ordered
	li	actualIndex, 	0
	
loop_2:
	bge	actualIndex, 	L2_lastIndex, 		end_1
	
	# CONDIÇÃO
	lw	actualValue, 	int_list(actualIndex)
	add	nextIndex, 	actualIndex, 		4
	lw	nextValue, 	int_list(nextIndex)
	blt	actualValue, 	nextValue, 		end_2
	
	# TROCA
	sw	nextValue, 	int_list(actualIndex)
	sw	actualValue,	int_list(nextIndex)
	
end_2:
	add	actualIndex, 	actualIndex, 	4
	j	loop_2
	
end_1:
	add	ordered, 	ordered, 	4
	j	loop_1
	
# 3 - ESCRITA
# 3.1 - CONVERSÃO DE INT PARA CHAR
IntToChar_init:
	li	charIndex, 	0
	li	writeIndex, 	0
	
restart:
	li	flagSign, 	0
	li	bufferIndex, 	0
	
sign_test:
	bgt	writeIndex,	CHAR_TO_WRITE, 	write
	lw	number,		int_list(writeIndex)
	add	writeIndex, 	writeIndex, 	4
	
	# VERIFICAR NEGATIVO
	bge	number, 	$zero, 		convert
	li	flagSign, 	1
	li	aux, 		-1
	mul	number, 	number, 	aux
	
convert:
	# CONVERSÃO INIT
	move	quotient, number
	
next:
	# DIVISÕES POR 10
	li	aux,		10
	div	quotient, 	aux
	mfhi	remainder
	mflo	quotient
	# DÍGITO EM ASCII
	add	character, 	remainder, 0x30
	sb	character, 	buffer2(bufferIndex)
	add	bufferIndex, 	bufferIndex, 1
	bnez	quotient, 	next
	# NEGATIVO EM ASCII
	beqz	flagSign, 	ordering_digits
	li	aux, 		'-'
	sb	aux, 		buffer2(bufferIndex)
	add	bufferIndex, 	bufferIndex, 		1
	
ordering_digits:
	# UPDATE char_list
	beqz	bufferIndex, 	out
	add	bufferIndex, 	bufferIndex, 		-1
	lb	character, 	buffer2(bufferIndex)
	sb	character, 	char_list(charIndex)
	add	charIndex, 	charIndex, 		1
	j	ordering_digits
	
out:
	li	aux, 		','
	sb	aux, 		char_list(charIndex)
	add	charIndex, 	charIndex, 		1
	j	restart

# 3.2 - WRITE TO FILE
write:
	# OPEN FILE SYSCALL
	li	$v0,	13
	la	$a0,	file_name2
	li	$a1,	1
	li	$a2,	0
	syscall
	
	# WRITE TO FILE SYSCALL
	move	fileDescriptor,	$v0
	li	$v0,	15
	move	$a0,	fileDescriptor
	la	$a1,	char_list
	move	$a2,	CHAR_TO_WRITE
	syscall
	
close:
	# CLOSE FILE SYSCALL
	li	$v0,	16
	move	$a0,	fileDescriptor
	syscall
	
fim:
	li	$v0, 	10
	syscall


	
