# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import Response
import json

class UserController(http.Controller):

    @http.route('/api/user', auth='public', method=['GET'], csrf=False)
    def get_users(self, **kw):
        try:
            users = http.request.env['res.users'].sudo().search_read([], ['id','name','login','lang','company_id'])
            res = json.dumps(users, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='aplication/json;charset=utf-8', status=200)

        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='aplication/json;charset=utf-8', status=505)

    @http.route('/api/hello', auth='public', website=True)
    def say_hello(self, **kw):
        return "Hola mundo - " + http.request.params['nombre']
