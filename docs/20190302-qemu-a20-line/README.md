# qemu-A20-line

qemu-system-i386では A20 line が最初からonになっていることを発見したので一応メモ。

とりあえず[このページ](http://www.independent-software.com/operating-system-development-enabling-a20-line.html)にしたがって、1MiB以上のアドレスに何かを書き込んだ時の挙動を見て判断してみる。もし A20 line がoffになっていれば画面にはAと出て、onになっていればBと出るようなものを書いてみる。

```
bits 16

start:
	xor ax, ax
  mov es, ax
	mov di, 0x0500
	mov ax, 0xffff
	mov ds, ax
  mov si, 0x0510
	mov byte [es:di], 0x00
	mov byte [ds:si], 0xff
	cmp byte [es:di], 0xff
	jz owrtn
	mov al, 0x42
	mov ah, 0x0e
	int 0x10
	jmp $
owrtn:
	mov al, 0x41
	mov ah, 0x0e
	int 0x10
	jmp $
times 510 - ($-$$) db 0
dw 0xaa55
```


結果としてはBと出た。要するにonになっているようだ。

少し調べてみると[こんなスレッド](https://www.reddit.com/r/osdev/comments/a20q4j/change_status_of_a20_line_when_qemu_starts/)も見つかったので、多分この結果はあってるはず。
