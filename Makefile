run:
	livereload -w 1 &
	export FLASK_APP=thermostat.py && export FLASK_ENV=development && flask run
