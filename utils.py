from flask_restful import reqparse, fields


def get_query():
    """ Returns the query parameter from the request for searching the news. """
    parser = reqparse.RequestParser()
    parser.add_argument('query')
    args = parser.parse_args()
    q = args.get('query')
    return q


def get_resource_fields(source=None):
    """ Returns the expected dict keys for JSON output. """
    resource_fields = dict()
    resource_fields['headline'] = fields.String(attribute='title')
    resource_fields['link'] = fields.String(attribute='url')
    if not source:
        resource_fields['source'] = fields.String(attribute='source.name')
    else:
        resource_fields['source'] = fields.String(default='reddit')

    return resource_fields
