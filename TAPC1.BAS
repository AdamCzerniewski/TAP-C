100 REM TAPC1
120 CLS
140 PRINT TAB(5);"RESISTANCE MATCHING - TAPPED CAPACITOR"
160 PRINT
180 PRINT TAB(10);"PASSBAND CENTER FRQ (MHz)";:INPUT F
200 PRINT
220 W=F*6280000!
240 PRINT TAB(10);"INSERTION LOSS";:INPUT IL
260 IF IL=0 THEN IL=.00001
280 PRINT
300 IL=10^(-IL/10)
320 PRINT TAB(10);"R1 in ohm";:INPUT RS
340 PRINT TAB(10);"Rt in ohm";:INPUT RL
360 IF RS<RL THEN K=SQR(RL/RS)-1
380 IF RS>RL THEN K=SQR(RS/RL)-1
400 IF RS<RL THEN X=2*RL*SQR(-1+1/IL)
420 IF RS>RL THEN X=2*RS*SQR(-1+1/IL)
440 L=X/(W*K)
460 C2=(1+K)*K*K*L/X^2
480 C1=C2/K
500 PRINT
520 PRINT TAB(10);"C1=";INT(C1*10^13)/10;"pF"
540 PRINT
560 PRINT TAB(10);"C2=";INT(C2*10^13)/10;"pF"
580 PRINT
600 PRINT TAB(10);" L=";INT(L*10^9)/1000;"uH"
620 PRINT
640 PRINT
660 IF RS<RL THEN B$="C2"
680 IF RS<RL THEN C$="L"
700 IF RS>RL THEN B$="L"
720 IF RS>RL THEN C$="C2"
740 PRINT TAB(7);"     -----o----o--- C1 ---o-----"
760 PRINT TAB(7);"    |          |          |     |"
780 PRINT TAB(7);"    |          |          |     |"
800 PRINT TAB(7);"   R1        ";B$;"         ";C$;"      Rt"
820 PRINT TAB(7);"    |          |          |     |"
840 PRINT TAB(7);"    |          |          |     |"
860 PRINT TAB(7);"     -----o----o----------o-----
880 PRINT
900 PRINT TAB(10);"press RETURN for next";:INPUT T
920 CLS
940 PRINT TAB(10);"Fmin,Fmax,step (MHz)";:INPUT F1,F2,FS
960 PRINT:PRINT:PRINT
980 GOTO 1200
1000 LPRINT
1020 IF H$="G" THEN PRINT
1040 IF H$="T" THEN 1120
1060 IF H$="G" THEN LPRINT TAB(13);"-60";TAB(33);"-40";TAB(53);"-20";TAB(74);"0"
1080 LPRINT TAB(13);"-+-------------------+-------------------+-------------------+--"
1100 IF H$="G" THEN 1280
1120 LPRINT TAB(10);"C1=";INT(C1*10^13)/10;TAB(22);"C2=";INT(C2*10^13)/10;TAB(36);"L=";INT(L*10^9)/1000;"uH"
1140 LPRINT
1160 LPRINT TAB(2);"F";TAB(27);"Zin";TAB(45);"IL"
1180 LPRINT
1200 PRINT TAB(2);"F";TAB(15);"Zin";TAB(35);"IL"
1220 PRINT TAB(1);"MHz";TAB(15);"ohm";TAB(35);"dB"
1240 PRINT
1260 W1=F1*6280000!:W2=F2*6280000!:WS=FS*6280000!
1280 FOR W=W1 TO W2 STEP WS
1300 IF RS>RL THEN 1600
1320 XL=W*L
1340 D1=XL*XL+RL*RL
1360 R1=XL*XL*RL/D1
1380 X1=XL*RL*RL/D1
1400 X2=-1/(W*C1)+X1
1420 XC=-1/(W*C2)
1440 D2=R1*R1+(X2+XC)^2
1460 D2=D2*(RL*RL+XL*XL)^2
1480 R2=-RL*XL*XL*XC*XC*(XL*XL+RL*RL)
1500 D2=-D2
1520 R2=R2/D2
1540 X3=-XC*(RL^2*(RL^2*X2*(XC+X2)+XL^2*(2*X2*(XC+X2)+XL^2))+XL^4*X2*(XC+X2))
1560 X3=X3/D2
1580 GOTO 1760
1600 REM RS>RL
1620 D1=1+(W*C2*RL)^2
1640 XO=-1/(W*C1)
1660 R1=RL/D1:X1=-W*C2*RL*RL/D1
1680 X2=XO+X1
1700 D2=R1*R1+(X2+W*L)^2
1720 R2=R1*(W*L)^2/D2
1740 X3=W*L*(R1*R1+X2*X2+W*L*X2)/D2
1760 N1=4*RS*R2
1780 D3=(RS+R2)^2+X3^2
1800 IL1=10*LOG(N1/D3)/LOG(10)
1820 IF X3<0 THEN B$="-j"
1840 IF X3>=0 THEN B$="+j"
1860 X3=ABS(INT(100*X3)/100)
1880 R2=INT(100*R2)/100
1900 IL1=INT(100*IL1)/100
1920 IL2=74+IL1
1940 IF H$="G" THEN LPRINT W/(6280000!);TAB(IL2);"*":GOTO 2040
1960 IF H$="T" AND PR=1 THEN 2000
1980 IF PR=0 THEN 2040
2000 LPRINT W/(6280000!);TAB(22);R2;B$;X3;TAB(44);IL1
2020 IL2=75+IL1
2040 PRINT W/(6280000!);TAB(12);R2;B$;X3;TAB(35);IL1
2060 NEXT W
2080 IF H$="G" THEN LPRINT TAB(13);"-+-------------------+-------------------+-------------------+--"
2100 IF H$="G" THEN LPRINT TAB(13);"-60";TAB(33);"-40";TAB(53);"-20";TAB(74);"0"
2120 PRINT:PRINT
2140 PRINT TAB(10);"HARD COPY - Table or Graph (T/G)";:INPUT H$
2160 IF H$<>"N" THEN PR=1:GOTO 1000
2180 PRINT
2200 PRINT TAB(10);"Do you want to change C1,C2 or L";:INPUT K$
2220 PRINT:PRINT
2240 IF K$="C1" THEN 2360
2260 IF K$="C2" THEN 2420
2280 IF K$="L" THEN 2480
2300 IF K$="N" THEN 920
2320 GOTO 100
2340 PRINT:PRINT
2360 PRINT TAB(10);"C1 in pF";:INPUT C1
2380 C1=C1*1E-12
2400 GOTO 2520
2420 PRINT TAB(10);"C2 in pF";:INPUT C2
2440 C2=C2*1E-12
2460 GOTO 2520
2480 PRINT TAB(10);" L in uH";:INPUT L
2500 L=L*.000001
2520 CLS
2540 PRINT:PRINT
2560 PRINT TAB(10);"C1=";INT(C1*1E+13+.5258
2580 PRINT
2600 PRINT TAB(10);"C2=";INT(C2*1E+13+.5262
2620 PRINT
2640 PRINT TAB(10);" L=";L*1000000!
2660 GOTO 2180
2680 END

