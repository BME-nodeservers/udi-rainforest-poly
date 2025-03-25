udi-rainforest-poly.zip: eagle.py
	cp README.md ../docs/udi-rainforest-poly.md
	zip -r ../udi-rainforest-poly.zip \
		LICENSE \
		Makefile \
		POLYGLOT_CONFIG.md \
		README.md \
		eagle.py \
		install.sh \
		nodes \
		profile \
		requirements.txt 
