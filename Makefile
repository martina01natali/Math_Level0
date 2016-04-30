# makefile per algebra1_dolce_ 1ed
#
# (c) 2014 Daniele Zambelli - daniele.zambelli@gmail.com
#
# tratto da un lavoro di:
# (c) 2013 Dimitrios Vrettos - d.vrettos@gmail.com
# v1.0
#
NAME = m_d_1_les

SHORT_NAME = m_d_1_les

TEX = $(NAME).tex

PDF = $(NAME).pdf

PDFLATEX = pdflatex --shell-escape

FILE_CLEAN = *.aux *.gnuplot *.table *.toc *.log *~ *backup *.old *.veia

ROOT = $(shell basename $$(pwd))

DIRS = chap* lbr

CLEAN_DIRS= $(DIRS:%=clean-%)

DATE = $(shell date "+%Y%m%d")

TAR= $(SHORT_NAME)-$(DATE).tar.gz

ZIP= $(SHORT_NAME)-$(DATE).zip

help:
	@echo ''
	@echo 'Algebra1    - Makefile targets'
	@echo ''
	@echo ' help       - Questo messaggio'
	@echo ' pdf        - Crea il file pdf'
	@echo ' clean      - Rimuove tutti i file ausiliari'
	@echo ' clean-dist - Rimuove tutti i file prodotti'
	@echo ' dist-tar   - Crea una distribuzione (tar.gz) del codice sorgente, esclundendo il file pdf'
	@echo ' dist-zip   - Crea una distribuzione (zip) del codice sorgente, esclundendo il file pdf'
	@echo ''

pdf: $(TEX)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

clean: $(CLEAN_DIRS)
$(CLEAN_DIRS):
	@for i in $(FILE_CLEAN); \
	 do \
		find ./ -type f -name "$$i" -delete ; \
	done

clean-dist: clean
	rm -f $(PDF)
	rm -f *.tar.gz
	rm -f *.zip
 
dist-zip: clean
	rm -f  $(ZIP)
	zip -r $(ZIP) . -x '$(PDF)' -x '*.zip' -x '*.tar.gz'

dist-tar: clean
	rm -f $(TAR)
	tar -czvf $(TAR) --exclude $(PDF) --exclude *.tar.gz --exclude *.zip *

# END OF MAKEFILE

