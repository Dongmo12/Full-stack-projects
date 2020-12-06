--CREATE DATABASE calsstest;
DROP TABLE IF NOT EXISTS projects;
CREATE TABLE projects(project_id SERIALIZABLE PRIMARY KEY, name VARCHAR(50), description VARCHAR(100));

insert into projects(name, description)
values ('di_implementation','This project aims to test the new features.'),('f2','This projectsas.')('f3','This projectdsdssas.')('f4','This projsasectsas.')('f5','This asasprojectsas.');