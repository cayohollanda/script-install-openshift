#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
# SCRIPT PARA SUBIR O OPENSHIFT SEM PRECISAR RODAR O COMANDO #
##############################################################

# Rodar comandos no bash
import os

# Verificando se OpenShift Client Tools está instalado
verifyIfOcIsInstalled = os.system("oc version > /dev/null")

if verifyIfOcIsInstalled != 256:
    print("Erro ao executar comando. Verifique se o OpenShift Client Tools está instalado.")
    exit()

# Coletando informações
public_hostname = raw_input("[?] DNS ou IP interno da máquina virtual -> ")
while public_hostname == '':
    public_hostname = raw_input("[?] DNS ou IP interno da máquina virtual -> ")

routing_suffix = raw_input("[?] IP público da máquina virtual -> ")
while routing_suffix == '':
    routing_suffix = raw_input("[?] IP público da máquina virtual -> ")

# Rodando script
commandRun = os.system("oc cluster up --skip-registry-check=true --public-hostname=%s --routing-suffix=%s" %(public_hostname, routing_suffix))