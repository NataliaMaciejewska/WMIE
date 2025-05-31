-- Insert a record into the `application` table for each schema
INSERT INTO WNSP.subjects_application (name, background_path, description)
VALUES ('WNSP App', '/static/wnsp.jpg', 'This is the WNSP application.');

INSERT INTO WA.subjects_application (name, background_path, description)
VALUES ('WA App', '/static/wa.jpg', 'This is the WA application.');

INSERT INTO CM.subjects_application (name, background_path, description)
VALUES ('CM App', '/static/cm.jpg', 'This is the CM application.');

INSERT INTO WNPE.subjects_application (name, background_path, description)
VALUES ('WNPE App', '/static/wnpe.jpg', 'This is the WNPE application.');

INSERT INTO WNIT.subjects_application (name, background_path, description)
VALUES ('WNIT App', '/static/wnit.jpg', 'This is the WNIT application.');

INSERT INTO WNS.subjects_application (name, background_path, description)
VALUES ('WNS App', '/static/wns.jpg', 'This is the WNS application.');

INSERT INTO WH.subjects_application (name, background_path, description)
VALUES ('WH App', '/static/wh.jpeg', 'This is the WH application.');
