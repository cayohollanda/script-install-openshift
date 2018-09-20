#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
# SCRIPT PARA SUBIR O OPENSHIFT SEM PRECISAR RODAR O COMANDO #
##############################################################

# Rodar comandos no bash
import os

# Coletando informações
public_hostname = raw_input("[?] DNS ou IP interno da máquina virtual -> ")
routing_suffix = raw_input("[?] IP público da máquina virtual -> ")

# Rodando script
os.system("oc cluster up --skip-registry-check=true --public-hostname=%s --routing-suffix=%s" %(public_hostname, routing_suffix));
