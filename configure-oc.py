#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################
# SCRIPT PARA CONFIGURAR O AMBIENTE #
#####################################

# Rodar comandos no bash
import os
import os.path

# Acessar OS
import platform

# Método responsável por instalar uma dependência
def instalaPacote(packageManager, pacote):
    os.system(packageManager + pacote)

# Método responsável por instalar o Docker
def instalaDocker(pm):
    if pm.find("yum"):
        instalaPacote(pm, 'yum-utils \
            device-mapper-persistent-data \
            lvm2')
        os.system("yum-config-manager \
            --add-repo \
            https://download.docker.com/linux/centos/docker-ce.repo")
        instalaPacote(pm, 'docker-ce')
    else:
        instalaPacote(pm, 'apt-transport-https \
            ca-certificates \
            curl \
            software-properties-common')
        os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
        os.system("apt-key fingerprint 0EBFCD88")
        os.system("sudo add-apt-repository \
            'deb [arch=amd64] https://download.docker.com/linux/ubuntu \
            $(lsb_release -cs) \
            stable'")
        os.system("apt-get update")
        instalaPacote(pm, 'docker-ce')
    
    os.system("systemctl start docker")
    os.service("systemctl daemon-reload")
    os.system("service docker restart")

# Método responsável por instalar o OpenShift Client Tools
def instalaOcTools():
    if not os.path.isfile("openshift-origin-client-tools-v3.10.0-dd10d17-linux-64bit.tar.gz"):
        os.system("wget https://github.com/openshift/origin/releases/download/v3.10.0/openshift-origin-client-tools-v3.10.0-dd10d17-linux-64bit.tar.gz")

    os.system("tar -xvf openshift-origin-client-tools-v3.10.0-dd10d17-linux-64bit.tar.gz")
    os.system("cp openshift-origin-client-tools-v3.10.0-dd10d17-linux-64bit/oc /usr/local/bin/")

# Verificando se o docker está instalado
verifyDockerInstalled = os.system("docker version > /dev/null")

# Verificando se o OpenShift Client Tools está instalado
verifyOcInstalled = os.system("oc version > /dev/null")

# Verificando sistema operacional
verifyOperationSystem = os.path.exists("/etc/redhat-release")

# Setando gerenciador de pacotes default como o do Debian
packageManager = 'apt-get install -y '

# Se for uma dist baseada no RedHat, ele muda o gerenciador de pacotes para o do RedHat
if verifyOperationSystem == True:
    packageManager = 'yum install '

# Se não tiver o Docker instalado, ele instalará
if verifyDockerInstalled != 0:
    instalaDocker(packageManager)

# Se não tiver o OpenShift Client Tools instalado, ele instalará
if verifyOcInstalled != 0:
    instalaOcTools()

print("[*] Dependências instaladas com sucesso!")