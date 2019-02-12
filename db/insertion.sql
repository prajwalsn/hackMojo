INSERT INTO Type (name,disc_factor) VALUES ('pro','0.9');
INSERT INTO Type (name,disc_factor) VALUES ('guest','1');

INSERT INTO User (email,password,type_id) VALUES ('pro1@gmail.com','pro1','1');
INSERT INTO User (email,password,type_id) VALUES ('pro2@gmail.com','pro2','1');
INSERT INTO User (email,password,type_id) VALUES ('guest3@gmail.com','guest3','2');
INSERT INTO User (email,password,type_id) VALUES ('guest4@gmail.com','guest4','2');
INSERT INTO User (email,password,type_id) VALUES ('pro5@gmail.com','pro5','1');

INSERT INTO Video (title,price_day) VALUES ('Title1','20');
INSERT INTO Video (title,price_day) VALUES ('Title2','340');
INSERT INTO Video (title,price_day) VALUES ('Title3','9');

INSERT INTO genres VALUES ('1','music');
INSERT INTO genres VALUES ('1','dance');
INSERT INTO genres VALUES ('2','comedy');


/*INSERT INTO Pack VALUES ('2','comedy');*/