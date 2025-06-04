-- Wstaw pytania do tabeli Survey
INSERT INTO users_survey (id, question)
VALUES
    (1, 'Co Cię bardziej interesuje?'),
    (2, 'Co Cię bardziej interesuje?'),
    (3, 'Co Cię bardziej interesuje?'),
    (4, 'Co Cię bardziej interesuje?'),
    (5, 'Co Cię bardziej interesuje?'),
    (6, 'Co Cię bardziej interesuje?'),
    (7, 'Co Cię bardziej interesuje?'),
    (8, 'Co Cię bardziej interesuje?'),
    (9, 'Co Cię bardziej interesuje?'),
    (10, 'Co Cię bardziej interesuje?'),
    (11, 'Co Cię bardziej interesuje?'),
    (12, 'Co Cię bardziej interesuje?'),
    (13, 'Co Cię bardziej interesuje?'),
    (14, 'Co Cię bardziej interesuje?'),
    (15, 'Co Cię bardziej interesuje?'),
    (16, 'Co Cię bardziej interesuje?'),
    (17, 'Co Cię bardziej interesuje?'),
    (18, 'Co Cię bardziej interesuje?'),
    (19, 'Co Cię bardziej interesuje?'),
    (20, 'Co Cię bardziej interesuje?'),
    (21, 'Co Cię bardziej interesuje?');

INSERT INTO users_department (id, name)
VALUES
    (1, 'Wydział Artystyczny'),
    (2, 'Wydział Humanistyczny'),
    (3, 'Wydział Lekarski i Nauk o Zdrowiu'),
    (4, 'Wydział Nauk Inżynieryjno-Technicznych'),
    (5, 'Wydział Nauk Prawnych i Ekonomicznych'),
    (6, 'Wydział Nauk Społecznych'),
    (7, 'Wydział Nauk Ścisłych i Przyrodniczych');

INSERT INTO users_departmentinterest (department_id, interest_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),

    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (2, 11),
    (2, 12),

    (3, 13),
    (3, 14),
    (3, 15),
    (3, 16),
    (3, 17),
    (3, 18),

    (4, 19),
    (4, 20),
    (4, 21),
    (4, 22),
    (4, 23),
    (4, 24),

    (5, 25),
    (5, 26),
    (5, 27),
    (5, 28),
    (5, 29),
    (5, 30),

    (6, 31),
    (6, 32),
    (6, 33),
    (6, 34),
    (6, 35),
    (6, 36),

    (7, 37),
    (7, 38),
    (7, 39),
    (7, 40),
    (7, 41),
    (7, 42);

-- Wstaw zainteresowania do tabeli Interest

INSERT INTO users_interest (id, name)
VALUES
    (1, 'Projektowanie przestrzeni i wnętrz'),
    (2, 'Tworzenie ilustracji i grafiki cyfrowej'),
    (3, 'Śpiewanie lub gra na instrumencie'),
    (4, 'Improwizacja muzyczna'),
    (5, 'Malowanie obrazów lub rysowanie'),
    (6, 'Eksperymentowanie ze sztuką współczesną'),
    (7, 'Uczenie się języków obcych'),
    (8, 'Prowadzenie rozmów na trudne tematy i doradzanie innym'),
    (9, 'Czytanie książek i analizowanie ich treści'),
    (10, 'Zainteresowanie historią i przeszłością'),
    (11, 'Tworzenie własnych opowiadań, światów lub scenariuszy'),
    (12, 'Pogłębianie idei, wartości i sensu życia'),
    (13, 'Pomaganie innym w sytuacjach kryzysowych'),
    (14, 'Zainteresowanie ludzkim ciałem i anatomią'),
    (15, 'Opiekowanie się innymi i dbanie o ich zdrowie'),
    (16, 'Uczenie się o chorobach i sposobach ich leczenia'),
    (17, 'Współpraca w zespole i działanie pod presją'),
    (18, 'Zainteresowanie rehabilitacją i sprawnością fizyczną'),
    (19, 'Rozwiązywanie problemów technicznych lub logicznych'),
    (20, 'Budowanie lub projektowanie urządzeń i konstrukcji'),
    (21, 'Zainteresowanie nowoczesnymi technologiami i innowacjami'),
    (22, 'Zarządzanie projektami technicznymi lub produkcją'),
    (23, 'Zainteresowanie energią, środowiskiem i zrównoważonym rozwojem'),
    (24, 'Programowanie lub praca z danymi i systemami cyfrowymi'),
    (25, 'Zainteresowanie przepisami prawa i ich zastosowaniem'),
    (26, 'Analizowanie danych finansowych lub budżetu'),
    (27, 'Zarządzanie zespołem lub podejmowanie decyzji organizacyjnych'),
    (28, 'Zainteresowanie bezpieczeństwem państwa i systemami ochrony'),
    (29, 'Planowanie procesów logistycznych lub łańcuchów dostaw'),
    (30, 'Obserwowanie trendów gospodarczych i rynkowych'),
    (31, 'Zrozumienie zachowań ludzi i relacji społecznych'),
    (32, 'Zainteresowanie systemem edukacji i pracą z dziećmi lub młodzieżą'),
    (33, 'Obserwowanie i komentowanie wydarzeń politycznych'),
    (34, 'Rozwiązywanie problemów społecznych i pomaganie w zmianie'),
    (35, 'Zainteresowanie komunikacją i językiem w kontekście społecznym'),
    (36, 'Analiza danych społecznych i badania opinii publicznej'),
    (37, 'Zainteresowanie naukami przyrodniczymi, np. biologią czy chemią'),
    (38, 'Obserwowanie zjawisk fizycznych i zrozumienie zasad rządzących światem'),
    (39, 'Rozwiązywanie zadań matematycznych i logicznych zagadek'),
    (40, 'Analiza danych i wykorzystywanie statystyki w praktyce'),
    (41, 'Zainteresowanie środowiskiem naturalnym i jego ochroną'),
    (42, 'Zgłębianie zasad zdrowego stylu życia, odżywiania i aktywności fizycznej');

-- Powiązania pytań z zainteresowaniami
INSERT INTO users_survey_interests (id, survey_id, interest_id)
VALUES
    -- Pytanie 1:
    (1, 1, 5),
    (2, 1, 7),

    -- Pytanie 2:
    (3, 2, 2),
    (4, 2, 13),

    -- Pytanie 3:
    (5, 3, 1),
    (6, 3, 19),

    -- Pytanie 4:
    (7, 4, 4),
    (8, 4, 25),

    -- Pytanie 5:
    (9, 5, 3),
    (10, 5, 31),

    -- Pytanie 6:
    (11, 6, 6),
    (12, 6, 37),

    -- Pytanie 7:
    (13, 7, 8),
    (14, 7, 18),

    -- Pytanie 8:
    (15, 8, 9),
    (16, 8, 20),

    -- Pytanie 9:
    (17, 9, 10),
    (18, 9, 26),

    -- Pytanie 10:
    (19, 10, 12),
    (20, 10, 36),

    -- Pytanie 11:
    (21, 11, 11),
    (22, 11, 40),

    -- Pytanie 12:
    (23, 12, 15),
    (24, 12, 22),

    -- Pytanie 13:
    (25, 13, 16),
    (26, 13, 30),

    -- Pytanie 14:
    (27, 14, 17),
    (28, 14, 32),

    -- Pytanie 15:
    (29, 15, 14),
    (30, 15, 38),

    -- Pytanie 16:
    (31, 16, 24),
    (32, 16, 28),

    -- Pytanie 17:
    (33, 17, 23),
    (34, 17, 33),

    -- Pytanie 18:
    (35, 18, 21),
    (36, 18, 42),

    -- Pytanie 19:
    (37, 19, 29),
    (38, 19, 34),

    -- Pytanie 20:
    (39, 20, 27),
    (40, 20, 41),

    -- Pytanie 21:
    (41, 21, 35),
    (42, 21, 39);

