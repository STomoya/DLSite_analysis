setup:
	python /src/python/initual.py
	python /src/python/scrape_info.py
	python /src/python/extract_basic_info.py
	python /src/python/count_tag_by_actor.py
	python /src/python/create_variable.js.py

update:
	python /src/python/extract_basic_info.py
	python /src/python/count_tag_by_actor.py
	python /src/python/create_variable.js.py