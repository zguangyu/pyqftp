all:
	make -C pyqftp
clean:
	rm -rf __pycache__ && make -C pyqftp clean
