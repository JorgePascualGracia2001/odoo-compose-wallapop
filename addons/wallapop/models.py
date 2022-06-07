# -*- coding: utf-8 -*-
import random
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Estudiante(models.Model):
    _name = 'estudiante'
    name = fields.Char(string="Nombre")
    dni = fields.Char(string="DNI")
    email = fields.Char(string="Correo")
    telefono = fields.Char(string="Telefono")
    laptop = fields.Boolean('Posee Portatil', compute='_checkLaptop')
    portatil_id = fields.One2many('portatil',
                                  'estudiante_id',
                                   string="Portatiles poseidos")

    


    @api.depends('laptop')
    def _checkLaptop(self):
        for record in self:
            if len(record.portatil_id) != 0:
                record.laptop = True
            else:
                record.laptop = False



    @api.constrains('dni')
    def _checkDNI(self):

        REGEXP = "[0-9]{8}[A-Z]"
        DIGITO_CONTROL = "TRWAGMYFPDXBNJZSQVHLCKE"
        INVALIDOS = {"00000000T", "00000001R", "99999999R"}

        for record in self:
            print(record)
            if( record.dni in INVALIDOS 
                and re.match(REGEXP, record.dni) is None 
                and record.dni[8] != DIGITO_CONTROL[int(record.dni[0:8]) % 23]
            ):
                return  ValidationError("The dni is invalid")
            

    
    

class Portatil(models.Model):
    _name = 'portatil'
    name = fields.Char(string="Nombre")
    marca = fields.Char(string="Marca")
    cpu = fields.Char(string="Cpu")
    grafica = fields.Char(string="Grafica")
    ram = fields.Char(string="RAM")
    storage = fields.Char(string="Almacenamiento")
    estudiante_id = fields.Many2one('estudiante', string='Estudiante')
    prize = fields.Char(string="Presio")




    
    

    