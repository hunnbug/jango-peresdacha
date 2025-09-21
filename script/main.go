package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	de, err := os.ReadDir("../coolproject/school/templates")
	if err != nil {
		fmt.Println(err)
	}

	for _, item := range de {
		if item.IsDir() {
			continue
		}
		if item.Name() == "base.html" {
			continue
		}

		doShit(item.Name())
	}
}

func doShit(name string) {

	str1 := `{% extends 'base.html' %}
{% load static %}`
	str2 := `{% block content %}`
	str3 := `{% endblock %}`

	stringList := `{% block title_name %}
    Список 
{% endblock %}
`
	stringDetail := `{% block title_name %}
    Просмотр
{% endblock %}
`
	stringCreate := `{% block title_name %}
    Создание
{% endblock %}
`
	stringUpdate := `{% block title_name %}
    Обновление
{% endblock %}
`
	stringDelete := `{% block title_name %}
    Удаление
{% endblock %}
`

	badLine := "<!DOCTYPE html>"

	lines := make([]string, 0, 150)
	lines = append(lines, str1, str2)

	if strings.Contains(name, "_list") {
		lines = append(lines, stringList)
	}
	if strings.Contains(name, "_detail") {
		lines = append(lines, stringDetail)
	}
	if strings.Contains(name, "_create") {
		lines = append(lines, stringCreate)
	}
	if strings.Contains(name, "_update") {
		lines = append(lines, stringUpdate)
	}
	if strings.Contains(name, "_delete") {
		lines = append(lines, stringDelete)
	}

	name = "../coolproject/school/templates/" + name

	file, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if !strings.Contains(line, badLine) {
			lines = append(lines, line)
		}
	}

	lines = append(lines, str3)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
		return
	}

	os.WriteFile(name, []byte(strings.Join(lines, "\n")), 0644)
}
