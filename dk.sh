#xoa man hinh
clear
echo "---------------------------"
echo "--cac phep toan so hoc---"
echo "---------------------------"
echo "phep cong(+)"
echo "phep tru(-)"
echo "phep nhan(*)"
echo "phep chia(/)"
echo "ket thuc(e)"
echo "----------------------------"
read -p "moi chon" chon
read -p "a=" a
read -p "b=" b
case $chon in 
	"+" )
		let  "tong=$a+$b"
		echo "tong= $tong";;
	"-" )
		let  "hieu=$a-$b"
		echo "hieu= $hieu";;
	"*" )
		let  "nhan=$a*$b"
		echo "nhan= $nhan";;
	"/" )
		let  "chia=$a/$b"
		echo "chia= $chia";;
	"e" )
	exit;;
esac 




		
