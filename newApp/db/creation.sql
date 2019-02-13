
CREATE TABLE Vd_subscription (
	user_id INT NOT NULL,
	start_date DATETIME,
	end_date DATETIME NOT NULL,
	price FLOAT NOT NULL,
	video_id INT NOT NULL,
	PRIMARY KEY (user_id,video_id)
);

CREATE TABLE Video (
	video_id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255) NOT NULL,
	price_day FLOAT NOT NULL,
	PRIMARY KEY (video_id)
);

CREATE TABLE User (
	user_id INT NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	type_id INT NOT NULL,
	PRIMARY KEY (user_id)
);

CREATE TABLE genres (
	video_id INT NOT NULL,
	genre varchar(255) NOT NULL,
	PRIMARY KEY (video_id,genre)
);

CREATE TABLE Pack_subscription (
	user_id INT NOT NULL AUTO_INCREMENT,
	start_date DATETIME NOT NULL,
	end_date DATETIME NOT NULL,
	price FLOAT NOT NULL,
	pack_id INT NOT NULL,
	PRIMARY KEY (user_id,pack_id)
);

CREATE TABLE Pack_content (
	pack_id INT NOT NULL,
	video_id INT NOT NULL,
	PRIMARY KEY (pack_id,video_id)
);

CREATE TABLE Pack (
	pack_id INT NOT NULL,
	daily FLOAT NOT NULL,
	weekly FLOAT NOT NULL,
	monthly FLOAT NOT NULL,
	yearly FLOAT NOT NULL,
	title varchar(255) NOT NULL,
	PRIMARY KEY (pack_id)
);

CREATE TABLE Add_on (
	pack_id1 INT NOT NULL,
	pack_id2 INT NOT NULL,
	option1_price FLOAT NOT NULL,
	option2_price FLOAT NOT NULL,
	option2_ppv FLOAT NOT NULL,
	PRIMARY KEY (pack_id1,pack_id2)
);

CREATE TABLE Type (
	type_id INT NOT NULL AUTO_INCREMENT,
	name varchar(255) NOT NULL,
	disc_factor FLOAT NOT NULL,
	PRIMARY KEY (type_id)
);

CREATE TABLE ppv_subscription (
	user_id INT NOT NULL,
	pack_id INT NOT NULL,
	start_end DATETIME NOT NULL,
	end_date DATETIME NOT NULL,
	price FLOAT NOT NULL,
	price_ppv FLOAT NOT NULL
);

ALTER TABLE Vd_subscription ADD CONSTRAINT Vd_subscription_fk0 FOREIGN KEY (user_id) REFERENCES User(user_id);

ALTER TABLE Vd_subscription ADD CONSTRAINT Vd_subscription_fk1 FOREIGN KEY (video_id) REFERENCES Video(video_id);

ALTER TABLE User ADD CONSTRAINT User_fk0 FOREIGN KEY (type_id) REFERENCES Type(type_id);

ALTER TABLE genres ADD CONSTRAINT genres_fk0 FOREIGN KEY (video_id) REFERENCES Video(video_id);

ALTER TABLE Pack_subscription ADD CONSTRAINT Pack_subscription_fk0 FOREIGN KEY (user_id) REFERENCES User(user_id);

ALTER TABLE Pack_subscription ADD CONSTRAINT Pack_subscription_fk1 FOREIGN KEY (pack_id) REFERENCES Pack(pack_id);

ALTER TABLE Pack_content ADD CONSTRAINT Pack_content_fk0 FOREIGN KEY (pack_id) REFERENCES Pack(pack_id);

ALTER TABLE Pack_content ADD CONSTRAINT Pack_content_fk1 FOREIGN KEY (video_id) REFERENCES Video(video_id);


ALTER TABLE Add_on ADD CONSTRAINT Add_on_fk0 FOREIGN KEY (pack_id1) REFERENCES Pack(pack_id);

ALTER TABLE Add_on ADD CONSTRAINT Add_on_fk1 FOREIGN KEY (pack_id2) REFERENCES Pack(pack_id);

ALTER TABLE ppv_subscription ADD CONSTRAINT ppv_subscription_fk0 FOREIGN KEY (user_id) REFERENCES User(user_id);

ALTER TABLE ppv_subscription ADD CONSTRAINT ppv_subscription_fk1 FOREIGN KEY (pack_id) REFERENCES Pack(pack_id);

