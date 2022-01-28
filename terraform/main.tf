# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  backend "azurerm" {
    resource_group_name   = "pers-robin_mohan-rg"
    storage_account_name  = "storageforrobin"
    container_name        = "tstate"
    key                   = "Rk/X+EPlwSzzBaOrI2UGzVgeaorD+fXPXRllYSG1v2IOv7IqAepI3WDhqRR9Vo60S9zHXJN4GxIcoyR++FR2zA=="
}
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  skip_provider_registration = true
  features {}
}


variable "prefix" {
  default = "featuretest"
}

variable "resource_group_name" {
  default = "pers-robin_mohan-rg"
}

variable "resource_group_location" {
    default = "eastus"
}


resource "azurerm_virtual_network" "main" {
  name                = "${var.prefix}-network"
  address_space       = ["10.0.0.0/16"]
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
}

resource "azurerm_subnet" "internal" {
  name                 = "internal"
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_public_ip" "main" {
  name = "${var.prefix}-pip"
  location = var.resource_group_location
  resource_group_name = var.resource_group_name
  allocation_method = "Dynamic"
  sku = "Basic"
}

resource "azurerm_network_security_group" "main" {
  name                = "${var.prefix}-securitygroup"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name

  security_rule {
    name                       = "SSH"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = 22
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = {
    environment = "testing"
  }
}

resource "azurerm_network_interface" "main" {
  name                = "${var.prefix}-nic"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "testconfiguration1"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.main.id
  }
}

resource "azurerm_virtual_machine" "main" {
  name                  = "${var.prefix}-vm"
  location              = var.resource_group_location
  resource_group_name   = var.resource_group_name
  network_interface_ids = [azurerm_network_interface.main.id]
  vm_size               = "Standard_DS1_v2"

  # Uncomment this line to delete the OS disk automatically when deleting the VM
  delete_os_disk_on_termination = true

  # Uncomment this line to delete the data disks automatically when deleting the VM
  delete_data_disks_on_termination = true

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
  storage_os_disk {
    name              = "myosdisk1"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
  os_profile {
    computer_name  = "hostname"
    admin_username = "testadmin"
    admin_password = "Password1234!"
  }
  os_profile_linux_config {
    disable_password_authentication = false
  }
  tags = {
    environment = "testing"
  }
}

#this exports the ip to the hosts.cfg file for Ansible
# resource "local_file" "hosts_cfg" {
#   content = templatefile("${path.module}/templates/hosts.tpl",
#     {
#       test_clients = azurerm_public_ip.main.*.ip_address
#     }
#   )
#   filename = "../ansible/inventory/hosts.cfg"
# }

resource "local_file" "hosts_cfg" {
  content = templatefile("/tmp/hosts.tpl",
    {
      test_clients = azurerm_public_ip.main.*.ip_address
    }
  )
  filename = "tmp/hosts.cfg"
}

