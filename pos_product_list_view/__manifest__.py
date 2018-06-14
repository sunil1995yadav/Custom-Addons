# -*- encoding: utf-8 -*-
##############################################################################
#
#    Authors: sunil, 
#    Copyright Knacktechs SA 2016
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'POS Product In List View',
    'description': """
        Product Show in list view in Pont of Sale
""",
    'version': '1.1',
    'author': "Knacktechs Solutions",
    'license': '',
    'summary': """It will show product in list view""",
    'category': 'Point of Sale',
    'website': 'http://www.knacktechs.com',
    'images': [],
    'depends': ['point_of_sale'],
    'demo': [],
    'data': [   
                'views/point_of_sale.xml',
             ],
    'images': ['static/description/list_view.JPG'],
    'qweb': ['static/xml/pos.xml'],
    'active': False,
    'installable': True,
    'application': True,
}
