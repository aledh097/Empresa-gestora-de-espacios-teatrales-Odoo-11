# -*- coding: utf-8 -*-
{
    'name': "upoteatro",
    'summary': """Empresa Gestora de Espacios Teatrales""",
    'description': """Nuestro sistema tiene como fin gestionar un espacio teatral, que será llevado a cabo por un administrador, para ello desarrollaremos un Módulo personalizado en un sistema ERP que permita realizar su cometido. Nos hemos decidido por Odoo por ser un ERP de código abierto y disponer de una interfaz web (requisito del cliente).""",
    'author': "Alejandro Palomino, Álvaro García, Jesús Sena y Juan Alberto García",
    'category': 'teatro',
    'version': '0.1',
    'depends': ['base'],
    'data': ['views/teatro_view.xml','views/espectaculo_view.xml','views/representacion_view.xml',
             'views/butaca_view.xml','views/entrada_view.xml','views/obra_view.xml',
             'views/compania_view.xml','views/idioma_view.xml','views/interprete_view.xml'], # el orden es en el que aparecen en Odoo. Si no sale bien, hay que reinstalar el módulo
    'demo': ['demo/datosPrueba.xml'],
    'application': True,
}
