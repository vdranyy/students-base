from django.db import connection
from django.template.loader import render_to_string
from django.utils.encoding import smart_unicode
from datetime import datetime


class SQLMiddleware(object):
		
	def process_response(self, request, response):
		start_time =  datetime.now()
		count = 0
		for query in connection.queries:
			count += 1
		end_time = datetime.now()
		execution_time = end_time - start_time
		context = {'count': count, 'time': execution_time}
		render_template = render_to_string('sql_extension.html', context)
		response.content = smart_unicode(response.content).replace('</body>', render_template)
		return response

