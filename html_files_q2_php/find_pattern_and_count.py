# -*- coding: utf-8 -*-
# html_files = ['file.html']
# copyright = '<p class="text-muted">&copy; 2014. Core Team</p>'
# new_copyright = """<?php
	# $year = date("Y");
	# echo "<p class='text-muted'>© $year. Core Team</p>";
	# ?>"""
# for html_file_path in html_files:
	# with open(html_file_path) as html_file:
		# html = html_file.read()

	# if copyright in html:
		# php_file_path = html_file_path.replace('.html', '.php')
		# with open(php_file_path, "w") as php_file:
			# php = html.replace(copyright, new_copyright)
			# php_file.write(php)
			
with open('file', 'r') as myfile:
	data=myfile.read().replace('\n', '')
with open('old', 'r') as myfile:
	search=myfile.read().replace('\n', '')

print data.count(search)