{
    'name': 'MODULO PEDRO AUTOESCUELA',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'GESTOR DE MI AUTOESCUELA PEDRO',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Pedro',
    'maintainer': 'Pedro',
    'website': 'gestorejemplopedro.com',
    'depends': [],
    'demo': [],
    'data': [
		'security/security.xml',
		'security/ir.model.access.csv',
		'views/autoescuelas.xml',
        'views/alumnos.xml',
        'views/examenes.xml',
        'views/profesores.xml',
		#'views/rrhhempleydepar.xml',
		'views/menus.xml',
		'reports/report.xml',
		'reports/autoescuelareport.xml',
        'reports/profesorreport.xml',
        'reports/examenreport.xml',
        'reports/alumnoreport.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
