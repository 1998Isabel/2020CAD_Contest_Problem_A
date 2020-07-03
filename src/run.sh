BASEDIR=$(pwd)

cd $1
python $BASEDIR/utils/transfer.py gf.v
python $BASEDIR/utils/transfer.py rf.v

yosys -s $BASEDIR/utils/yosys_gf.ys
yosys -s $BASEDIR/utils/yosys_rf.ys

python $BASEDIR/utils/transfer_blif.py Mgf.blif
python $BASEDIR/utils/transfer_blif.py Mrf.blif

python $BASEDIR/utils/transfer_myoutput.py new_Mgf.blif new_Mrf.blif $BASEDIR/utils/my_std_cell.blif

cd $BASEDIR/../../abc-master
# ./abc -c "read_blif $BASEDIR/$1/my_output.blif; sat;"
./abc -c "cec $BASEDIR/$1/my_output.blif $BASEDIR/$1/my_const.blif;"
# cec ../final_project/src/testcases/case1/my_output.blif ../final_project/src/testcases/case1/my_const.blif