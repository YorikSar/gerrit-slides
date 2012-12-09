
.PHONY: page git

page: .html/index.html .html/images 

git: page
	cd .html;\
		if [ "$$(git status -s)" ]; then \
			git commit -am "Update to master branch" && git push origin gh-pages; \
		fi

.html/index.html: slides.rst | .html
	./rst2s5.py --theme-url ui/advanced_utf $< $@

.html:
	git clone -s -b gh-pages . .html

.html/images: images
	cp -rv images .html/
