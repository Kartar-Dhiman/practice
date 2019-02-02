package main

import (
	"fmt"
	"github.com/koding/multiconfig"
)

type Server struct {
	Name string `required:"true"`
	Port int `default:"6060"`
	Enabled bool
	Users []string
	Database struct {
		ConnectionString string
		Port int
		} `required:"true"`
}

func main() {
	m := multiconfig.NewWithPath("config.toml")

	serverConf := new(Server)

	err := m.Load(serverConf)

	if err!=nil{
		fmt.Println("Error in loading.")
		return
	}

	fmt.Printf("Name of the Server from the config: %s\n", serverConf.Name)
	fmt.Printf("Port of the Database from the config: %d", serverConf.Database.Port)
}