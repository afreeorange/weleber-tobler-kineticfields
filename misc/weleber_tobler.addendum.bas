100 REM Program lines that alter the original so that
110 REM distances, RD, and directions, TD, can be 
120 REM entered from the keyboard. Lines 165, 250,
130 and 260 must be deleted.
190 PRINT "PAIR","DISTANCE (RD), DIRECTION (TD)"
200 PRINT ,"AS RD,TD"
210 FOR I=1 TO N
220     IF I<10 THEN PRINT " ";
230     PRINT I;:INPUT "            ";RD(I),TD(I)
240 NEXT I