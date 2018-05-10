clear 
echo "Nhap so thu nhat"
read -p "a=" a
echo "Nhap so thu hai"
read -p "b=" b 
echo "Tham so ban da truyen vao la: $a va $b"
echo "$a + $b =  `expr $a + $b` "
echo "$a - $b =  `expr $a - $b` "
echo "$a * $b =  `expr $a \* $b`"

if test $b -eq 0; then
	echo "So chia bang 0 nen khong the chia"
else
	echo "$a / $b =  `expr $a / $b` "
	echo "$a % $b =  `expr $a % $b` "
fi
