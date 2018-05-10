clear
echo "Nhap ten thu muc:"
read -p "dir_name=" dir_name
mkdir $dir_name
if test $? -eq 0; then
	clear
	echo "Thu muc $dir_name da duoc tao ^^"
else
	clear
	echo "Khong the tao thu muc ten $dir_name"
fi
