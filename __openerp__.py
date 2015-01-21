{
    'name' : 'Parking Management System',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Parking Management System',
    'depends' : ['base_setup','base','hr'],
    'init_xml' : [],
    'data' : [			
        'security/jakc_parking_security.xml',
        'security/ir.model.access.csv',             
        'jakc_parking_view.xml',
        'jakc_parking_menu.xml',        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}