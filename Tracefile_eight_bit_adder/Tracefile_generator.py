# Python script for generation of a tracefile for terror-string-recognizer-fsm.
#
# You may modify it suitably to prepare script for tracefile-generation for
#  your odd-parity-coronavirus-recognizer-fsm
#
# --- Sachin B. Patkar ( for ee-214-spring-sem-2019-2020 , 13th March 2020 )



#
#   i0 : excess3up_fsm	port map (
#			clk => input_vector(6),
#			r   => input_vector(5),
#			X   => input_vector(4 downto 0),
#			W   => output_vector(0));

f=open("TRACEFILE_strrecog_fsm.txt","w")
f.write("0100000 0 0\n");
f.write("1100000 0 0\n");

str="lllclllollllrllllollnllllallcorlllonllallcoronllllallll"
N = len(str)

st_corona=0


for i in range(N) :
    c=str[i];
    y = 0
    if ( c=='c' ) :
        if ( st_corona==0 or st_corona==6 or st_corona==12) : st_corona = st_corona+1
    elif ( c=='o' ) :
        if ( st_corona==1 ) : st_corona = 2
        if ( st_corona==3 ) : st_corona = 4
        if (st_corona==7) : st_corona = 8
        if (st_corona==9) : st_corona = 10
    elif ( c=='r' ) :
        if ( st_corona==2 ) : st_corona = 3
        if(st_corona==8) : st_corona = 9
    elif ( c=='n' ) :
        if ( st_corona == 4 ) : st_corona = 5
        if (st_corona == 10 ) : st_corona = 11
    elif ( c=='a' ) :
        if ( st_corona==5 ) :
            st_corona = 6
            y = 1
        if (st_corona==11) : st_corona = 12
    else :
        pass

    f.write("00")
    if ( c==' ' ) :
        f.write("00000" )
    else :
        f.write("{:05b}".format( ord(c)-96 ))
    if ( y == 1 ) :
        f.write(" 1 1\n")
    else :
        f.write(" 0 1\n")

    f.write("10")
    if ( c==' ' ) :
        f.write("00000" )
    else :
        f.write("{:05b}".format( ord(c)-96 ))
    f.write(" 0 0\n")
    if ( st_corona==13 ) : st_corona=1

f.close()

