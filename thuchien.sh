clear
echo "Nhap vao lenh can thuc hien"
read -p "lenh = " lenh
echo "Nhap vao tham so"
read -p "arg = " arg
$lenh $arg
if test $? -eq 0; then
	clear 
	echo "Xong roi"
else 
	echo "Loi!!"
fi

