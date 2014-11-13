PYUIC = pyuic5
FORMS = form_ui.py

%_ui.py : %.ui
	$(PYUIC) $< > $@

all: $(FORMS)

clean:
	rm -rf __pycache__
	rm *_ui.py
