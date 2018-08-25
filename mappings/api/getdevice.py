# -*- config: utf-8 -*-

def changed_by(data):
    return {
        'id': data['id'],
        'code': data['code]',
        'message': data['message'] if type(data['message']) is str else '',
        'data': __to_data(data['message'])
    }

def __to_data(message):
    if type(message) is str:
        return {}
    else:
        values = []
        for key, value in message.items():
            values.append({'key': key, 'value': value})
        return values
