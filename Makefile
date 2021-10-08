pdf: info.md static
	pandoc info.md -o out.pdf

clean:
	rm *.pdf
