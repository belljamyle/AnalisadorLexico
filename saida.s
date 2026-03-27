.global _start

_start:
   MOV R0, #5
   MOV R1, #2
   MOV R2, #0
   div_loop_1:
   CMP R0, R1
   BLT div_end_1
   SUB R0, R0, R1
   ADD R2, R2, #1
   B div_loop_1
   div_end_1:
   MOV R0, R2
   MOV R0, #3
   MOV R1, #4
   ADD R0, R0, R1
   MOV R0, #10
   MOV R1, #2
   MOV R2, #0
   div_loop_2:
   CMP R0, R1
   BLT div_end_2
   SUB R0, R0, R1
   ADD R2, R2, #1
   B div_loop_2
   div_end_2:
   MOV R0, R2
   MOV R0, #6
   MOV R1, #3
   MUL R0, R0, R1
   MOV R0, #8
   MOV R1, #3
   SUB R0, R0, R1
   MOV R0, #2
   MOV R1, #3
   MUL R0, R0, R1
   MOV R2, #4
   MOV R3, #5
   MUL R2, R2, R3
   MOV R4, #0
   div_loop_3:
   CMP R0, R2
   BLT div_end_3
   SUB R0, R0, R2
   ADD R4, R4, #1
   B div_loop_3
   div_end_3:
   MOV R0, R4
   MOV R0, #10
   MOV R1, #2
   ADD R0, R0, R1
   MOV R2, #3
   MOV R3, #4
   ADD R2, R2, R3
   MUL R0, R0, R2
   MOV R0, #7
   MOV R1, #2
   SUB R0, R0, R1
   MOV R2, #5
   MOV R3, #3
   ADD R2, R2, R3
   MOV R4, #0
   div_loop_4:
   CMP R0, R2
   BLT div_end_4
   SUB R0, R0, R2
   ADD R4, R4, #1
   B div_loop_4
   div_end_4:
   MOV R0, R4
   MOV R0, #9
   MOV R1, #3
   MOV R2, #0
   div_loop_5:
   CMP R0, R1
   BLT div_end_5
   SUB R0, R0, R1
   ADD R2, R2, #1
   B div_loop_5
   div_end_5:
   MOV R0, R2
   MOV R0, #2
   MOV R1, #3
   MOV R2, R0
   SUB R1, R1, #1
   loop_6:
   CMP R1, #0
   BEQ end_6
   MUL R2, R2, R0
   SUB R1, R1, #1
   B loop_6
   end_6:
   MOV R0, #2
   MOV R1, #3
   ADD R0, R0, R1
   MOV R2, #4
   MOV R3, #5
   ADD R2, R2, R3
   MUL R0, R0, R2
   MOV R0, #8
   MOV R1, #2
   MOV R2, #0
   div_loop_7:
   CMP R0, R1
   BLT div_end_7
   SUB R0, R0, R1
   ADD R2, R2, #1
   B div_loop_7
   div_end_7:
   MOV R0, R2
   MOV R3, #3
   MOV R4, #1
   ADD R3, R3, R4
   MUL R0, R0, R3
   MOV R0, #5
   MOV R1, #5
   MUL R0, R0, R1
   MOV R2, #10
   MOV R3, #2
   MOV R4, #0
   div_loop_8:
   CMP R2, R3
   BLT div_end_8
   SUB R2, R2, R3
   ADD R4, R4, #1
   B div_loop_8
   div_end_8:
   MOV R2, R4
   ADD R0, R0, R2
   MOV R0, #1
   MOV R0, #5
   MOV R10, R0

end:
   B end
