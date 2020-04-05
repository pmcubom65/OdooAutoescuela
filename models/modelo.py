# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'autoescuela'

    name = fields.Char('Nombre de la autoescuela', required=True)
    domicilio = fields.Char('Domicilio')
    localidad = fields.Char('Localidad')
    provincia = fields.Char('Provincia')
    examen_id = fields.Many2many('examen.examen', string='Examenes')
    profesor_id = fields.One2many('profesor.profesor', 'autoescuela_id', string='Profesores asignados')
    alumno_id = fields.One2many('pedro.pedro', 'autoescuela_id', string='Autoescuela asignada')
    contacto = fields.Char('Contacto')



class Profesor(models.Model):
    _name = 'profesor.profesor'
    _description = 'profesor'

    name = fields.Char('Nombre del profesor', required=True)
    dni = fields.Char('DNI del profesor', required=True)
    coche = fields.Char('Coche del profesor', required=True)
    matricula = fields.Char('Matricula del coche', required=True)
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string='Autoescuela asignada')
    alumno_id = fields.One2many('pedro.pedro', 'profesor_id', string='alumnos del profesor')



class Examen(models.Model):
    _name = 'examen.examen'
    _description = 'examen'

    name = fields.Char('Codigo del Examen', required=True)
    fecha = fields.Date('Fecha del Examen')
    examen_autoescuela_ids = fields.Many2many('autoescuela.autoescuela', string='Examenes de la Autoescuela', relation='autoescuela_autoescuela_examen_examen')
    alumno_id=fields.One2many('pedro.pedro', 'examen_id', string='Alumno a Examinar')
    moneda_id=fields.Many2one('res.currency', string="Moneda")
    precio=fields.Monetary('Precio del Examen', currency_field='moneda_id')
    clases = fields.Char('Numero de clases')
    carnet = fields.Char('Tipo de Carnet')
    aprobado = fields.Char('Aprobado')


class Alumno(models.Model):
    _name = 'pedro.pedro'
    _description = 'alumno'

    name = fields.Char('Nombre del alumno', required=True)
    dni = fields.Char('DNI del alumno', required=True)
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string='Autoescuela')
    profesor_id=fields.Many2one('profesor.profesor', string='Profesor Habitual')
    examen_id=fields.Many2one('examen.examen', string='Examen')
    domicilio = fields.Char('Contacto')
    matricula = fields.Char('Numero de Matricula')
    