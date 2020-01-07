# -*- coding: utf-8 -*-
{
    'name': "upoteatro_extension",
    'summary': """Extensión del módulo upoteatro""",
    'description': """Extensión que añade los modelos: entradaIndividual, entradaGrupal y Autobús para las entradas grupales.""",
    'author': "Alejandro Palomino, Álvaro García, Jesús Sena y Juan Alberto García",
    'category': 'teatro',
    'version': '0.1',
    'depends': ['upoteatro'],
    'data': ['views/entradaindividual_view.xml','views/entradagrupal_view.xml','views/entrada_view.xml'],
    'demo': [],
    #'demo': ['demo/datosPrueba.xml'],
    'application': True,
}