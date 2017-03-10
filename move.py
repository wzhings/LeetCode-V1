# Another Reference: http://www.cnblogs.com/zhurun/archive/2015/06/20/4590755.html

def move(n, a, b, c):
	if n == 1:
		print('move', a, '-->', c)
		return
	move(n - 1, a, c, b)   # 将前 n-1个盘子从x移动到y上
	move(1, a, b, c)   # 将最底下的最后一个盘子从x移到到z上
	move(n - 1, b, a, c)  # 将y上的n-1个盘子移到z上

move(4, 'A', 'B', 'C')	